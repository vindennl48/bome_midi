from ObjectContainer import ObjectContainer as oc
from nice_json import json_print_pretty

'''
Summary:
 - def init_variables()
 - def get_new_global_var(device, start_value=0)
 - def get_global_var(device)
 - def get_new_note(ch=1, note=-1) # device, note_type
 - def n(note=-1, ch=1)
 - def init_connections(body)
 - def get_details(name)
'''


# setup global vars
def init_variables():
    gvars = []
    notes = []

    for j in range(16):
        new_notes = []
        for i in range(1,128):
            new_notes.append(
                {
                    "Note" : 0 + i,
#                   "Type" : "control change",
                    "Taken": False     # or the name of the device using this note
#                   "Value": 0
                }
            )
        notes.append(new_notes)

    fl = "g h i j k l m n y z".split()
    sl = "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9".split()
    for c in fl:
        for c2 in sl:
            gvars.append(
                {
                    "Var" : "{}{}".format(c,c2),
                    "Taken": False, # or the name of the device using this variable
                    "Value": 0
                }
            )
    oc._add("global_vars", gvars)
    oc._add("notes", notes)
# setup global vars


# get an unused global var
def get_new_global_var(device, start_value=0):
    global_vars = oc._get("global_vars")
    for v in global_vars:
        if not v['Taken']:
            v['Taken'] = device
            v['Value'] = start_value
            return v['Var']
    raise Exception("Error retrieving global var")
# get an unused global var


# get global var given device name
def get_global_var(device):
    global_vars = oc._get("global_vars")
    g = (g for g in global_vars if g['Taken'] == device).next()
    return g['Var']
# get global var given device name


# get new note
def get_new_note(ch=1, note=-1): # device, note_type
    notes = oc._get("notes")
    if note == -1:
        for n in notes[ch]:
            if not n['Taken']:
                n['Taken'] = True # device
#               n['Type']  = note_type
                return n['Note']
    else:
        n = (n for n in notes[ch] if n['Note'] == note).next()
        if not n['Taken']:
            n['Taken'] = True
            return n['Note']
        else:
            raise Exception("Note \"{}\" already taken!".format(note))
    raise Exception("Error retrieving note")
# get new note


# n()
def n(note=-1, ch=1):
    if note != -1:
        result = get_new_note(note=note, ch=ch)
    else:
        result = get_new_note(ch=ch)
    return result
# n()


# init_connections
def init_connections(body):
    outputs  = body['Outputs']
    inputs   = body['Inputs']
    events   = body['Events']

    keys = inputs.keys()
    for name in keys:

        btn       = inputs[name]
        if btn['To'] in outputs:
            out       = outputs[btn['To']]

            note_in   = btn['Note']
            type_in   = btn['Type']
            ch_in     = btn['Channel']
            ports_in  = btn['Ports']

            note_out  = out['Note']
            type_out  = out['Type']
            ch_out    = out['Channel']
            ports_out = out['Ports']

            c = oc._add(
                btn['To'],
                {
                    "Name"      : btn['To'],
                    "Note_In"   : note_in,
                    "Type_In"   : type_in,
                    "Ch_In"     : ch_in,
                    "Ports_In"  : ports_in,

                    "Note_Out"  : note_out,
                    "Type_Out"  : type_out,
                    "Ch Out"    : ch_out,
                    "Ports_Out" : ports_out,
                    "gvar"      : get_new_global_var(name, out['Start Val']) if \
                                type_out == "cc" else ""
                }
            )
        elif btn['To'] in events:
            out        = events[btn['To']]

            note_in    = btn['Note']
            type_in    = btn['Type']
            ch_in      = btn['Channel']
            ports_in   = btn['Ports']

            event_list = out['Output']

            c = oc._add(
                btn['To'],
                {
                    "Name"      : btn['To'],
                    "Note_In"   : note_in,
                    "Type_In"   : type_in,
                    "Ch_In"     : ch_in,
                    "Ports_In"  : ports_in,

                    "Event_List": event_list,
                }
            )

        print(c)
# init_connections


# get_details
def get_details(name):
    return oc._get(name)
# get_details


## # set new note
## def set_new_note(device, note, note_type):
##     notes = oc._get("notes")
##     n = (n for n in notes if n['Note'] == note).next()
##     n['Taken'] = device
##     n['Type']  = note_type
##     return n
## # set new note
## 
## # init_midi_device
## def init_midi_device(midi_devices):
##     for md in midi_devices:
##         device = {
##             "Type"     : md['Type'],
##             "Channel"  : md['Channel'],
##             "Ports"    : md['Ports'],
##             "Toggles"  : init_toggles(md['Toggles']),
##             "Buttons"  : init_buttons(md['Buttons']),
##             "Sliders"  : init_sliders(md['Sliders'])
##         }
##         oc._add(md['Name'], device)
## # init_midi_device
## 
## # init_daw
## def init_daw(daws):
##     for d in daws:
##         new_daw = {
##             "Channel"  : d['Channel'],
##             "Ports"    : d['Ports'],
##             "Toggles"  : init_toggles(d['Toggles']),
##             "Buttons"  : init_buttons(d['Buttons']),
##             "Sliders"  : init_sliders(d['Sliders'])
##         }
##         oc._add(d['Name'], new_daw)
## # init_daw
##
## # init_toggles
## def init_toggles(toggles):
##     result = {}
##     keys = toggles.keys()
##     for name in keys:
##         note = toggles[name]
##         if note != "auto":
##             result[name] = set_new_note(name, note, "control change")
##         else:
##             result[name] = get_new_note(name, "control change")
##         oc._add(name, result[name])
##     return result
## # init_toggles
## 
## # init_buttons
## def init_buttons(buttons):
##     result = {}
##     keys = buttons.keys()
##     for name in keys:
##         note = buttons[name]
##         if note != "auto":
##             result[name] = set_new_note(name, note, "note on")
##         else:
##             result[name] = get_new_note(name, "note on")
##         oc._add(name, result[name])
##     return result
## # init_buttons
## 
## # init_sliders
## def init_sliders(sliders):
##     result = {}
##     keys = sliders.keys()
##     for name in keys:
##         note = sliders[name]
##         if note != "auto":
##             result[name] = set_new_note(name, note, "control change")
##         else:
##             result[name] = get_new_note(name, "control change")
##         oc._add(name, result[name])
##     return result
## # init_sliders
