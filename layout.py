from objects import n, e, l
from super_secret_footer import footer_signature, footer_signed_by



# standard ports #
p1 = 'Scarlett 18i20 USB'
p2 = 'Bome Virtual Port 1'
p3 = 'TouchOSC Bridge'



# ENDPOINTS ####################################################################
endpoints = [
    # Name,                    Ports,   Chan, Note Type, Note Incoming, Note Outgoing

    # fcb1010 :00 #
    e('fcb1010_btn_1',         [p1,p2], 1,    'note',         1),
    e('fcb1010_btn_2',         [p1,p2], 1,    'note',         2),
    e('fcb1010_btn_3',         [p1,p2], 1,    'note',         3),
    e('fcb1010_btn_4',         [p1,p2], 1,    'note',         4),
    e('fcb1010_btn_5',         [p1,p2], 1,    'note',         5),
    e('fcb1010_btn_6',         [p1,p2], 1,    'note',         6),
    e('fcb1010_btn_7',         [p1,p2], 1,    'note',         7),
    e('fcb1010_btn_8',         [p1,p2], 1,    'note',         8),
    e('fcb1010_btn_9',         [p1,p2], 1,    'note',         9),
    e('fcb1010_btn_10',        [p1,p2], 1,    'note',        10),
    # fcb1010 :01 #
    e('fcb1010_btn_11',        [p1,p2], 1,    'note',        11),
    e('fcb1010_btn_12',        [p1,p2], 1,    'note',        12),
    e('fcb1010_btn_13',        [p1,p2], 1,    'note',        13),
    e('fcb1010_btn_14',        [p1,p2], 1,    'note',        14),
    e('fcb1010_btn_15',        [p1,p2], 1,    'note',        15),
    e('fcb1010_btn_16',        [p1,p2], 1,    'note',        16),
    e('fcb1010_btn_17',        [p1,p2], 1,    'note',        17),
    e('fcb1010_btn_18',        [p1,p2], 1,    'note',        18),
    e('fcb1010_btn_19',        [p1,p2], 1,    'note',        19),
    e('fcb1010_btn_20',        [p1,p2], 1,    'note',        20),
    # fcb1010 expression #
    e('fcb1010_exp_1',         [p1,p2], 1,    'note',       126),
    e('fcb1010_exp_2',         [p1,p2], 1,    'note',       127),

    # bass effect I/O's #
    e('fx_lowcut',             [p2],    2,    'cc',       'none',       'auto'),
    e('fx_hicut',              [p2],    2,    'cc',       'none',       'auto'),
    e('fx_dist',               [p2],    2,    'cc',       'none',       'auto'),
    e('fx_delay',              [p2],    2,    'cc',       'none',       'auto'),
    e('fx_reverb',             [p2],    2,    'cc',       'none',       'auto'),
    e('fx_volume',             [p2],    2,    'cc',       'none',       'auto'),
    e('fx_exp',                [p2],    2,    'cc',       'none',       'auto'),

    # daw I/O's #
    e('daw_stop_playhead',     [p2],    2,    'note',     'none',       'auto'),
    e('daw_stop_clips',        [p2],    2,    'note',     'none',       'auto'),
    e('daw_advance_playhead',  [p2],    2,    'note',     'none',       'auto'),
    e('daw_play',              [p2],    2,    'note',     'none',       'auto'),
    e('daw_record',            [p2],    2,    'note',     'none',       'auto'),
    e('daw_talkback',          [p2],    2,    'cc',       'none',       'auto'),
    e('daw_start_drums',       [p2],    2,    'note',     'none',       'auto'),
    e('daw_start_trans_drums', [p2],    2,    'note',     'none',       'auto'),
    e('daw_start_metron',      [p2],    2,    'note',     'none',       'auto'),

    # hipbox I/O's #
    e('mitch_hb_talkback',     [p2,p3], 3,    'cc',            1,            1),
    e('mitch_hb_vol',          [p2,p3], 3,    'cc',            1,            1),
]



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
    # fcb1010 :01 #
    l('fcb1010_btn_11',     'fx_lowcut'),
    l('fcb1010_btn_12',     'fx_hicut'),
    l('fcb1010_btn_13',     'fx_dist'),
    l('fcb1010_btn_14',     'fx_delay'),
    l('fcb1010_btn_15',     'fx_reverb'),
    l('fcb1010_btn_16',     'daw_talkback'),
    l('fcb1010_btn_17',     'daw_start_drums'),
    l('fcb1010_btn_18',     'daw_start_trans_drums'),
    l('fcb1010_btn_19',     'daw_start_metron'),
    l('fcb1010_btn_20',     'daw_stop_playhead'),
    l('fcb1010_btn_20',     'daw_stop_clips'),
    l('fcb1010_btn_20',     'daw_advance_playhead'),
    # fcb1010 expression #
    l('fcb1010_exp_1',      'fx_volume'),
    l('fcb1010_exp_2',      'fx_exp'),


]
################################################################################



