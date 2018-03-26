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
    l('fcb1010_btn_10',     'daw_stop_playhead', [
        'hb_mitch_rec=0',
        'hb_james_rec=0',
        'hb_jesse_rec=0',
        'is_playing=0',
    ]),
    l('fcb1010_btn_10',     'daw_stop_clips',        delay=50),
    l('fcb1010_btn_10',     'daw_advance_playhead',  delay=100),
    # fcb1010 :01 #
    l('fcb1010_btn_11',     'fx_lowcut'),
    l('fcb1010_btn_12',     'fx_hicut'),
    l('fcb1010_btn_13',     'fx_dist'),
    l('fcb1010_btn_14',     'fx_delay'),
    l('fcb1010_btn_15',     'fx_reverb'),
    l('fcb1010_btn_16',     'daw_talkback'),
    # fcb1010_btn_17,18,19 in # songs # section
    l('fcb1010_btn_17',     '', [ 'is_playing=1' ]),
    l('fcb1010_btn_18',     '', [ 'is_playing=1' ]),
    l('fcb1010_btn_19',     '', [ 'is_playing=1' ]),
    # fcb1010_btn_17,18,19 in # songs # section
    l('fcb1010_btn_20',     'daw_stop_playhead', [
        'hb_mitch_rec=0',
        'hb_james_rec=0',
        'hb_jesse_rec=0',
        'is_playing=0',
    ]),
    l('fcb1010_btn_20',     'daw_stop_clips',        delay=50),
    l('fcb1010_btn_20',     'daw_advance_playhead',  delay=100),
    # fcb1010 expression #
    l('fcb1010_exp_1',      'fx_volume'),
    l('fcb1010_exp_2',      'fx_exp')
]

# hipbox links #
links += l('hb_mitch_mitch',     'daw_mitch_mitch',       thru=X)
links += l('hb_mitch_james',     'daw_mitch_james',       thru=X)
links += l('hb_mitch_jesse',     'daw_mitch_jesse',       thru=X)
links += l('hb_mitch_drums',     'daw_mitch_drums',       thru=X)
links += l('hb_mitch_vol',       'daw_mitch_vol',         thru=X)
links += l('hb_mitch_click',     'daw_mitch_click',       thru=X)
links += l('hb_mitch_tbvol',     'daw_mitch_tbvol',       thru=X)
links += l('hb_mitch_tbio',      'daw_talkback',          thru=X, options=[
    'hb_james_tbio=pp',
    'hb_jesse_tbio=pp',
])
links += l('hb_mitch_james_lrc', 'daw_mitch_james_lrc',   thru=X)
links += l('hb_mitch_jesse_lrc', 'daw_mitch_jesse_lrc',   thru=X)
links += l('hb_mitch_mitch_lrc', 'daw_mitch_mitch_lrc',   thru=X)
links += l('hb_bass_out',        'daw_bass_out',          thru=X)
links += l('hb_drums_out',       'daw_drums_out',         thru=X)
links += l('hb_level_james',     'daw_level_james',       thru=X)
links += l('hb_level_jesse',     'daw_level_jesse',       thru=X)
links += l('hb_level_in_mitch',  'daw_level_in_mitch',    thru=X)
links += l('hb_level_out_mitch', 'daw_level_out_mitch',   thru=X)
links += l('hb_amp',             'fx_amp',                thru=X)
links += l('hb_s_delay_beat',    'fx_s_delay_beat',       thru=X)
links += l('hb_s_delay_fdbk',    'fx_s_delay_fdbk',       thru=X)
links += l('hb_s_delay_drywet',  'fx_s_delay_drywet',     thru=X)
links += [ l('hb_mitch_rec',     'daw_advance_playhead', options=[
    'if is_playing==0 then goto END',
    'exit, skip',
    'label END'
] ) ]
links += [ l('hb_mitch_rec',     'daw_play', delay=200 , options=[
    'if is_playing==0 then goto END',
    'exit, skip',
    'label END',
    'is_playing=1'
] ) ]
links += [ l('hb_mitch_rec',     'daw_record', delay=1200, options=[
    'hb_mitch_rec=pp',
    'hb_james_rec=pp',
    'hb_jesse_rec=pp'
] ) ]
links += [ l('hb_mitch_tuner', 'daw_select_tuner', options=[
    'if pp==127 then goto END',
    'exit, skip',
    'label END'
] ) ]
links += [ l('hb_mitch_tuner', 'daw_select_mitch', options=[
    'if pp==0 then goto END',
    'exit, skip',
    'label END'
] ) ]

