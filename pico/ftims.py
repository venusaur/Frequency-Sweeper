import machine
import utime

# Configure SPI
spi = machine.SPI(0)
spi.init(baudrate=1000000, polarity=0, phase=0)  # Adjust the baudrate, polarity, and phase as needed

# Define CS (Chip Select) pin
cs_pin = machine.Pin(5, machine.Pin.OUT)  # Use any available GPIO pin

# Function to send and receive data
def spi_transfer(data):
    cs_pin.off()  # Activate the CS pin
    result = spi.write_readinto(data)
    cs_pin.on()  # Deactivate the CS pin
    return result

# Example usage
while True:
    data_to_send = bytearray([0x01, 0x02, 0x03])  # Example data to send
    received_data = spi_transfer(data_to_send)
    print("Received data:", received_data)
    utime.sleep(1)
