from objects import n
from super_secret_footer import footer_signature, footer_signed_by

# ENDPOINTS ####################################################################
# fcb1010 foot switches
endpoints = [
    {   'Name': 'fcb1010_btn_{}'.format(i),
            'Incoming': { 'Note': i, 'Channel': 1, 'Note Type': 'note' },
            'Ports': [ 'Scarlett 18i20 USB', 'Bome Virtual Port 1' ]}
    for i in range(1,20)]

# fcb1010 expression pedals
endpoints += [
    {   'Name': 'fcb1010_exp_1'.format(i),
            'Incoming': { 'Note': 126, 'Channel': 1, 'Note Type': 'cc' },
            'Ports': [ 'Scarlett 18i20 USB', 'Bome Virtual Port 1' ]},

    {   'Name': 'fcb1010_exp_2'.format(i),
            'Incoming': { 'Note': 127, 'Channel': 1, 'Note Type': 'cc' },
            'Ports': [ 'Scarlett 18i20 USB', 'Bome Virtual Port 1' ]}
]

# bass effects thru ableton
effects = 'fx_lowpass fx_hipass fx_dist fx_delay fx_reverb'.split()
endpoints += [
    {   'Name': e,
            'Incoming': { 'Note': 'auto', 'Channel': 2, 'Note Type': 'cc' },
            'Outgoing': { 'Note': 'Incoming', 'Channel': 2, 'Note Type': 'cc' },
            'Ports': [ 'Bome Virtual Port 1' ]}
    for e in effects]
################################################################################


# LINKS ########################################################################
links = [
    {   'Link': ('fcb1010_btn_1', 'fx_dist'), 'Options': []}
]
################################################################################



# GLOBAL VARIABLES #############################################################
global_variables = [
    ('current_song', 0),
    ('petrichor',    1),
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
