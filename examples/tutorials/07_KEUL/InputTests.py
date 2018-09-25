# Module de gestions des inputs hardware
from inputs import get_gamepad

while True:
    events = get_gamepad()
    for event in events:
        if(event.ev_type == 'Absolute' and event.code == 'ABS_X'):
            print(event.ev_type, event.code, event.state)