links += l('hb_james_mitch',     'daw_james_mitch',       thru=X)
links += l('hb_james_james',     'daw_james_james',       thru=X)
links += l('hb_james_jesse',     'daw_james_jesse',       thru=X)
links += l('hb_james_drums',     'daw_james_drums',       thru=X)
links += l('hb_james_vol',       'daw_james_vol',         thru=X)
links += l('hb_james_click',     'daw_james_click',       thru=X)
links += l('hb_james_tbvol',     'daw_james_tbvol',       thru=X)
links += l('hb_james_tbio',      'daw_talkback',          thru=X, options=[
    'hb_mitch_tbio=pp',
    'hb_jesse_tbio=pp',
])
links += l('hb_james_james_lrc', 'daw_james_james_lrc',   thru=X)
links += l('hb_james_jesse_lrc', 'daw_james_jesse_lrc',   thru=X)
links += l('hb_james_mitch_lrc', 'daw_james_mitch_lrc',   thru=X)
links += [ l('hb_james_rec',     'daw_advance_playhead', options=[
    'if is_playing==0 then goto END',
    'exit, skip',
    'label END'
] ) ]
links += [ l('hb_james_rec',     'daw_play', delay=200 , options=[
    'if is_playing==0 then goto END',
    'exit, skip',
    'label END',
    'is_playing=1',
] ) ]
links += [ l('hb_james_rec',       'daw_record', [
    'hb_mitch_rec=pp',
    'hb_james_rec=pp',
    'hb_jesse_rec=pp'
] ) ]

links += l('hb_jesse_mitch',     'daw_jesse_mitch',       thru=X)
links += l('hb_jesse_james',     'daw_jesse_james',       thru=X)
links += l('hb_jesse_jesse',     'daw_jesse_jesse',       thru=X)
links += l('hb_jesse_drums',     'daw_jesse_drums',       thru=X)
links += l('hb_jesse_vol',       'daw_jesse_vol',         thru=X)
links += l('hb_jesse_click',     'daw_jesse_click',       thru=X)
links += l('hb_jesse_tbvol',     'daw_jesse_tbvol',       thru=X)
links += l('hb_jesse_tbio',      'daw_talkback',          thru=X, options=[
    'hb_mitch_tbio=pp',
    'hb_james_tbio=pp',
])
links += l('hb_jesse_james_lrc', 'daw_jesse_james_lrc',   thru=X)
links += l('hb_jesse_jesse_lrc', 'daw_jesse_jesse_lrc',   thru=X)
links += l('hb_jesse_mitch_lrc', 'daw_jesse_mitch_lrc',   thru=X)
links += [ l('hb_jesse_rec',     'daw_advance_playhead', options=[
    'if is_playing==0 then goto END',
    'exit, skip',
    'label END'
] ) ]
links += [ l('hb_jesse_rec',     'daw_play', delay=200 , options=[
    'if is_playing==0 then goto END',
    'exit, skip',
    'label END',
    'is_playing=1'
] ) ]
links += [ l('hb_jesse_rec',       'daw_record', [
    'hb_mitch_rec=pp',
    'hb_james_rec=pp',
    'hb_jesse_rec=pp'
] ) ]

    # hipbox solo btn
