from machine import Pin
import utime

LED = Pin(11, Pin.OUT)
LED2 = Pin(25, Pin.OUT)

while True:
    if LED.value() == 1:
        LED.on() # Turn on Teensy LED
        LED2.on()
    else:
        LED.off() # Turn on Teensy LED
        LED2.off()
    
    utime.sleep(0.1)  # Delay for stability