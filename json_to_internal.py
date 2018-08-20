from global_vars import GlobalVars as gv
from global_vars import get_body



# incoming options besides midi
PROCESSING_ENABLED     = 'EnDi01'
PROCESSING_DISABLED    = 'EnDi00'
PROJECT_FILE_OPENED    = 'EnDi02'
CUR_PRESET_ACTIVATED   = 'Pres080000'  # when current preset is activated
CUR_PRESET_DEACTIVATED = 'Pres090000'  # when current preset is deactivated
def ACTIVATE_ONLY_BY_NAME(name):            # activate preset by name
    return 'Pres02{}{}'.format(to_hex(len(name),4),name)
def ACTIVATE_BY_TIMER(name):
    return 'Tim0TimT{}{}'.format(to_hex(len(name),4),name)

incoming_options = [
    PROCESSING_ENABLED,
    PROCESSING_DISABLED,
    PROJECT_FILE_OPENED,
    CUR_PRESET_ACTIVATED,
    CUR_PRESET_DEACTIVATED,
    'Pres02',
    'Tim0TimT'
]

'''
Name#=Translator Name
Incoming#=<incoming info>
Outgoing#=<outgoing info>
Options#=<translator rules>

translator = {
    'Incoming'  : {
        'Type'     : 'note',
        'Name'     : 'hb_mitch_vol',
        'Note Type': 'cc',
        'Channel'  : 3,
        'Note'     : 20,
        'Value'    : 'g3',
        'Ports'    : [p3]
    },
    'Outgoing'  : {
        'Type'     : 'note',
        'Name'     : 'daw_mitch_vol',
        'Note Type': 'cc',
        'Channel'  : 2,
        'Note'     : 20,
        'Value'    : 'g7',
        'Ports'    : [p2]
    },
    'Options'   : [
        'g3=pp',
        'g7=pp',
    ],
    'Trans_Type' : 'thru'
}

'''


class Translator:
    THRU      = 'thru'
    TOGGLE    = 'toggle'
    SET_RULES = 'set_rules'
    BI_DIR    = 'bi_dir'

    def __init__(self, settings):
        self.name     = ''
        self.incoming = ''
        self.outgoing = ''
        self.options  = ''
        self.compile(settings)

    def compile(self, settings):
        ttype = settings['Trans_Type']

        if   ttype == Translator.THRU:
            self.incoming += 'Incoming{}='

        elif ttype == Translator.TOGGLE:
        elif ttype == Translator.SET_RULES:
        elif ttype == Translator.BI_DIR:
            # set two translators

    def set_incoming():
        result  = 'MID3'
        result += '<Incoming Action=\'MIDI\'>'
        result += '<Description>{0}</Description>'
        result += '<Ports>{1}</Ports>'
        result += '<Simple Type=\'{2}\'>{}</Simple>'
        result += '<Channel num=\'{3}\'/>'
        result += '<Value1 {4}=\'{5}\'/>'
        result += '<Value2 {6}=\'{7}\' {8}/>'
        result += '</Incoming>'

        options = []
        options.append( Type1 )
        options.append( '{} -> {}'.format(Name1, Name2) )

        ports = ''
        for p in Ports1: ports += '<Port>{}</Port>'.format(p)
        options.append(ports)

        if   note_type1 == 'note': options.append('NoteOn')
        elif note_type1 == 'cc': options.append('ControlChange')

        options.append(Channel1)

        if type(Note1) is str: options.append('var')
        else: options.append('num')
        options.append(Note1)

        if   note_type1 == 'note': 
            options.append('num')
            options.append('0x00')
            options.append('Type=\'Any\'')
        elif note_type1 == 'cc':
            options.append('var')
            options.append('pp')
            options.append('')



    def get_endpoint(self, name):
        body = get_body()

        # get rid of any empty names
        if not name: return name

        # first check in endpoint list
        for e in body['Endpoints']:
            if e['Name'] == name:
                return e

        # then check other input types
        for p in incoming_options:
            if p in name:
                return p

        raise Exception('Endpoint {} doesnt exist!'.format(name))



class Preset:
    def __init__(self, name='default', active=1, psi=0):
        self._name        = name
        self._active      = active
        self._psi         = psi
        self._translators = []

    def new_translator(
        self, name, in_type, in_settings,
        out_type, out_settings
    ):
        new_t = Translator(
            name = name
        )
        translator = {
            'Name': name,
            'Incoming': self._generate_incoming(),
            'Outgoing': self._generate_outgoing(),
            'Options' : self._generate_options()
        }

    def _generate_incoming(self):
        pass

    def _generate_outgoing(self):
        pass

    def _generate_options(self):
        pass


def to_hex(num, padding=0, keep_x=False):
    result = str(hex(num))[2:].upper()
    if padding > 0:
        itr = padding - len(result)
        if itr > 0:
            for i in range(itr):
                result = '0' + result
    if keep_x: result = '0x{}'.format(result)
    return result