# GLOBAL VARIABLES #############################################################
global_variables = [
    ('current_song', 0),
    ('blind',        0),
    ('old_pete',     1),
    ('sono',         2),
    ('petrichor',    3),
    ('space',        4),
]
################################################################################



# hipbox I/O's #
# bandmates = 'mitch james jesse'.split()
# for i, bm in enumerate(bandmates):
#     endpoints.append(
#     {'Name': '{}_hb_talkback'.format(bm),
#         'Incoming': {'Note': 'auto',     'Channel': i+3, 'Note Type': 'cc'},
#         'Outgoing': {'Note': 'incoming', 'Channel': i+3, 'Note Type': 'cc'},
#         'Ports': p2+p3})
#     endpoints.append(
#     {'Name': '{}_hb_solo'.format(bm),
#         'Incoming': {'Note': 'auto',     'Channel': i+3, 'Note Type': 'cc'},
#         'Outgoing': {'Note': 'incoming', 'Channel': i+3, 'Note Type': 'cc'},
#         'Ports': p3})
#     endpoints.append(
#     {'Name': '{}_hb_hp_vol'.format(bm),
#         'Incoming': {'Note': 'auto',     'Channel': i+3, 'Note Type': 'cc'},
#         'Outgoing': {'Note': 'incoming', 'Channel': i+3, 'Note Type': 'cc'},
#         'Ports': p3})
#     endpoints.append(
#     {'Name': '{}_hb_mitch_vol'.format(bm),
#         'Incoming': {'Note': 'auto',     'Channel': i+3, 'Note Type': 'cc'},
#         'Outgoing': {'Note': 'incoming', 'Channel': i+3, 'Note Type': 'cc'},
#         'Ports': p3})
#     endpoints.append(
#     {'Name': '{}_hb_james_vol'.format(bm),
#         'Incoming': {'Note': 'auto',     'Channel': i+3, 'Note Type': 'cc'},
#         'Outgoing': {'Note': 'incoming', 'Channel': i+3, 'Note Type': 'cc'},
#         'Ports': p3})
#     endpoints.append(
#     {'Name': '{}_hb_jesse_vol'.format(bm),
#         'Incoming': {'Note': 'auto',     'Channel': i+3, 'Note Type': 'cc'},
#         'Outgoing': {'Note': 'incoming', 'Channel': i+3, 'Note Type': 'cc'},
#         'Ports': p3})
#     endpoints.append(
#     {'Name': '{}_hb_metron_vol'.format(bm),
#         'Incoming': {'Note': 'auto',     'Channel': i+3, 'Note Type': 'cc'},
#         'Outgoing': {'Note': 'incoming', 'Channel': i+3, 'Note Type': 'cc'},
#         'Ports': p3})
#     endpoints.append(
#     {'Name': '{}_hb_drums_vol'.format(bm),
#         'Incoming': {'Note': 'auto',     'Channel': i+3, 'Note Type': 'cc'},
#         'Outgoing': {'Note': 'incoming', 'Channel': i+3, 'Note Type': 'cc'},
#         'Ports': p3})
#     endpoints.append(
#     {'Name': '{}_hb_talkback_vol'.format(bm),
#         'Incoming': {'Note': 'auto',     'Channel': i+3, 'Note Type': 'cc'},
#         'Outgoing': {'Note': 'incoming', 'Channel': i+3, 'Note Type': 'cc'},
#         'Ports': p3})

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
