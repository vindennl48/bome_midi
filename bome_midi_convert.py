from layout import footer
from ObjectContainer import ObjectContainer as oc


'''
Summary:
 - def get_bome_midi(presets)
 - def get_incoming(t)
 - def get_outgoing(t)
 - def get_options(t)
 - def get_comment(o)
 - def get_if(o)
 - def get_label(o)
 - def get_goto(o)
 - def to_hex(num, padding=0, keep_x=False)
'''


# incoming options besides midi
PROCESSING_ENABLED     = 'EnDi01'
PROCESSING_DISABLED    = 'EnDi00'
PROJECT_FILE_OPENED    = 'EnDi02'
CUR_PRESET_ACTIVATED   = 'Pres080000'  # when current preset is activated
CUR_PRESET_DEACTIVATED = 'Pres090000'  # when current preset is deactivated
def ACTIVATE_ONLY_BY_NAME(name):            # activate preset by name
    return 'Pres02{}{}'.format(to_hex(len(name),4),name)


def get_bome_midi(presets):
    result = []

    preset_num = 0
    for p in presets:
        result.append( '[Preset.{}]'.format(preset_num) )
        result.append( 'Name={}'.format(p['Name']) )
        result.append( 'Active={}'.format(p['Active']) )
        result.append( 'PresetSwitchIgnore={}'.format(p['Psi']) )

        t_num = 0
        for t in p['Translators']:
            result.append( 'Name{}={}'.format(t_num, t['Name']) )
            result.append( 'Incoming{}={}'.format(t_num, get_incoming(t)) )
            result.append( 'Outgoing{}={}'.format(t_num, get_outgoing(t)) )
            result.append( 'Options{}={}'.format(t_num, get_options(t)) )
            t_num += 1          # T_NUM

        preset_num += 1         # PRESET_NUM
        result.append( '' )     # newline

    result += footer

    return result


def get_incoming(t):
    if 'Incoming' in t:
        i = t['Incoming']

        if 'Type' in i: return i['Type']

        result = [ 'MID3<Incoming Action="MIDI">' ]

        result.append( '<Description>{}</Description>'.format(i['Desc']) )

        result.append( '<Ports>' )
        for p in i['Ports']:
            result.append( '<Port>{}</Port>'.format(p) )
        result.append( '</Ports>' )

        if i['Note Type'] == "note":
            result.append( '<Simple Type="NoteOn">' )
        elif i['Note Type'] == "cc":
            result.append( '<Simple Type="ControlChange">' )

        result.append( '<Channel num="{}"/>'.format(i['Channel']-1) )
        result.append( '<Value1 num="{}"/>'.format(to_hex(i['Note'],2,True)) )
        result.append( '<Value2 num="{}" Type="Any"/>'.format(to_hex(0,2,True)) )
        result.append( '</Simple>' )

        result.append( '</Incoming>' )

        return ''.join(result)

    else:
        return 'None'


def get_outgoing(t):
    if 'Outgoing' in t:
        i = t['Outgoing']

        if 'Type' in i: return i['Type']

        result = [ 'MID3<Outgoing Action="MIDI">' ]

        result.append( '<Description>{}</Description>'.format(i['Desc']) )

        result.append( '<Ports>' )
        for p in i['Ports']:
            result.append( '<Port>{}</Port>'.format(p) )
        result.append( '</Ports>' )

        if i['Note Type'] == "note":
            result.append( '<Simple Type="NoteOn">' )
        elif i['Note Type'] == "cc":
            result.append( '<Simple Type="ControlChange">' )

        result.append( '<Channel num="{}"/>'.format(i['Channel']-1) )
        result.append( '<Value1 num="{}"/>'.format(to_hex(i['Note'],2,True)) )

        if i['Note Type'] == "note":
            result.append( '<Value2 num="{}"/>'.format(to_hex(127,2,True)) )
        elif i['Note Type'] == "cc":
            result.append( '<Value2 var="{}"/>'.format(i['Note Value']) )

        result.append( '</Simple>' )

        result.append( '</Outgoing>' )

        return ''.join(result)

    else:
        return 'None'


def get_options(t):
    result = []

    for i, o in enumerate(t['Options']):
        if i == 0:
            result.append( o )
            continue

        elif o[:2] == '//':
            # comment
            result.append( get_comment(o) )

        elif o[:2] == 'if':
            result.append( get_if(o) )

        elif o[:5] == 'label':
            result.append( get_label(o) )

        elif o[:4] == 'goto':
            result.append( get_goto(o) )

        elif '=' in o:
            result.append( get_equation(o) )

        else:
            result.append( o )

    return ''.join(result)


import re
def get_equation(o):
    global_vars = oc.items['global_vars']
    for gv in global_vars:
        if type(gv['Taken']) is str and gv['Taken'] in o:
            o = re.sub(gv['Taken'],gv['Var'],o)
    return o


def get_comment(o):
    return 'label{}__cmt>{}'.format(to_hex(len(o)+6,4), o)


def get_if(o):
    o = o.split()

    if o[3] == 'goto':
        rest = 'goto{}{}'.format( to_hex(len(o[4]),4), o[4])
    return 'if({}){}'.format(o[1], rest)


def get_label(o):
    o = o.split()
    return 'label{}{}'.format(to_hex(len(o[1]),4), o[1])


def get_goto(o):
    o = o.split()
    return 'goto{}{}'.format(to_hex(len(o[1]),4), o[1])


def to_hex(num, padding=0, keep_x=False):
    result = str(hex(num))[2:]
    if padding > 0:
        itr = padding - len(result)
        if itr > 0:
            for i in range(itr):
                result = '0' + result
    if keep_x: result = '0x{}'.format(result)
    return result


