import machine
import utime

I2C_SLAVE_ADDRESS = 0x12  # I2C slave address of the Teensy

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0), freq=400000)  # Create an I2C object with the appropriate pins and frequency

while True:
    # Send a value of 1 to turn on the LED
    i2c.writeto(I2C_SLAVE_ADDRESS, bytes([1]))

    utime.sleep(1)  # Wait for 1 second

    # Send a value of 0 to turn off the LED
    i2c.writeto(I2C_SLAVE_ADDRESS, bytes([0]))

    utime.sleep(1)  # Wait for 1 second
