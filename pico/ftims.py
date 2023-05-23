import machine
import utime

uart = machine.UART(0, baudrate=9600, tx=1, rx=0)  # Initialize UART with the appropriate pins and baudrate

while True:
    if machine.Pin(20).value() == 1:
        uart.write(b'1')  # Send '1' to the Teensy
    else:
        uart.write(b'0')  # Send '0' to the Teensy
    utime.sleep(0.1)  # Delay for stability
