import machine
import utime

# Configure UART
uart = machine.UART(0, baudrate=9600, bits=8, parity=None, stop=1, tx=0, rx=1)

# Send data to the Teensy
uart.write("Hello Teensy!")

while True:
    # Additional code or operations
    utime.sleep(1)
