from machine import Pin
from time

button = Pin(4, Pin.IN, Pin.PULL_DOWN)  # Changed to GPIO4 with pull-down
led = Pin(2, Pin.OUT)

# Main loop
while True:

# put the code here

    print(button.value())
    if button.value() == 1:  # Button pressed (high due to pull-down)
        print("Stopped")
        break
