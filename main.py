from ObjectContainer import ObjectContainer as oc
from objects import init_variables, get_new_global_var, n, get_global_var
from layout import endpoints, links, global_variables, footer
from nice_json import json_print_pretty
from bome_midi_convert import get_bome_midi, to_hex
from GetArgs import getargs


'''
Summary:
 - def run()
 - def test(generated_file)
 - def get_body()
 - def get_endpoint(body, endpoint_name)
 - def create_globals(body)
 - def get_presets(body)
 - def create_preset(options, body=None)
 - def get_global_start_values()
 - def get_translators(body)
 - def get_default_rules(a,b)
 - def create_options_header(link, options)
'''


def run():
    myargs = getargs([
        '--test', 'test_file',
        '-s', 'save_file',
        '-p',
        '--json',
        '-h', '--help'])
    args = myargs.getargs()

    init_variables()
    body = get_body()
    create_globals(body)

    presets        = get_presets(body)
    bome_midi_file = get_bome_midi(presets)

    if '--json' in args:
        print(json_print_pretty(presets))
    elif '-p' in args:
        print('\n'.join(bome_midi_file))

    if '-s' in args:
        # save to file
        with open('save_file') as f:
            f.write(bome_midi_file)

    if '--test' in args:
        test(bome_midi_file, args['test_file'])


    if ('--help' in args and len(args) == 1) or \
       (len(args) == 0):
        result =    '''
        --json                 : print out json format before conversion to bomeMidi format
        --test <bomeMidi file> : run a test with selected bomeMidi file to compare
        -p                     : print out bomeMidi format
        -s     <file name>     : save bomeMidi format as file
        -h, --help             : print help
        '''
        print(result)


def test(generated_file, file_to_test):
    test_passed = True

    test_file = []
    with open(file_to_test) as f:
        test_file = f.readlines()

    for i in range(len(test_file)-4):
        tf = test_file[i+4].rstrip('\n')
        gf = generated_file[i].rstrip('\n')
        if tf != gf:
            test_passed = False
            print('Test Failed! Line:{}'.format(i))
            print('bome: {}'.format(repr(tf)))
            print('')
            print('main: {}'.format(repr(gf)))
            pause = raw_input('\n\npress enter to continue..\n\n')

    if test_passed: print('You Passed!!')


################################################################################



def get_body():
    body = { 'Endpoints': endpoints, 'Links': links, 'Globals': global_variables, 'Footer': footer}
    return body


def get_endpoint(body, endpoint_name):
    endpoints = body['Endpoints']
    try:
        return (e for e in endpoints if e['Name'] == endpoint_name).next()
    except:
        raise Exception('Value \"{}\" does not exist!..'.format(endpoint_name))


def create_globals(body):
    # create default globals for internal settings
    freq = 2
    for g in body['Globals']:
        if g[0] == 'update_freq': freq = g[1]
    get_new_global_var('update_freq', freq) # name/freq in seconds

    # create globals for all cc values
    for value in body['Endpoints']:
        if 'Outgoing' in value and \
           'Note Type' in value['Outgoing'] and \
           value['Outgoing']['Note Type'] == 'cc':
            get_new_global_var(
                value['Name'],
                value['Default'] if 'Default' in value else 0
            )

    # create custom globals
    for g in body['Globals']:
        get_new_global_var(
            g[0],
            g[1] if len(g) >= 2 else 0
        )


def get_presets(body):
    presets = [ create_preset('init') ]
    presets.append( create_preset('links', body) ) 
    return presets


def create_preset(options, body=None):
    result = {}
    if options == 'init':
        # create initial preset
        result = {
            'Name'   : 'Initialize',
            'Active' : 1,
            'Psi'    : 0,     # PresetSwitchIgnore
            'Translators': get_global_start_values()
        }
    elif options == 'links':
        # create linking preset
        result = {
            'Name'   : 'Links',
            'Active' : 1,
            'Psi'    : 0,
            'Translators': get_translators(body)
        }

    return result


