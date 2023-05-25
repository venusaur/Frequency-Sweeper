import machine
import time
import csv

# Data Collection
SAMPLING_TIME = 5  # Sampling time in seconds
CSV_FILE = 'analog_data.csv'  # CSV file name
data = []; #Data Array

# Analog In
adc = machine.ADC(ANALOG_PIN)
adc.atten(machine.ADC.ATTN_11DB)  # Set ADC input attenuation to 11dB

# Define Pins
TRIGGER_PIN = machine.Pin(16, machine.Pin.OUT)

def collect_analog_data():
    samples = []
    start_time = time.time()

    # compares the elapsed time time to the set sampling time 
    while time.time() - start_time < SAMPLING_TIME:
        samples.append(adc.get())  # Read analog value
        time.sleep(0.01) 
    
    return samples
 
def save_to_csv(samples):
    with open(CSV_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Sample', 'Value'])
        
        for i, value in enumerate(samples):
            writer.writerow([i+1, value]) 
 
while True:
    TRIGGER_PIN.value(1)
    collect_analog_data()
    time.sleep(.05)
    TRIGGER_PIN.value(0)

    
    
   
        