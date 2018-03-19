# [Preset.X] = preset number
# 
# Name=<Name of preset>
# 
# Active=<bool 0/1>
# 
# PresetSwitchIgnore=<bool 0/1> when true, prevents another preset 
#   from turning this on/off
# 
# NameX=<name of translator> x being translator number in list
# 
# IncomingX= type of incoming signal to activate translator
# OutgoingX= type of outgoing signal to activate translator
#   options for incoming/outgoing:
#       - 'EnDi00' = 'Processing is disabled'
#       - 'EnDi01' = 'Processing is enabled'
#       - 'EnDi02' = 'Project file is opened'
#       - 'None'   = 'None'
#       - 'Pres080000' = when current preset is activated
#       - 'Pres090000' = when current preset is deactivated
#       - 'Pres040000' = when preset is activated
#             'Pres040000' + num chars of preset name
#             'Pres04000EPlay Song - 01'
#       - 'Pres060000' = when preset is deactivated
#             'Pres060000' + num chars of preset name
#             'Pres06000EPlay Song - 01'
#       - 'MIDX':
#           - 3    = 'MIDI Message, Note On'
#           - at least this is in html format
#           IncomingX=MID3
#             <Incoming Action="MIDI">
#               <Description>Pedal 07</Description>
#               # if selecting specific ports instead
#               # of the project defaults \/ \/ 
#               <Ports>
#                 <Port>Scarlett 18i20 USB</Port>
#                 <Port>Bome Virtual Port 1</Port>
#               </Ports>
#               <Simple Type="NoteOn">
#                 <Channel num="0"/>
#                 <Value1 num="0x11"/>
#                 <Value2 num="0x64"/>
#               </Simple>
#             </Incoming>
#
#           OutgoingX=MID3
#             <Outgoing Action="MIDI">
#               <Ports>
#                 <Port>Bome Virtual Port 1</Port>
#               </Ports>
#               <Simple Type="NoteOn">
#                 <Channel num="0"/>
#                 <Value1 num="0x28"/>
#                 <Value2 num="0x64"/>
#               </Simple>
#             </Outgoing>
#
# OptionsX = 'Actv01Stop00OutO00Dlay200:MillisStMa00000020' # where x is iterator
# 'Activ01'= 'translator is active'
# 'Activ00'= 'translator is not active'
# 'Stop01' = 'stop processing after executing this translator'
# 'Stop00' = 'do not stop processing after executing this translator'
# 'OutO00' = 'swallow messages'
# 'OutO01' = 'do not swallow messages'
# 'Dlay200:Millis' = delay in milliseconds (do not include if no delay)
# 'MaXXXXXXXX' is hex of how many rules total
#
# label0006__cmt> is a new line
#
# any other comments '//<comment>' will be a new line label PLUS
#  a hex value of how many chars are in the comment string PLUS
#  the slashes.. for example:
#       '// this is a comment' = 'label001A__cmt>// this is a comment'
#
# labelXXXX<label name> is a programmed label of X hex characters
#       'Label "OFF"' = 'label0003OFF'
#
# if(<statement>) is an if statement
#       'if hh==127 then' = 'if(hh==127)'
#
# gotoXXXX<label name> is a goto label of X hex characters
#       'Goto "ON"' = 'goto0002ON'
#
# example of a full if statement:
#       'if hh==127 then Goto "ON"' = 
#           'if(hh==127)goto0003ON'
#
# 'exit rules, execute Outgoing Action' = execute
# 'exit rules, skip Outgoing Action' = noexecute
#
# assignment 'gk=127' or 'pp=0+0' = same thing, just need to parse
#   around the other shit in here.
#
# 



# Types of IO needed for my setup:
#   - Footswitch button to activate/deactivate fx
#   - Expression pedals to change volume/fx
#   - Footswitch button to stop clips
#   - Footswitch button to start scenes
#   - Footswitch button change songs
# 
#   - HipBox IO
#       - Phone slider to change volumes
#       - A way to save volume levels during 'solo'
#       - Phone button to start/stop recording
#       - Phone button to turn on/off talkback


# so any direct control changing can be in the following format
# 
# Preset toggle_switches
#   - Incoming = footswitch_btn_1
#   - Options  = if global_variable == 127 then pp=0
#                if global_variable ==   0 then pp=127
#                global_variable = pp
#   - Outgoing = fx_associated_w_btn_1
#                - set outgoing value to pp
# 
# Preset sliders (expression pedals or phone sliders)
#   - Incoming = slider_1
#                set slider_1 incoming to pp
#   - Options  = global_variable = pp
#   - Outgoing = fx_associated_w_slider_1
#                - set outgoing value to pp

# these are the slightly more complicated ones
# 
# Preset Timer
#   - This timer sends out a pulse.  Update presets will
#     get triggered by this pulse and send out an update
#     of global_variables to their respective devices.
#   - This will get created automatically.  This will
#     cycle thru all global_variables.
#
# Preset Event (ex. Stop All)
#   - An event is a preset that isn't as easy as a patch-
#     thru.  Multiple things need to happen in these steps.
#   - Translator "Stop"
#       - Incoming = activation of this preset
#       - Outgoing = btn_stop_button
#   - Translator "Stop_d"
#       - Incoming = activation of this preset
#       - Outgoing = btn_stop_button
#       - Delay    = 50ms
#   - Translator "Stop_Clips"
#       - Incoming = activation of this preset
#       - Outgoing = btn_stop_clips_button
#   - Translator "Stop_Clips_d"
#       - Incoming = activation of this preset
#       - Outgoing = btn_stop_clips_button
#       - Delay    = 50ms

# How to link
# 
# We will get a list of endpoints in a list. This way we can
#  just reference the endpoint name without needing to include 
#  all the rest of this shit.
endpoints = [
    # FCB1010
    {   "Name": "fcb1010_btn_1",
            "Incoming": { "Note": n(1,ch=1), "Channel": 1, "Note Type": "note" },
            "Ports": [ "Scarlett 18i20 USB", "Bome Midi Virtual Port 1" ]},

    # ABLETON
    {   "Name": "fx_dist",
            "Incoming": { "Note": n(ch=1), "Channel": 1, "Note Type": "cc" },
            "Outgoing": { "Note": n(ch=1), "Channel": 1, "Note Type": "cc" },
            "Ports": [ "Bome Midi Virtual Port 1" ]}

    {   "Name": "daw_stop_playhead",
            "Outgoing": { "Note": n(ch=2), "Channel": 2, "Note Type": "note" },
            "Ports": [ "Bome Midi Virtual Port 1" ]}

    {   "Name": "daw_stop_playhead_d",
            "Outgoing": { "Note": n(ch=2), "Channel": 2, "Note Type": "note" },
            "Ports": [ "Bome Midi Virtual Port 1" ],
            "Delay": "200ms"}
]

# events can reference either endpoints or other events, even it's self
events = [
    {   "Name": "event_stop_all",
            "Actions": [
                'daw_stop_playhead', 'daw_stop_playhead_d',
                'stop_clips', 'stop_clips_d' ] }
]

# additional variables that you would like to reference in the linking
custom_global_vars = {
    "current_song"  : 0,

    "blind"         : 0,
    "old_pete"      : 1,
    "sono"          : 2,
    "petrichor"     : 3,
}

links = [
    { "Link": ('fcb1010_btn_1',  'fx_dist'), "Conditions": [ "if current_song != blind then execute" ] },
    { "Link": ('fcb1010_btn_1',  'fx_low_cut'), "Conditions": [ "if current_song == petrichor then skip" ] },
    { "Link": ('fcb1010_btn_10', 'event_stop_all') },
]
