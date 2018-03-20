from objects import n

endpoints = [
    # FCB1010
    {   'Name': 'fcb1010_btn_1',
            'Incoming': { 'Note': 1, 'Channel': 1, 'Note Type': 'note' },
            'Ports': [ 'Scarlett 18i20 USB', 'Bome Midi Virtual Port 1' ]},

    # ABLETON
    {   'Name': 'fx_dist',
            'Incoming': { 'Note': 'auto', 'Channel': 1, 'Note Type': 'cc' },
            'Outgoing': { 'Note': 'auto', 'Channel': 1, 'Note Type': 'cc' },
            'Ports': [ 'Bome Midi Virtual Port 1' ]}
]

links = [
    {   'Link'   : ('fcb1010_btn_1', 'fx_dist'),
        'Options': [
            '// Comment',
            '// Comment',
            '// Comment',
            '// Comment',
        ],
        'Delay'  : 200 }
]
