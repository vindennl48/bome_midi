from objects import n, e, l, X
from super_secret_footer import footer_signature, footer_signed_by


# VARS #########################################################################
# standard ports #
p1 = 'Scarlett 18i20 USB'
p2 = 'Bome Virtual Port 1'
p3 = 'TouchOSC Bridge'

# band mates #
bandmates  = 'mitch james jesse'.split()
################################################################################


# LINKS ########################################################################
links = [
    # Name1,                Name2,                   Options

    # fcb1010 :00 #
    l('fcb1010_btn_1',      'blind',                 ['current_song=blind']),
    l('fcb1010_btn_2',      'old_pete',              ['current_song=old_pete']),
    l('fcb1010_btn_3',      'sono',                  ['current_song=sono']),
    l('fcb1010_btn_4',      'petrichor',             ['current_song=petrichor']),
    l('fcb1010_btn_5',      'space',                 ['current_song=space']),
    l('fcb1010_btn_6',      'daw_talkback'),
    l('fcb1010_btn_10',     'daw_stop_playhead'),
    l('fcb1010_btn_10',     'daw_stop_clips',        delay=50),
    l('fcb1010_btn_10',     'daw_advance_playhead',  delay=100),
    # fcb1010 :01 #
    l('fcb1010_btn_11',     'fx_lowcut'),
    l('fcb1010_btn_12',     'fx_hicut'),
    l('fcb1010_btn_13',     'fx_dist'),
    l('fcb1010_btn_14',     'fx_delay'),
    l('fcb1010_btn_15',     'fx_reverb'),
    l('fcb1010_btn_16',     'daw_talkback'),
    l('fcb1010_btn_17',     'daw_start_drums'),
    l('fcb1010_btn_18',     'daw_start_trans_drums'),
    l('fcb1010_btn_19',     'daw_start_click'),
    l('fcb1010_btn_20',     'daw_stop_playhead'),
    l('fcb1010_btn_20',     'daw_stop_clips',        delay=50),
    l('fcb1010_btn_20',     'daw_advance_playhead',  delay=100),
    # fcb1010 expression #
    l('fcb1010_exp_1',      'fx_volume'),
    l('fcb1010_exp_2',      'fx_exp'),

    # hipbox links are in the hipbox section
]
################################################################################


# ENDPOINTS ####################################################################
endpoints = []


# fcb1010 footpedal I/O's #
#                    Name,                         Ports,   Chan, Note Type, Note Incoming, Note Outgoing, Default Val
for i in range(20):
    endpoints += [ e('fcb1010_btn_{}'.format(i+1), [p1,p2], 1,    'note',    i+1) ]
for i in range(2):
    endpoints += [ e('fcb1010_exp_{}'.format(i+1), [p1,p2], 1,    'cc',      i+126) ]


# bass effect I/O's #
bass_fx_off = 'lowcut dist delay reverb volume exp'.split()
bass_fx_on  = 'hicut'.split()
#                    Name,                         Ports,   Chan, Note Type, Note Incoming, Note Outgoing, Default Val
for bf in bass_fx_off:
    endpoints += [ e('fx_{}'.format(bf),           [p2],    2,    'cc',      'none',        'auto') ]
for bf in bass_fx_on:
    endpoints += [ e('fx_{}'.format(bf),           [p2],    2,    'cc',      'none',        'auto',        127) ]


# daw I/O's #
daw_io_notes = 'stop_playhead stop_clips advance_playhead play record start_drums start_trans_drums start_click'.split()
daw_io_cc    = 'talkback'.split()
#                    Name,                         Ports,   Chan, Note Type, Note Incoming, Note Outgoing, Default Val
for din in daw_io_notes:
    endpoints += [ e('daw_{}'.format(din),         [p2],    2,    'note',    'none',        'auto') ]
for dic in daw_io_cc:
    endpoints += [ e('daw_{}'.format(dic),         [p2],    2,    'cc',      'none',        'auto') ]
################################################################################


# HIPBOX #######################################################################
# hipbox I/O's and Links #
hb_options = bandmates + 'drums vol click tbvol solo'.split()
for i, hbo in enumerate(hb_options):
    for j, bm in enumerate(bandmates):
        if hbo != 'tbio' or hbo != 'rec':
            endpoints += [ 
                e('hb_{}_{}'.format(bm,hbo),  [p3], j+3, 'cc', i+1, i+1, 89),
                e('daw_{}_{}'.format(bm,hbo), [p2], j+3, 'cc', i+1, i+1, 89) ]
            links += l('hb_{}_{}'.format(bm,hbo), 'daw_{}_{}'.format(bm,hbo), thru=X)
        else:
            endpoints += [ 
                e('hb_{}_{}'.format(bm,hbo),  [p3], j+3, 'cc', i+1, i+1, 0) ]
            if   hbo == 'tbio':
                links += l('hb_{}_{}'.format(bm,hbo), 'daw_talkback', thru=X)
            elif hbo == 'rec':
                links += [ l('hb_{}_{}'.format(bm,hbo), 'daw_record') ]
################################################################################


# GLOBAL VARIABLES #############################################################
global_variables = [
    ('update_freq',  2000),
    ('current_song', 0),
    ('blind',        0),
    ('old_pete',     1),
    ('sono',         2),
    ('petrichor',    3),
    ('space',        4),
]
################################################################################


# FOOTER #######################################################################
footer = [
    "[Project]",
    "Version=2",
    "Author=",
    "AuthorContact=",
    "Comments=",
    "AuthorWWW=",
    "AuthorCopyright=",
    "DefaultInPorts=MIDA0000",
    "DefaultOutPorts=MIDA0000",
    "",
    "[Signatures]",
    "SigName-1=[Midi Translator Pro Internal]",
    footer_signature,   # this is where your signature and 
    footer_signed_by    #  signature key go to make sure you 
                        #  have a legal copy.
]
################################################################################
