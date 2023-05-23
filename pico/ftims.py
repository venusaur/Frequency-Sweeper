import machine
import time

I2C_SLAVE_ADDRESS = 0x12  # I2C slave address of the Teensy

i2c = machine.I2C(0)  # Create an I2C object using the default I2C peripheral (I2C0)
i2c.init(machine.I2C.MASTER)  # Set the I2C mode to master

while True:
    # Send a value of 1 to turn on the LED
    i2c.writeto(I2C_SLAVE_ADDRESS, bytes([1]))

    time.sleep(1)  # Wait for 1 second

    # Send a value of 0 to turn off the LED
    i2c.writeto(I2C_SLAVE_ADDRESS, bytes([0]))

    time.sleep(1)  # Wait for 1 second
