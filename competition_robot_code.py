"""
Competition test code.
Copyright 2016. Pioneers in Engineering.
"""

from api.Gamepads import *
from api.Robot import *
import time

# Define different speeds
full_speed = 1
mid_speed = 0.5
slow_speed = 0.1


def autonomous():
    """
    Put auton code here, called 20 times a second
    """
    # Move forward for 3 seconds
    set_motor('right', -1)
    set_motor('left', 0.8)
    time.sleep(3.3)
    # Turn Left for 1.5 seconds
    set_motor('right', 0.5)
    set_motor('left', 0.5)
    time.sleep(1.5)
    # Move forward for 1 seconds
    set_motor('right', -1)
    set_motor('left', 1)
    time.sleep(1)
    # Sit there pressing the button for 3 seconds (1 time)
    set_motor('right', 0)
    set_motor('left', 0)
    time.sleep(3)
    # Move back for 1 seconds
    set_motor('right', 0.5)
    set_motor('left', -0.5)
    time.sleep(1)
    # Move forward for 1 seconds
    set_motor('right', -1)
    set_motor('left', 1)
    time.sleep(1)
    # Sit there pressing the button for 3 seconds (2 time)
    set_motor('right', 0)
    set_motor('left', 0)
    time.sleep(3)
    # Move back for 1 seconds
    set_motor('right', 0.5)
    set_motor('left', -0.5)
    time.sleep(1)
    # Move forward for 1 seconds
    set_motor('right', -1)
    set_motor('left', 1)
    time.sleep(1)
    # Sit there pressing the button for 3 seconds (3 time)
    set_motor('right', 0)
    set_motor('left', 0)
    time.sleep(3)
    # Move back for 1 seconds
    set_motor('right', 0.5)
    set_motor('left', -0.5)
    time.sleep(1)
    # Move forward for 1 seconds
    set_motor('right', -1)
    set_motor('left', 1)
    time.sleep(1)
    # Sit there pressing the button for 3 seconds (4 time)
    set_motor('right', 0)
    set_motor('left', 0)
    time.sleep(3)
    # Move back for 1 seconds
    set_motor('right', 1)
    set_motor('left', -1)
    time.sleep(1)
    # Turn right for 1.5 seconds
    set_motor('right', -0.6)
    set_motor('left', -0.7)
    time.sleep(1.5)
    # Wait for match to start for 2 seconds
    set_motor('right', 0)
    set_motor('left', 0)
    time.sleep(1.7)
def teleop():
    """
    Put teleop code here, called 20 times a second
    """
    # ramp up and down (Auto)
    if get_button(0, Button.R_BUMPER):
        set_motor('arm', .35)
        set_motor('string', -1)
        time.sleep(.43)
    elif get_button(0, Button.L_BUMPER):
        set_motor('arm', -.35)
        set_motor('string', 1)
        time.sleep(.8)
    else:
        set_motor('arm', 0)
        set_motor('string', 0)
        
    # Ramp up and down (Manu)
    if get_button(0, Button.R_TRIGGER):
        set_motor('arm', .35)
        set_motor('string', -1)
    elif get_button(0, Button.L_TRIGGER):
        set_motor('arm', -.35)
        set_motor('string', .7)
    else:
        set_motor('arm', 0)
        set_motor('string', 0)
        
    # Door Gate
    if get_button(0, Button.A):
        set_motor('door', mid_speed)
        time.sleep(.05)
    elif get_button(0, Button.B):
        set_motor('door', -1 * mid_speed)
        time.sleep(.1)
    else:
        set_motor('door', 0)
    # Master buttons list
    '''
    if get_button(0, Button.A):
    if get_button(0, Button.B):
    if get_button(0, Button.BACK):
    if get_button(0, Button.DPAD_DOWN):
    if get_button(0, Button.DPAD_RIGHT):
    if get_button(0, Button.DPAD_UP):
    if get_button(0, Button.L_STICK):
    if get_button(0, Button.START):
    if get_button(0, Button.X):
    if get_button(0, Button.XBOX):
    if get_button(0, Button.Y):
    '''
    # For now, get_joysticks actually takes in a string index, not integer
    # This will be fixed in a later update
    gamepad_index = 0
    joystick_1_value = get_axis(gamepad_index, Joystick.LEFT_Y)
    joystick_2_value = get_axis(gamepad_index, Joystick.RIGHT_Y)
    
    # Drives the robot at power_level percentage, based off of the joystick values.
    set_motor('right', full_speed * joystick_2_value)
    set_motor('left', -1 * full_speed * joystick_1_value)

    if get_button(0, Button.DPAD_DOWN):
        set_motor('right', mid_speed)
        set_motor('left', -1 * mid_speed)
    if get_button(0, Button.DPAD_UP):
        set_motor('right', -1 * mid_speed)
        set_motor('left', mid_speed)

    # time.sleep(.05)
while True:

    if is_autonomous() and is_enabled():
        autonomous()
    if not is_autonomous() and is_enabled():
        teleop()

    time.sleep(0.05)