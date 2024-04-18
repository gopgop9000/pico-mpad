from adafruit_hid.keycode import Keycode as kc
from adafruit_hid.consumer_control_code import ConsumerControlCode as cc

# KEY presses all keys in order, then releases them all once it reaches the end of the list.
# MACRO presses then releases each key before moving to the next key in the list. 
# You can place a number between each key and it will delay the specified amount of seconds until the next key
# If there isn't a number between keys it will use the default delay in code.py
# If you want a multi-key keystroke in a macro, you would format it with another set of [] like: (MACRO, [kc.HOME, [kc.SHIFT, kc.ENTER], kc.TAB]),

STRING = 1
KEY = 2
CONTROL_CODE = 3
MACRO = 4

keys = [
    # ROW 1, COLUMN 1 
    (CONTROL_CODE, cc.VOLUME_INCREMENT),
    # ROW 1, COLUMN 2 | New line before current line
    (MACRO, [kc.HOME, kc.ENTER, kc.TAB]),
    # ROW 1, COLUMN 3 | New line after current line
    (MACRO, [kc.END, kc.ENTER, kc.TAB]),
    # ROW 1, COLUMN 4
    (KEY, [(kc.SHIFT, kc.A), kc.A]),
    # ROW 2, COLUMN 1 
    (CONTROL_CODE, cc.VOLUME_DECREMENT),
    # ROW 2, COLUMN 2
    (KEY, [kc.F16]),
    # ROW 2, COLUMN 3
    (KEY, [kc.F17]),
    # ROW 2, COLUMN 4
    (KEY, [kc.F18]),
    # ROW 3, COLUMN 1 | pause
    (CONTROL_CODE, cc.PLAY_PAUSE),
    # ROW 3, COLUMN 2 | back
    (CONTROL_CODE, cc.SCAN_PREVIOUS_TRACK),
    # ROW 3, COLUMN 3 | skip
    (CONTROL_CODE, cc.SCAN_NEXT_TRACK),
    # ROW 3, COLUMN 4 
    (KEY, [kc.F20])
]

