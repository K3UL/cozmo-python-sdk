# Module de base Cozmo
import cozmo

# Méthodes utilitaires de contrôles de déplacement de Cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

# Module de gestions des inputs hardware
from inputs import get_gamepad

# Objet gérant une file FIFO avec taille max
from collections import deque

input_cache_size = 5
last_inputs = []
deq_last_inputs = deque(last_inputs, input_cache_size)
acceleration_factor = 1.5

# We use a deadzone because even when resting the joysticks are returning values
# Might vary depending on the controller. Ideally should be calculated by checking values over time
turning_dead_zone = [-400, 3500]

def handle_control_input_for_lift(robot: cozmo.robot.Robot, pad_event):
    if(pad_event.ev_type == 'Absolute' and pad_event.code == 'ABS_RY'):
        if(deq_last_inputs and len(deq_last_inputs) == input_cache_size):
            deq_last_inputs.popleft()
        deq_last_inputs.append(pad_event.state)
        if(pad_event.state < -5000 and len(deq_last_inputs) == input_cache_size and not any(item > -5000 for item in deq_last_inputs)):
            robot.move_lift(-2)
        elif(pad_event.state > 5000 and len(deq_last_inputs) == input_cache_size and not any(item < 5000 for item in deq_last_inputs)):
            robot.move_lift(2)

def handle_control_input_for_acceleration(robot: cozmo.robot.Robot, pad_events):
    for pad_event in pad_events:
        speed_diff
        # Check for direction
        if(pad_event.ev_type == 'Absolute' and pad_event.code == 'ABS_Y'):
            
        # Go forward or go backward
        if(pad_event.ev_type == 'Absolute' and pad_event.code == 'ABS_RZ'):
            speed = pad_event.state * acceleration_factor
            robot.drive_wheels(speed, speed)
        elif(pad_event.ev_type == 'Absolute' and pad_event.code == 'ABS_Z'):
            speed = pad_event.state * acceleration_factor * -1
            robot.drive_wheels(speed, speed)

def handle_control_input(robot: cozmo.robot.Robot):
    '''
        Méthode permettant de faire les actions en fonction des inputs de gamepad
    '''    
    while True:
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)
            handle_control_input_for_lift(robot, event)
        handle_control_input_for_acceleration(robot, events)

def cozmo_program(robot: cozmo.robot.Robot):    
    handle_control_input(robot)

cozmo.run_program(cozmo_program)