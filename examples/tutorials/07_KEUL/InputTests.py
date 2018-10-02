# Module de gestions des inputs hardware
from inputs import get_gamepad

minVal = 0
maxVal = 0

while True:
    events = get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)
