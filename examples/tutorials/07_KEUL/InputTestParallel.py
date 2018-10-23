import time
from inputs import get_gamepad
from multiprocessing import Process
import atexit

def firstFunc():
    print("FIRST FUNCTION")

def secondFunc():
    print("SECOND FUNCTION")

lights_functions = [firstFunc, secondFunc]
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
                print('Switching to function ' + lights_functions[current].__name__ + ' -- EN cours is ' + str(current))

def kill_runner(runner):
    runner.terminate()

def cozmo_program():
    input_reader = Process(target=read_input)
    input_reader.start()    
    
    atexit.register(kill_runner, input_reader)

    while True:
        time.sleep(1)

if __name__ == '__main__':
    cozmo_program()