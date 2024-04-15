import time
import board
import digitalio
import usb_hid 
import base_key_mapping as km
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.mouse import Mouse
 
# Config variables
macro_delay = 0.05

print("Loaded!")

def send_keys(button_number):
    try:
        key = km.keys[button_number]
        state = buttons[button_i]
        if state:
            if key[0] == km.STRING:
                keyboard_layout.write(key[1])
            elif key[0] == km.KEY:
                keyboard.press(*key[1])
            elif key[0] == km.CONTROL_CODE:
                cc.press(key[1])
            elif key[0] == km.MACRO:
                custom_delay = False
                iterkey = iter(key[1])
                for i in iterkey:
                    custom_delay = False
                    if type(i) is list:
                        keyboard.send(*i)
                    elif type(i) is int or float:
                        custom_delay = True
                        time.sleep(i)
                    if custom_delay == False:
                        time.sleep(macro_delay)
        else:
            if key[0] == km.KEY:
                keyboard.release(*key[1])
            elif key[0] == km.CONTROL_CODE:
                cc.release()
    except ValueError:
        pass


activator_pins = [board.GP28, board.GP27, board.GP22]
receiver_pins = [board.GP12, board.GP10, board.GP8, board.GP6]

receivers = []
for pin in receiver_pins:
    receiver = digitalio.DigitalInOut(pin)
    receiver.switch_to_input(pull=digitalio.Pull.DOWN)
    receivers.append(receiver)

activators = []
for activator in activator_pins:
    activator = digitalio.DigitalInOut(activator)
    activator.direction = digitalio.Direction.OUTPUT
    activators.append(activator)

buttons_count = len(activators) * len(receivers)
buttons = [False] * buttons_count
history = [False] * buttons_count

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
cc = ConsumerControl(usb_hid.devices)

activators_count = len(activators)
receivers_count = len(receivers)

while True:
    for activator_i in range(activators_count):
        activators[activator_i].value = True
        for receiver_i in range(receivers_count):
            buttons[activator_i * receivers_count + receiver_i] = receivers[receiver_i].value
        activators[activator_i].value = False
    for button_i in range(buttons_count):
        if buttons[button_i] != history[button_i]:
            send_keys(button_i)
            history[button_i] = buttons[button_i]
    time.sleep(0.01)