import machine
import utime

uart = machine.UART(0, baudrate=9600, tx=1, rx=0)  # Initialize UART with the appropriate pins and baudrate

while True:
    uart.write(b'1')  # Send '1' to turn on the Teensy LED
    utime.sleep(1)  # Wait for 1 second
    uart.write(b'0')  # Send '0' to turn off the Teensy LED
    utime.sleep(1)  # Wait for 1 second
