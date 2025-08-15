from machine import Pin
from time import sleep

button = Pin(4, Pin.IN, Pin.PULL_DOWN)  # GPIO4 with pull-down

# Main loop
while True:
    #code here
    if button.value() == 1:  # Button pressed
        print("Stopped")
        break
    sleep(0.1)  # Prevent excessive polling
