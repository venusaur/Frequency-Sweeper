from machine import Pin
import utime

input_pin = Pin(20, Pin.IN)
output_pin_teensy = Pin(13, Pin.OUT)

while True:
    if input_pin.value() == 1:
        output_pin_teensy.on()  # Turn on Teensy LED
    else:
        output_pin_teensy.off()  # Turn off Teensy LED
    utime.sleep(0.1)  # Delay for stability
