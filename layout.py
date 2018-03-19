from ObjectContainer import ObjectContainer as oc
from objects import n

def get_body():
    inputs = {

    # FCB1010 #######################################################################################################################################
    # Foot Switches
    "fcb1010_btn_1": { "Channel": 1, "Note":   n(1,ch=1), "Type": "note", "To":  "fx_low_cut", "Ports": [ "Scarlett 18i20 USB", "Bome Virtual Port 1" ] },
    "fcb1010_btn_2": { "Channel": 1, "Note":   n(2,ch=1), "Type": "note", "To": "fx_low_pass", "Ports": [ "Scarlett 18i20 USB", "Bome Virtual Port 1" ] },
    "fcb1010_btn_3": { "Channel": 1, "Note":   n(3,ch=1), "Type": "note", "To":        "stop", "Ports": [ "Scarlett 18i20 USB", "Bome Virtual Port 1" ] },
    # Expression Pedals
    "fcb1010_exp_1": { "Channel": 1, "Note": n(126,ch=1), "Type":   "cc", "To":  "exp_volume", "Ports": [ "Scarlett 18i20 USB", "Bome Virtual Port 1" ] },
    "fcb1010_exp_2": { "Channel": 1, "Note": n(127,ch=1), "Type":   "cc", "To":  "exp_reverb", "Ports": [ "Scarlett 18i20 USB", "Bome Virtual Port 1" ] },

    # HIPBOX ########################################################################################################################################
    # Mitch
#   "tosc_mitch_james": { "Channel": 10, "Note": n(ch=10), "Type": "cc", "To": "hb_mitch_james", "Ports": [ "TouchOSC Bridge" ] },
#   "tosc_mitch_jesse": { "Channel": 10, "Note": n(ch=10), "Type": "cc", "To": "hb_mitch_jesse", "Ports": [ "TouchOSC Bridge" ] },
#   "tosc_mitch_durms": { "Channel": 10, "Note": n(ch=10), "Type": "cc", "To": "hb_mitch_drums", "Ports": [ "TouchOSC Bridge" ] },
#   "tosc_mitch_metro": { "Channel": 10, "Note": n(ch=10), "Type": "cc", "To": "hb_mitch_metro", "Ports": [ "TouchOSC Bridge" ] },
#   "tosc_mitch_bass" : { "Channel": 10, "Note": n(ch=10), "Type": "cc", "To": "hb_mitch_bass",  "Ports": [ "TouchOSC Bridge" ] },
#   "tosc_mitch_vol"  : { "Channel": 10, "Note": n(ch=10), "Type": "cc", "To": "hb_mitch_vol",   "Ports": [ "TouchOSC Bridge" ] },

    }

    outputs = {
    # Effects
    "fx_low_cut"       : { "Channel": 1, "Note": n(ch=1), "Type":   "cc", "Ports": [ "Bome Virtual Port 1" ], "Start Val":   0 },
    "fx_low_pass"      : { "Channel": 1, "Note": n(ch=1), "Type":   "cc", "Ports": [ "Bome Virtual Port 1" ], "Start Val": 127 },
    "exp_volume"       : { "Channel": 1, "Note": n(ch=1), "Type":   "cc", "Ports": [ "Bome Virtual Port 1" ], "Start Val":   0 },
    "exp_reverb"       : { "Channel": 1, "Note": n(ch=1), "Type":   "cc", "Ports": [ "Bome Virtual Port 1" ], "Start Val":   0 },
    # System
    "stop"             : { "Channel": 1, "Note": n(ch=1), "Type": "note", "Ports": [ "Bome Virtual Port 1" ] },
    "stop_clips"       : { "Channel": 1, "Note": n(ch=1), "Type": "note", "Ports": [ "Bome Virtual Port 1" ] },
    "stop_clips_d"     : { "Channel": 1, "Note": n(ch=1), "Type": "note", "Ports": [ "Bome Virtual Port 1" ], "Delay": 50 },
    "stop_play_head"   : { "Channel": 1, "Note": n(ch=1), "Type": "note", "Ports": [ "Bome Virtual Port 1" ] },
    "stop_play_head_d" : { "Channel": 1, "Note": n(ch=1), "Type": "note", "Ports": [ "Bome Virtual Port 1" ], "Delay": 50 },
    }

    events = {
    "stop" : { "Output": [ "stop_clips", "stop_clips_d", "stop_play_head", "stop_play_head_d" ] }
    }

    body = {
        "Inputs"  : inputs,
        "Outputs" : outputs,
        "Events"  : events
    }

    return body
