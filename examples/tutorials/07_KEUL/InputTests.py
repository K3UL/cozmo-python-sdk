# Module de gestions des inputs hardware
from inputs import get_gamepad

minVal = 0
maxVal = 0

while True:
    events = get_gamepad()
    for event in events:
        if event.ev_type == 'Absolute' and event.code == 'ABS_Y':
            if event.state < minVal:
                minVal = event.state
            elif event.state > maxVal:
                maxVal = event.state

            print(f"Min : {minVal} -- Max : {maxVal}")