links += [ l('hb_mitch_solo', '', [
    'hb_mitch_solo=pp',
    'if pp==127 then goto ON',
    'label OFF',

    'daw_james_mitch=mitch_solo_james_mitch',
    'hb_james_mitch=mitch_solo_james_mitch',
    'daw_jesse_mitch=mitch_solo_jesse_mitch',
    'hb_jesse_mitch=mitch_solo_jesse_mitch',

    'daw_mitch_james=mitch_solo_mitch_james',
    'hb_mitch_james=mitch_solo_mitch_james',
    'daw_mitch_jesse=mitch_solo_mitch_jesse',
    'hb_mitch_jesse=mitch_solo_mitch_jesse',

    'goto END',
    'label ON',

    'mitch_solo_james_mitch=daw_james_mitch',
    'daw_james_mitch=0',
    'hb_james_mitch=0',

    'mitch_solo_jesse_mitch=daw_jesse_mitch',
    'daw_jesse_mitch=0',
    'hb_jesse_mitch=0',

    'mitch_solo_mitch_james=daw_mitch_james',
    'daw_mitch_james=0',
    'hb_mitch_james=0',
    'mitch_solo_mitch_jesse=daw_mitch_jesse',
    'daw_mitch_jesse=0',
    'hb_mitch_jesse=0',

    'label END'
]) ]
links += [ l('hb_james_solo', '', [
    'hb_james_solo=pp',
    'if pp==127 then goto ON',
    'label OFF',

    'daw_jesse_james=james_solo_jesse_james',
    'hb_jesse_james=james_solo_jesse_james',
    'daw_mitch_james=james_solo_mitch_james',
    'hb_mitch_james=james_solo_mitch_james',

    'daw_james_jesse=james_solo_james_jesse',
    'hb_james_jesse=james_solo_james_jesse',
    'daw_james_mitch=james_solo_james_mitch',
    'hb_james_mitch=james_solo_james_mitch',

    'goto END',
    'label ON',

    'james_solo_jesse_james=daw_jesse_james',
    'daw_jesse_james=0',
    'hb_jesse_james=0',

    'james_solo_mitch_james=daw_mitch_james',
    'daw_mitch_james=0',
    'hb_mitch_james=0',

    'james_solo_james_jesse=daw_james_jesse',
    'daw_james_jesse=0',
    'hb_james_jesse=0',
    'james_solo_james_mitch=daw_james_mitch',
    'daw_james_mitch=0',
    'hb_james_mitch=0',

    'label END'
]) ]
links += [ l('hb_jesse_solo', '', [
    'hb_jesse_solo=pp',
    'if pp==127 then goto ON',
    'label OFF',

    'daw_mitch_jesse=jesse_solo_mitch_jesse',
    'hb_mitch_jesse=jesse_solo_mitch_jesse',
    'daw_james_jesse=jesse_solo_james_jesse',
    'hb_james_jesse=jesse_solo_james_jesse',

    'daw_jesse_mitch=jesse_solo_jesse_mitch',
    'hb_jesse_mitch=jesse_solo_jesse_mitch',
    'daw_jesse_james=jesse_solo_jesse_james',
    'hb_jesse_james=jesse_solo_jesse_james',

    'goto END',
    'label ON',

    'jesse_solo_mitch_jesse=daw_mitch_jesse',
    'daw_mitch_jesse=0',
    'hb_mitch_jesse=0',

    'jesse_solo_james_jesse=daw_james_jesse',
    'daw_james_jesse=0',
    'hb_james_jesse=0',

    'jesse_solo_jesse_mitch=daw_jesse_mitch',
    'daw_jesse_mitch=0',
    'hb_jesse_mitch=0',
    'jesse_solo_jesse_james=daw_jesse_james',
    'daw_jesse_james=0',
    'hb_jesse_james=0',

    'label END'
]) ]
################################################################################


