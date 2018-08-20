from ObjectContainer import ObjectContainer

class GlobalVars(ObjectContainer):
    def __init__(self, body):
        self.init_vars()
        self.init_notes()
        self.set_body(body)

    def set_body(self, body):
        GlobalVars._add('body', body)

    def init_notes(self):
        notes = []
        for j in range(16):
            new_notes = []
            for i in range(1,128):
                new_notes.append(
                    {
                        'Note' : 0 + i,
                        #'Type' : 'control change',
                        'Taken': False     # or the name of the device using this note
                        #'Value': 0
                    }
                )
            notes.append(new_notes)
        GlobalVars._add('notes', notes)

    def init_vars(self):
        gvars = []
        fl = 'g h i j k l m n y z'.split()
        sl = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'.split()
        for c in fl:
            for c2 in sl:
                if c != 'i' and c2 != 'f':
                    gvars.append(
                        {
                            'Var' : '{}{}'.format(c,c2),
                            'Taken': False, # or the name of the device using this variable
                            'Value': 0
                        }
                    )
        GlobalVars._add('global_vars', gvars)

    def get_var_list(self):
        return GlobalVars._get('global_vars')

    def get_note_list(self):
        return GlobalVars._get('notes')

    def get_new_var(self, device, start_value=0):
        global_vars = self.get_var_list()
        for v in global_vars:
            if not v['Taken']:
                v['Taken'] = device
                v['Value'] = start_value
                return v['Var']
        raise Exception('No More Global Vars Are Left!')

    def get_var_name(self, device):
        global_vars = self.get_var_list()
        g = (g for g in global_vars if g['Taken'] == device).next()
        return g['Var']

    def get_var_value(self, device):
        global_vars = self.get_var_list()
        g = (g for g in global_vars if g['Taken'] == device).next()
        return g['Value']

    def get_new_note(self, note=-1, ch=1):
        notes = self.get_note_list()
        if note == -1:
            for n in notes[ch]:
                if not n['Taken']:
                    n['Taken'] = True # device
                    #n['Type']  = note_type
                    return n['Note']
        else:
            n = (n for n in notes[ch] if n['Note'] == note).next()
            if not n['Taken']:
                n['Taken'] = True
                return n['Note']
            else:
                raise Exception('Note \'{}\' already taken!'.format(note))
        raise Exception('Error retrieving note')

gv = GlobalVars()

def n(note=-1, ch=1):
    global gv
    if note != -1:
        result = gv.get_new_note(note=note, ch=ch)
    else:
        result = gv.get_new_note(ch=ch)
    return result

def e(name, ports=[], channel=0, note_type='note', note_in='', note_out='', default=''):
    result = {}
    result['Name']  = name
    result['Ports'] = ports

    if note_in and note_in != 'none':
        result['Incoming'] = {'Note': note_in,  'Channel': channel, 'Note Type': note_type}

    if  note_out and note_out != 'none':
        result['Outgoing'] = {'Note': note_out, 'Channel': channel, 'Note Type': note_type}

    if default and default != 'none':
        result['Default']  = default

    return result

def get_body():
    return GlobalVars._get('body')