def get_global_start_values():
    global_vars = oc._get('global_vars')

    taken_global_vars = []
    for g in global_vars:
        if g['Taken']: taken_global_vars.append(g)

    rules = []
    for g in taken_global_vars:
        rules.append('// {}'.format(g['Taken']))
        rules.append('{}={}'.format(g['Var'], g['Value']))

    options = rules
    options = create_options_header(len(rules), options)

    translator = {
        'Name'    : 'Global Variables',
        'Options' : options,
    }
    return [ translator ]


def get_translators(body):
    end_points = body['Endpoints']
    links      = body['Links']
    result     = []

    for link in links:
        a     = link['Link'][0]
        b     = link['Link'][1]
        rules = link['Options']
        translator = {}

        a = get_endpoint(body, a)
        a_note = a['Incoming']['Note'] if a['Incoming']['Note'] != 'auto' else n(a['Incoming']['Channel'])

        incoming = {
            'Desc'      : a['Name'],
            'Note'      : a_note,
            'Channel'   : a['Incoming']['Channel'],
            'Note Type' : a['Incoming']['Note Type'],
            'Ports'     : a['Ports']
        }

        if a['Incoming']['Note Type'] == 'cc':
            incoming['Note Value'] = get_global_var(a['Name'])

        try_get_endpoint = False
        try:
            b = get_endpoint(body, b)
            try_get_endpoint = True
        except:
            pass

        if try_get_endpoint:
            if b['Outgoing']['Note'] == 'auto':
                b_note = n(b['Outgoing']['Channel'])
            elif b['Outgoing']['Note'] == 'Incoming':
                b_note = a_note
            else:
                b_note = b['Outgoing']['Note']
#            b_note = b['Incoming']['Note'] if b['Incoming']['Note'] != 'auto' else n(b['Incoming']['Channel'])

            outgoing = {
                'Desc'      : b['Name'],
                'Note'      : b_note,
                'Channel'   : b['Outgoing']['Channel'],
                'Note Type' : b['Outgoing']['Note Type'],
                'Ports'     : b['Ports']
            }

            if b['Outgoing']['Note Type'] == 'cc':
                outgoing['Note Value'] = get_global_var(b['Name'])

            options  = get_default_rules(incoming,outgoing)
            options += rules
            options  = create_options_header(link, options)

            translator = {
                'Name'    : '{} -> {}'.format(a['Name'], b['Name']),
                'Incoming': incoming,
                'Outgoing': outgoing,
                'Options' : options,
            }

        else:
            options = rules
            options = create_options_header(link, options)

            translator = {
                'Name'    : '{} -> {}'.format(a['Name'], b),
                'Incoming': incoming,
                'Options' : options,
            }
        result.append(translator)
    return result


def get_default_rules(a,b):
    result   = []
    b_global = False
    a_is_cc  = False

    if b['Note Type'] == 'cc':
        b_global = get_global_var(b['Desc'])
    if a['Note Type'] == 'cc':
        a_is_cc = True

    if b_global:
        if a_is_cc:
            result.append( '// set {}'.format(b['Desc']) )
            result.append( '{}=pp'.format(b_global) )
        else:
            result.append( '// toggle {} on and off'.format(b['Desc']) )
            result.append( 'if {}==0 then goto NEXT'.format(b_global) )
            result.append( '{}=0'.format(b_global) )
            result.append( 'goto END'.format(b_global) )
            result.append( 'label NEXT'.format(b_global) )
            result.append( '{}=127'.format(b_global) )
            result.append( 'label END'.format(b_global) )
    return result


def create_options_header(link, options):
    if type(link) is not dict:
        result = [ 'Actv01Stop00OutO00StMa{}'.format(to_hex(link, 8)) ]
    else:
        if 'Delay' in link:
            delay = 'Dlay{}:Millis'.format(link['Delay'])
        else:
            delay = ''

        num_rules = len(options)

        result = [ 'Actv{:02d}Stop{:02d}OutO{:02d}{}StMa{}'.format(
            1, 0, 0, delay, to_hex(num_rules, 8)
        ) ]

    result += options
    return result


if __name__ == '__main__':
    run()