# ENDPOINTS ####################################################################
endpoints = [
    #Name,                     Ports,   Chan, Note Type, Note Incoming, Note Outgoing, Default Val

    # fcb1010 footpedal I/O's #
    # bank :00 #
    e('fcb1010_btn_1',         [p1,p2], 1,    'note',      1),
    e('fcb1010_btn_2',         [p1,p2], 1,    'note',      2),
    e('fcb1010_btn_3',         [p1,p2], 1,    'note',      3),
    e('fcb1010_btn_4',         [p1,p2], 1,    'note',      4),
    e('fcb1010_btn_5',         [p1,p2], 1,    'note',      5),
    e('fcb1010_btn_6',         [p1,p2], 1,    'note',      6),
    e('fcb1010_btn_7',         [p1,p2], 1,    'note',      7),
    e('fcb1010_btn_8',         [p1,p2], 1,    'note',      8),
    e('fcb1010_btn_9',         [p1,p2], 1,    'note',      9),
    e('fcb1010_btn_10',        [p1,p2], 1,    'note',     10),
    # bank :01 #
    e('fcb1010_btn_11',        [p1,p2], 1,    'note',     11),
    e('fcb1010_btn_12',        [p1,p2], 1,    'note',     12),
    e('fcb1010_btn_13',        [p1,p2], 1,    'note',     13),
    e('fcb1010_btn_14',        [p1,p2], 1,    'note',     14),
    e('fcb1010_btn_15',        [p1,p2], 1,    'note',     15),
    e('fcb1010_btn_16',        [p1,p2], 1,    'note',     16),
    e('fcb1010_btn_17',        [p1,p2], 1,    'note',     17),
    e('fcb1010_btn_18',        [p1,p2], 1,    'note',     18),
    e('fcb1010_btn_19',        [p1,p2], 1,    'note',     19),
    e('fcb1010_btn_20',        [p1,p2], 1,    'note',     20),
    # expression pedals #      
    e('fcb1010_exp_1',         [p1,p2], 1,    'cc',      126),
    e('fcb1010_exp_2',         [p1,p2], 1,    'cc',      127),

    #Name,                     Ports,   Chan, Note Type, Note Incoming, Note Outgoing, Default Val
    # bass effect I/O's #      
    e('fx_tuner',              [p2],    2,    'note',    'none',          1),
    e('fx_lowcut',             [p2],    2,    'cc',      'none',          2,             0),
    e('fx_hicut',              [p2],    2,    'cc',      'none',          3,           127),
    e('fx_dist',               [p2],    2,    'cc',      'none',          4,             0),
    e('fx_delay',              [p2],    2,    'cc',      'none',          5,             0),
    e('fx_s_delay_beat',       [p2],    2,    'cc',           6,          6,           105),
    e('fx_s_delay_fdbk',       [p2],    2,    'cc',           7,          7,            86),
    e('fx_s_delay_drywet',     [p2],    2,    'cc',           8,          8,            64),
    e('fx_reverb',             [p2],    2,    'cc',      'none',          9,             0),
    e('fx_octaver',            [p2],    2,    'cc',      'none',         10,             0),
    e('fx_amp',                [p2],    2,    'cc',          11,         11,            64),
    e('fx_volume',             [p2],    2,    'cc',      'none',         12,             0),
    e('fx_exp',                [p2],    2,    'cc',      'none',         13,             0),

    #Name,                     Ports,   Chan, Note Type, Note Incoming, Note Outgoing, Default Val
    # daw I/O's #
    e('daw_stop_playhead',     [p2],    2,    'note',    'none',         14),
    e('daw_stop_clips',        [p2],    2,    'note',    'none',         15),
    e('daw_advance_playhead',  [p2],    2,    'note',    'none',         16),
    e('daw_play',              [p2],    2,    'note',    'none',         17),
    e('daw_record',            [p2],    2,    'note',    'none',         18),
    e('daw_start_drums',       [p2],    2,    'note',    'none',         19),
    e('daw_start_trans_drums', [p2],    2,    'note',    'none',         20),
    e('daw_start_click',       [p2],    2,    'note',    'none',         21),
    e('daw_talkback',          [p2],    2,    'cc',          22,         22,           127),
    e('daw_bass_out',          [p2],    2,    'cc',          23,         23,           127),
    e('daw_drums_out',         [p2],    2,    'cc',          24,         24,           127),

    # leveling #
    e('daw_level_james',       [p2],    2,    'cc',          25,         25,            78),
    e('daw_level_jesse',       [p2],    2,    'cc',          26,         26,            78),
    e('daw_level_in_mitch',    [p2],    2,    'cc',          27,         27,            36),
    e('daw_level_out_mitch',   [p2],    2,    'cc',          28,         28,            56),

    e('daw_select_tuner',      [p2],    2,    'note',    'none',         29),
    e('daw_select_mitch',      [p2],    2,    'note',    'none',         30),

    #Name,                     Ports,   Chan, Note Type, Note Incoming, Note Outgoing, Default Val
    # hb I/O's #
    e('hb_mitch_mitch',        [p3],    3,    'cc',           1,          1,            89),
    e('hb_mitch_james',        [p3],    3,    'cc',           2,          2,            89),
    e('hb_mitch_jesse',        [p3],    3,    'cc',           3,          3,            89),
    e('hb_mitch_drums',        [p3],    3,    'cc',           4,          4,            89),
    e('hb_mitch_vol',          [p3],    3,    'cc',           5,          5,            89),
    e('hb_mitch_click',        [p3],    3,    'cc',           6,          6,            89),
    e('hb_mitch_tbvol',        [p3],    3,    'cc',           7,          7,            89),
    e('hb_mitch_solo',         [p3],    3,    'cc',           8,          8,             0),
    e('hb_mitch_tbio',         [p3],    3,    'cc',           9,          9,           127),
    e('hb_mitch_rec',          [p3],    3,    'cc',          10,         10,             0),
    e('hb_mitch_james_lrc',    [p3],    3,    'cc',          11,         11,             0),
    e('hb_mitch_jesse_lrc',    [p3],    3,    'cc',          12,         12,           127),
    e('hb_mitch_mitch_lrc',    [p3],    3,    'cc',          13,         13,            64),
    e('hb_bass_out',           [p3],    3,    'cc',          14,         14,           127),
    e('hb_drums_out',          [p3],    3,    'cc',          15,         15,           127),
    e('hb_level_james',        [p3],    3,    'cc',          16,         16,            78),
    e('hb_level_jesse',        [p3],    3,    'cc',          17,         17,            78),
    e('hb_level_in_mitch',     [p3],    3,    'cc',          18,         18,            36),
    e('hb_level_out_mitch',    [p3],    3,    'cc',          19,         19,            56),
    e('hb_amp',                [p3],    3,    'cc',          20,         20,            64),
    e('hb_s_delay_beat',       [p3],    3,    'cc',          21,         21,           105),
    e('hb_s_delay_fdbk',       [p3],    3,    'cc',          22,         22,            86),
    e('hb_s_delay_drywet',     [p3],    3,    'cc',          23,         23,            64),
    e('hb_mitch_tuner',        [p3],    3,    'cc',          24,     'none',             0),

    e('hb_james_mitch',        [p3],    4,    'cc',           1,          1,            89),
    e('hb_james_james',        [p3],    4,    'cc',           2,          2,            89),
    e('hb_james_jesse',        [p3],    4,    'cc',           3,          3,            89),
    e('hb_james_drums',        [p3],    4,    'cc',           4,          4,            89),
    e('hb_james_vol',          [p3],    4,    'cc',           5,          5,            89),
    e('hb_james_click',        [p3],    4,    'cc',           6,          6,            89),
    e('hb_james_tbvol',        [p3],    4,    'cc',           7,          7,            89),
    e('hb_james_solo',         [p3],    4,    'cc',           8,          8,             0),
    e('hb_james_tbio',         [p3],    4,    'cc',           9,          9,           127),
    e('hb_james_rec',          [p3],    4,    'cc',          10,         10,             0),
    e('hb_james_james_lrc',    [p3],    4,    'cc',          11,         11,             0),
    e('hb_james_jesse_lrc',    [p3],    4,    'cc',          12,         12,           127),
    e('hb_james_mitch_lrc',    [p3],    4,    'cc',          13,         13,            64),

    e('hb_jesse_mitch',        [p3],    5,    'cc',           1,          1,            89),
    e('hb_jesse_james',        [p3],    5,    'cc',           2,          2,            89),
    e('hb_jesse_jesse',        [p3],    5,    'cc',           3,          3,            89),
    e('hb_jesse_drums',        [p3],    5,    'cc',           4,          4,            89),
    e('hb_jesse_vol',          [p3],    5,    'cc',           5,          5,            89),
    e('hb_jesse_click',        [p3],    5,    'cc',           6,          6,            89),
    e('hb_jesse_tbvol',        [p3],    5,    'cc',           7,          7,            89),
    e('hb_jesse_solo',         [p3],    5,    'cc',           8,          8,             0),
    e('hb_jesse_tbio',         [p3],    5,    'cc',           9,          9,           127),
    e('hb_jesse_rec',          [p3],    5,    'cc',          10,         10,             0),
    e('hb_jesse_james_lrc',    [p3],    5,    'cc',          11,         11,             0),
    e('hb_jesse_jesse_lrc',    [p3],    5,    'cc',          12,         12,           127),
    e('hb_jesse_mitch_lrc',    [p3],    5,    'cc',          13,         13,            64),

    e('daw_mitch_mitch',       [p2],    3,    'cc',           1,          1,            89),
    e('daw_mitch_james',       [p2],    3,    'cc',           2,          2,            89),
    e('daw_mitch_jesse',       [p2],    3,    'cc',           3,          3,            89),
    e('daw_mitch_drums',       [p2],    3,    'cc',           4,          4,            89),
    e('daw_mitch_vol',         [p2],    3,    'cc',           5,          5,            89),
    e('daw_mitch_click',       [p2],    3,    'cc',           6,          6,            89),
    e('daw_mitch_tbvol',       [p2],    3,    'cc',           7,          7,            89),
    e('daw_mitch_james_lrc',   [p2],    3,    'cc',           8,          8,             0),
    e('daw_mitch_jesse_lrc',   [p2],    3,    'cc',           9,          9,           127),
    e('daw_mitch_mitch_lrc',   [p2],    3,    'cc',          10,         10,            64),

    e('daw_james_mitch',       [p2],    4,    'cc',           1,          1,            89),
    e('daw_james_james',       [p2],    4,    'cc',           2,          2,            89),
    e('daw_james_jesse',       [p2],    4,    'cc',           3,          3,            89),
    e('daw_james_drums',       [p2],    4,    'cc',           4,          4,            89),
    e('daw_james_vol',         [p2],    4,    'cc',           5,          5,            89),
    e('daw_james_click',       [p2],    4,    'cc',           6,          6,            89),
    e('daw_james_tbvol',       [p2],    4,    'cc',           7,          7,            89),
    e('daw_james_james_lrc',   [p2],    4,    'cc',           8,          8,             0),
    e('daw_james_jesse_lrc',   [p2],    4,    'cc',           9,          9,           127),
    e('daw_james_mitch_lrc',   [p2],    4,    'cc',          10,         10,            64),

    e('daw_jesse_mitch',       [p2],    5,    'cc',           1,          1,            89),
    e('daw_jesse_james',       [p2],    5,    'cc',           2,          2,            89),
    e('daw_jesse_jesse',       [p2],    5,    'cc',           3,          3,            89),
    e('daw_jesse_drums',       [p2],    5,    'cc',           4,          4,            89),
    e('daw_jesse_vol',         [p2],    5,    'cc',           5,          5,            89),
    e('daw_jesse_click',       [p2],    5,    'cc',           6,          6,            89),
    e('daw_jesse_tbvol',       [p2],    5,    'cc',           7,          7,            89),
    e('daw_jesse_james_lrc',   [p2],    5,    'cc',           8,          8,             0),
    e('daw_jesse_jesse_lrc',   [p2],    5,    'cc',           9,          9,           127),
    e('daw_jesse_mitch_lrc',   [p2],    5,    'cc',          10,         10,            64),

]
################################################################################


