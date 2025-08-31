from machine import Pin
from time import sleep
import time

# Define pin (built-in LED is usually on pin 2 for ESP32)
led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_DOWN)  # GPIO4 with pull-down

# Main loop
while True:
    #code here

    led.value(1)   # Turn LED ON
    time.sleep(1)  # Wait 1 second
    led.value(0)   # Turn LED OFF
    time.sleep(1)  # Wait 1 second

    if button.value() == 1:  # Button pressed
        print("Stopped")
        break
    sleep(0.1)  # Prevent excessive polling
