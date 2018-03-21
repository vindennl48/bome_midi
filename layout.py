from objects import n
from super_secret_footer import footer_signature, footer_signed_by

# ENDPOINTS ####################################################################


## fcb1010 #############################
'''
 - fcb1010_btn_1
 - fcb1010_btn_2
 - fcb1010_btn_3
 - fcb1010_btn_4
 - fcb1010_btn_5
 - fcb1010_btn_6
 - fcb1010_btn_7
 - fcb1010_btn_8
 - fcb1010_btn_9
 - fcb1010_btn_10
 - fcb1010_btn_11
 - fcb1010_btn_12
 - fcb1010_btn_13
 - fcb1010_btn_14
 - fcb1010_btn_15
 - fcb1010_btn_16
 - fcb1010_btn_17
 - fcb1010_btn_18
 - fcb1010_btn_19
 - fcb1010_btn_20

 - fcb1010_exp_1
 - fcb1010_exp_2
'''
endpoints = [
    { 
        'Name': 'fcb1010_btn_{:02d}'.format(i),
        'Incoming': {
            'Note'     : i,
            'Channel'  : 1,
            'Note Type': 'note'
        },
        'Ports': [
            'Scarlett 18i20 USB',
            'Bome Virtual Port 1'
        ]
    }
    for i in range(1,21)
]
endpoints += [
    {
        'Name': 'fcb1010_exp_{:02d}'.format(i),
        'Incoming': {
            'Note'     : i+126,
            'Channel'  : 1,
            'Note Type': 'cc'
        },
        'Ports': [
            'Scarlett 18i20 USB',
            'Bome Virtual Port 1'
        ]
    }
    for i in range(2)
]
########################################



## bass effects thru ableton ###########
'''
 - fx_lowpass
 - fx_hipass
 - fx_dist
 - fx_delay
 - fx_reverb
'''
effects = 'fx_lowcut fx_hicut fx_dist fx_delay fx_reverb'.split()
endpoints += [
    {
        'Name': e,
        'Incoming': {
            'Note': 'auto',
            'Channel': 2,
            'Note Type': 'cc'
        },
        'Outgoing': {
            'Note': 'Incoming',
            'Channel': 2,
            'Note Type': 'cc'
        },
        'Ports': [
            'Bome Virtual Port 1'
        ]
    }
    for e in effects
]
########################################
################################################################################



# LINKS ########################################################################
'''
'''
links = [
    {   'Link': ('fcb1010_btn_01',  'blind'),     'Options': [ 'current_song=blind' ]},
    {   'Link': ('fcb1010_btn_02',  'old_pete'),  'Options': [ 'current_song=old_pete' ]},
    {   'Link': ('fcb1010_btn_03',  'sono'),      'Options': [ 'current_song=sono' ]},
    {   'Link': ('fcb1010_btn_04',  'petrichor'), 'Options': [ 'current_song=petrichor' ]},
    {   'Link': ('fcb1010_btn_05',  'space'),     'Options': [ 'current_song=space' ]},

    {   'Link': ('fcb1010_btn_11', 'fx_lowcut'), 'Options': []},
    {   'Link': ('fcb1010_btn_12', 'fx_hicut'),  'Options': []},
    {   'Link': ('fcb1010_btn_13', 'fx_dist'),   'Options': []},
    {   'Link': ('fcb1010_btn_14', 'fx_delay'),  'Options': []},
    {   'Link': ('fcb1010_btn_15', 'fx_reverb'), 'Options': []},
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
