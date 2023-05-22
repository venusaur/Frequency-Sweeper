import machine
import utime

uart = machine.UART(0, baudrate=9600, bits=8, parity=None, stop=1)  # Initialize UART

while True:
    command = b'1'  # Command to turn on the LED
    uart.write(command)  # Send the command over UART
    utime.sleep_ms(1000)  # Wait for 1 second
    command = b'0'  # Command to turn off the LED
    uart.write(command)  # Send the command over UART
    utime.sleep_ms(1000)  # Wait for 1 second
