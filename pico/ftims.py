import machine
import utime

# Configure UART
uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

# Send data to the Teensy
uart.write("Hello Teensy!")

while True:
    # Additional code or operations
    utime.sleep(1)

