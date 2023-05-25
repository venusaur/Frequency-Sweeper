import time
from machine import Pin

# overclock
machine.freq(270000000)


# Setting values
startFreq = 5
endFreq = 1000
steps = 5
numpts = int((endFreq - startFreq) / steps)
point = 0
pulseInterval = 0
setFreq = 0

# Pins
TX_OUTPUT = 14
interruptPin = 9
LED = 25

TX_OUTPUT_PIN = Pin(TX_OUTPUT, Pin.OUT)
interruptPin_PIN = Pin(interruptPin, Pin.IN, Pin.PULL_DOWN)
LED_PIN = Pin(LED, Pin.OUT)


def constantTimeFreqSweep(setFreq):
    pulseInterval = (1 / setFreq) / 2
    # delay(500)
    LED_PIN.on()
    while interruptPin_PIN.value() == 1:
        TX_OUTPUT_PIN.on()
        time.sleep(pulseInterval)  # 50% duty cycle
        TX_OUTPUT_PIN.off()
        time.sleep(pulseInterval)  # Delay for the remaining half of the pulse interval
    time.sleep(.05)
    LED_PIN.off()


while True:
    if interruptPin_PIN.value() == 1:
        setFreq = startFreq + point * steps
        constantTimeFreqSweep(setFreq)
        point += 1

