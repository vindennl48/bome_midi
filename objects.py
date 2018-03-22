from ObjectContainer import ObjectContainer as oc
from nice_json import json_print_pretty


'''
Summary:
 - def init_variables()
 - def get_new_global_var(device, start_value=0)
 - def get_global_var(device)
 - def get_new_note(ch=1, note=-1) # device, note_type
 - def n(note=-1, ch=1)
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


# e()
def e(name, ports=[], channel=0, note_type='note', note_in='', note_out=''):
    result = {}
    result['Name'] = name
    if note_in != '' and note_in != 'none':
        result['Incoming'] = {'Note': note_in,  'Channel': channel, 'Note Type': note_type}
    if note_out != '' and note_out != 'none':
        result['Outgoing'] = {'Note': note_out, 'Channel': channel, 'Note Type': note_type}
    result['Ports'] = ports
    return result
# e()


# l()
def l(name1, name2='', options=[]):
    return { 'Link': (name1, name2), 'Options': options }
# l()
