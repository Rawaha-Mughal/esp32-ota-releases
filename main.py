
import machine
import time

# Configure LED pin (GPIO 2 is common for built-in LED)
led = machine.Pin(2, machine.Pin.OUT)

# Blink LED with 0.2-second interval
while True:
    led.value(1)  # LED ON
    time.sleep(1)
    led.value(0)  # LED OFF
    time.sleep(1)
