from ObjectContainer import ObjectContainer as oc
from objects import init_variables, get_new_global_var, n, get_global_var
from layout import endpoints, links
from nice_json import json_print_pretty


'''
Summary:
 - def run()
 - def get_body()
 - def get_endpoint(body, endpoint_name)
 - def create_globals(body)
 - def get_presets(body)
 - def create_preset(options, body=None)
 - def get_global_start_values()
 - def get_translators(body)
 - def create_options_header(link)
 - def to_hex(num, padding=0)
'''


def run():
    init_variables()
    body = get_body()
    create_globals(body)

    presets = get_presets(body)
    print(json_print_pretty(presets))



################################################################################



def get_body():
    body = { 'Endpoints': endpoints, 'Links': links }
    return body


def get_endpoint(body, endpoint_name):
    endpoints = body['Endpoints']
    try:
        return (e for e in endpoints if e['Name'] == endpoint_name).next()
    except:
        raise Exception('Value \"{}\" does not exist!..'.format(endpoint_name))


def create_globals(body):
    for value in body['Endpoints']:
        if 'Outgoing' in value and \
           'Note Type' in value['Outgoing'] and \
           value['Outgoing']['Note Type'] == 'cc':
            get_new_global_var(value['Name'])


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
            'Translators': [ get_global_start_values() ]
        }
    elif options == 'links':
        # create linking preset
        result = {
            'Name'   : 'Links',
            'Active' : 1,
            'Psi'    : 0,
            'Translators': [ get_translators(body) ]
        }

    return result


def get_global_start_values():
    global_vars = oc._get('global_vars')

    taken_global_vars = [(g for g in global_vars if g['Taken']).next()]

    rules = []
    for g in taken_global_vars:
        rules.append('// {}'.format(g['Taken']))
        rules.append('{}={}'.format(g['Var'], g['Value']))

    options = [ create_options_header(len(rules)) ]
    options += rules

    translator = {
        'Name'    : 'Links',
        'Options' : options,
    }
    return translator


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

        options = [ create_options_header(link) ]
        options += rules

        try:
            b = get_endpoint(body, b)
            b_note = b['Incoming']['Note'] if b['Incoming']['Note'] != 'auto' else n(b['Incoming']['Channel'])

            outgoing = {
                'Desc'      : b['Name'],
                'Note'      : b_note,
                'Channel'   : b['Incoming']['Channel'],
                'Note Type' : b['Incoming']['Note Type'],
                'Ports'     : b['Ports']
            }

            translator = {
                'Name'    : '{} - {}'.format(a['Name'], b['Name']),
                'Incoming': incoming,
                'Outgoing': outgoing,
                'Options' : options,
            }
        except:
            translator = {
                'Name'    : '{} - {}'.format(a['Name'], b['Name']),
                'Incoming': incoming,
                'Options' : options,
            }
        result.append(translator)
    return result


def create_options_header(link):
    if type(link) is not dict:
        return 'Activ01Stop01OutO01StMa{}'.format(to_hex(link, 8))
    else:
        if 'Delay' in link:
            delay = 'Dlay{}:Millis'.format(link['Delay'])
        else:
            delay = ''

        num_rules = len(link['Options'])

        return 'Activ{:02d}Stop{:02d}OutO{:02d}{}StMa{}'.format(
            1, 0, 0, delay, to_hex(num_rules, 8)
        )


def to_hex(num, padding=0):
    result = str(hex(num))[2:]
    if padding > 0:
        itr = padding - len(result)
        for i in range(itr):
            result = '0' + result
    return result


if __name__ == '__main__':
    run()
