import cozmo, time
from inputs import get_gamepad
from multiprocessing import Process
import atexit

def quick_flash(robot: cozmo.robot.Robot):
    delay = 0.1
    robot.set_all_backpack_lights(cozmo.lights.red_light)
    time.sleep(delay)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(delay)
    robot.set_all_backpack_lights(cozmo.lights.red_light)
    time.sleep(delay)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(delay)
    robot.set_all_backpack_lights(cozmo.lights.blue_light)
    time.sleep(delay)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(delay)
    robot.set_all_backpack_lights(cozmo.lights.blue_light)

    time.sleep(delay)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(delay)

def quint_flash(robot: cozmo.robot.Robot):
    robot.set_backpack_lights(cozmo.lights.off_light,
                                cozmo.lights.blue_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                cozmo.lights.off_light)
    time.sleep(0.1)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(0.1)
    robot.set_backpack_lights(cozmo.lights.off_light,
                                cozmo.lights.blue_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                cozmo.lights.off_light)
    time.sleep(0.1)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(1)

def quint_flash_p1_p1(robot: cozmo.robot.Robot):
    robot.set_backpack_lights(cozmo.lights.off_light,
                                cozmo.lights.blue_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                cozmo.lights.off_light)
    time.sleep(0.1)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(0.1)
    robot.set_backpack_lights(cozmo.lights.off_light,
                                cozmo.lights.blue_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                cozmo.lights.off_light)
    time.sleep(0.1)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(1)

def quint_flash_p1_p2(robot: cozmo.robot.Robot):
    robot.set_backpack_lights(cozmo.lights.red_light,
                                cozmo.lights.off_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                cozmo.lights.red_light)
    time.sleep(0.1)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(0.1)
    robot.set_backpack_lights(cozmo.lights.red_light,
                                cozmo.lights.off_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                cozmo.lights.red_light)
    time.sleep(0.3)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(0.1)

    robot.set_backpack_lights(cozmo.lights.off_light,
                                cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.off_light,
                                cozmo.lights.off_light)
    time.sleep(0.1)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(0.1)
    robot.set_backpack_lights(cozmo.lights.off_light,
                                cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.off_light,
                                cozmo.lights.off_light)
    time.sleep(0.3)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(0.1)

def single_flash_p1_p1(robot: cozmo.robot.Robot):
    robot.set_backpack_lights(cozmo.lights.red_light,
                                cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.red_light,
                                cozmo.lights.red_light)
    time.sleep(0.150)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(0.800)

def single_flash_p1_p2(robot: cozmo.robot.Robot):
    robot.set_backpack_lights(cozmo.lights.red_light,
                                cozmo.lights.off_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                cozmo.lights.red_light)
    time.sleep(0.5)
    robot.set_backpack_lights(cozmo.lights.off_light,
                                cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.off_light,
                                cozmo.lights.off_light)
    time.sleep(0.5)

def manual_lights(robot: cozmo.robot.Robot):
    robot.set_backpack_lights(cozmo.lights.red_light,
                                cozmo.lights.off_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                cozmo.lights.red_light)
    time.sleep(0.5)
    robot.set_backpack_lights(cozmo.lights.off_light,
                                cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.off_light,
                                cozmo.lights.off_light)
    time.sleep(0.5)

def lights_off(robot: cozmo.robot.Robot):
    robot.set_backpack_lights_off()


lights_functions = [lights_off, quick_flash, quint_flash, quint_flash_p1_p1, quint_flash_p1_p2, single_flash_p1_p1, single_flash_p1_p2, manual_lights]
nb_functions = len(lights_functions)
current = 0

def read_input():
    print('Appel read input')
    global current
    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == 'Absolute' and event.code == 'ABS_HAT0X' and event.state == 1:
                if current == nb_functions-1:
                    current = 0
                else:
                    current += 1
                print('Switching to function ' + lights_functions[current].__name__ + ' -- Current is ' + str(current))
                break

def do_lighting(robot: cozmo.robot.Robot):
    while True:
        fn = lights_functions[current]
        print('Executing fuction ' + fn.__name__ + ' -- Current is ' + str(current))
        fn(robot)

def kill_runner(runner):
    runner.terminate()

def cozmo_program(robot: cozmo.robot.Robot):
    # read_input()
    # while True:
    #     quint_flash_p1_p2(robot)
    input_reader = Process(target=read_input)
    input_reader.start()    
    
    atexit.register(kill_runner, input_reader)

    while True:
        time.sleep(1)
    #do_lighting(robot)

cozmo.run_program(cozmo_program)