# GLOBAL VARIABLES #############################################################
global_variables = [
    # daw vars #
    ('update_freq',  2000),
    ('is_playing',      0),
    ('current_song',    0),

    # hipbox solo btn
    ('mitch_solo_mitch_james', 0),
    ('mitch_solo_mitch_jesse', 0),
    ('mitch_solo_james_mitch', 0),
    ('mitch_solo_jesse_mitch', 0),
    ('james_solo_james_mitch', 0),
    ('james_solo_james_jesse', 0),
    ('james_solo_mitch_james', 0),
    ('james_solo_jesse_james', 0),
    ('jesse_solo_jesse_mitch', 0),
    ('jesse_solo_jesse_james', 0),
    ('jesse_solo_mitch_jesse', 0),
    ('jesse_solo_james_jesse', 0),
]
################################################################################


# songs #
songs = 'blind old_pete sono petrichor space'.split()
for i, song in enumerate(songs):
    global_variables.append( (song, i) )
    endpoints.append(e('song_click_{}'.format(song), [p2], 10, 'note', 'none', 'auto'))
    endpoints.append(e('song_intro_{}'.format(song), [p2], 10, 'note', 'none', 'auto'))
    endpoints.append(e('song_{}'.format(song),       [p2], 10, 'note', 'none', 'auto'))
    links.append(l('fcb1010_btn_17', 'song_{}'.format(song),       [ 'if current_song=={} then goto END'.format(song), 'exit, skip', 'label END', ]))
    links.append(l('fcb1010_btn_18', 'song_intro_{}'.format(song), [ 'if current_song=={} then goto END'.format(song), 'exit, skip', 'label END', ]))
    links.append(l('fcb1010_btn_19', 'song_click_{}'.format(song), [ 'if current_song=={} then goto END'.format(song), 'exit, skip', 'label END', ]))


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
