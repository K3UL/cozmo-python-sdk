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

min_head_angle = -25
max_head_angle = 44.5
min_analog_val = -32767
max_analog_val = 32767
prev_head_stick_val = 0

def get_head_angle_from_stick_val(analog_val: int):
    analog_gap = round(max_analog_val - min_analog_val, 2)
    head_gap = round(max_head_angle - min_head_angle, 2)
    mid_head_val = round((min_head_angle + max_head_angle) / 2, 2)
    divider = round(analog_gap / head_gap, 2)

    return degrees(round((analog_val/divider) + mid_head_val, 2))

# We use a deadzone because even when resting the joysticks are returning values
# Might vary depending on the controller. Ideally should be calculated by checking values over time
turning_dead_zone = [-400, 3500]

def handle_control_input_for_lift(robot: cozmo.robot.Robot, pad_event):
    if(pad_event.ev_type == 'Absolute' and pad_event.code == 'ABS_HAT0Y'):
        if pad_event.state > 0:
            robot.move_lift(-5)
        elif pad_event.state < 0:
            robot.move_lift(5)

def handle_control_input_for_head(robot: cozmo.robot.Robot, pad_event):
    '''
        Moves Cozmo's head following the analog stick

        Analog stick goes from -32 768 to 32 767 => Gap of 65 535
        Cozmo's head goes from angles -25 deg to 44.5 => Gap of 69.5
        We're going to consider that a difference of 1 000 on the stick is not worth a movement when considered in deg. Over that value we'll move

        The middle of Cozmo's head angles is actually 9.75 and not 0
        65535/69.5 (the gaps) is 942.95
        - We're gonna consider that the angle goes from -34.75 to +34.75 (having zero has the middle) and then add 9.75
        - -> Any value over 44.5 or under -25 will be coerced inside these bounds
        - Going from analog is going to be (analogVal/942.95)+9.75
        - Generalized, the formula will be (analogVal/(AnalogGap/HeadGap))+((MinHeadAngle+MaxHeadAngle)/2)
    '''
    if pad_event.ev_type == 'Absolute' and pad_event.code == 'ABS_RY':
        if deq_last_inputs and (abs(pad_event.state - deq_last_inputs[-1]) < 1000):
            return

        if deq_last_inputs and len(deq_last_inputs) == input_cache_size:
            deq_last_inputs.popleft()
        deq_last_inputs.append(pad_event.state)
        if pad_event.state < -5000 and len(deq_last_inputs) == input_cache_size and not any(item > -5000 for item in deq_last_inputs):
            print(pad_event.state)
            try:
                robot.set_head_angle(get_head_angle_from_stick_val(pad_event.state))
            except cozmo.exceptions.RobotBusy:
                pass
        elif pad_event.state > 5000 and len(deq_last_inputs) == input_cache_size and not any(item < 5000 for item in deq_last_inputs):
            print(pad_event.state)
            try:
                robot.set_head_angle(get_head_angle_from_stick_val(pad_event.state))
            except cozmo.exceptions.RobotBusy:
                pass

def handle_control_input_for_acceleration(robot: cozmo.robot.Robot, pad_events):
    for pad_event in pad_events:
        # Check for direction
        # Go forward or go backward
        if pad_event.ev_type == 'Absolute' and pad_event.code == 'ABS_RZ':
            speed = pad_event.state * acceleration_factor
            robot.drive_wheels(speed, speed)
        elif pad_event.ev_type == 'Absolute' and pad_event.code == 'ABS_Z':
            speed = pad_event.state * acceleration_factor * -1
            robot.drive_wheels(speed, speed)

def handle_control_input(robot: cozmo.robot.Robot):
    '''
        Méthode permettant de faire les actions en fonction des inputs de gamepad
    '''
    stop_all_movement = False
    while True and not stop_all_movement:
        events = get_gamepad()
        for event in events:
            #print(event.ev_type, event.code, event.state)
            handle_control_input_for_lift(robot, event)
            handle_control_input_for_head(robot, event)
        
        if robot.is_cliff_detected:
            robot.move_lift(5)
            robot.drive_wheels(-800, -800, duration=0.5)
            robot.move_lift(-5)
            stop_all_movement = True
            break
        
        handle_control_input_for_acceleration(robot, events)

def cozmo_program(robot: cozmo.robot.Robot):
    min_head_angle = cozmo.robot.MIN_HEAD_ANGLE.degrees
    max_head_angle = cozmo.robot.MAX_HEAD_ANGLE.degrees

    handle_control_input(robot)
    #robot.move_lift(-5)
    #robot.set_head_angle(degrees(9.75)).wait_for_completed()

cozmo.run_program(cozmo_program, use_viewer=True)
