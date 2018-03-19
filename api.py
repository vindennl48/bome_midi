from ObjectContainer import ObjectContainer as oc
from objects import init_variables, get_new_global_var, n, get_global_var

def get_body():
    endpoints = [
        # FCB1010
        {   "Name": "fcb1010_btn_1",
                "Incoming": { "Note": n(1,ch=1), "Channel": 1, "Note Type": "note" },
                "Ports": [ "Scarlett 18i20 USB", "Bome Midi Virtual Port 1" ]},

        # ABLETON
        {   "Name": "fx_dist",
                "Incoming": { "Note": n(ch=1), "Channel": 1, "Note Type": "cc" },
                "Outgoing": { "Note": n(ch=1), "Channel": 1, "Note Type": "cc" },
                "Ports": [ "Bome Midi Virtual Port 1" ]}
    ]

    links = [
        { "Link": ('fcb1010_btn_1',  'fx_dist') },
    ]

    body = { "Endpoints": endpoints, "Links": links }
    return body


def create_globals(body):
    for value in body['Endpoints']:
        if 'Outgoing' in value and \
           'Note Type' in value['Outgoing'] and \
           value['Outgoing']['Note Type'] == "cc":
            get_new_global_var(value['Name'])


def run_me():
    init_variables()
    body = get_body()
    create_globals(body)

    presets = get_presets(body)

    print(presets)


def get_presets(body):
    presets = [ create_preset('init') ]
    for l in body['Links']:
        presets.append( create_preset(l) )
    return presets



def create_preset(options):
    result = {}
    if options == 'init':
        # create initial preset
        result = {
            'Name'   : "Initialize",
            'Active' : 1,
            'Psi'    : 0,     # PresetSwitchIgnore
            'Translators': []
        }
    elif 'Link' in options:
        # create linking preset
        a = options['Link'][0]
        b = options['Link'][1]
        result = {
            'Name'   : "{} - {}".format(a,b),
            'Active' : 1,
            'Psi'    : 0,
            'Translators': []
        }

    return result


if __name__ == "__main__":
    run_me()
