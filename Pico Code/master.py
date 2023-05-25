import machine


startFreq = 5
endFreq = 1000
steps = 5
point = 0
pulseInterval = 0
setFreq = 0

OUTPUT = machine.Pin(14, machine.Pin.OUT)
interruptPin = machine.Pin(9, machine.Pin.OUT, machine.Pin.PULL_DOWN)
LED = Pin(25, Pin.OUT)

def switchFreqSweep(setFreq):
    pulseInterval = (1/setFreq) / 2
    LED.value(1)

    while interruptPin.value() == 1:
        OUTPUT.value(1)
        time.sleep(pulseInterval * 1000)
        OUTPUT.value(0)
        time.sleep(pulseInterval * 1000)
    
    LED.value(0)

while True:
    if interruptPin.value() == 1:
        setFreq = startFreq + point * steps
        switchFreqSweep(setFreq)
        point += 1 


