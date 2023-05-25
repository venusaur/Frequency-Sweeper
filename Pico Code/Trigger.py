import machine
import time

LED_PIN = machine.Pin(machine.LED)
TRIGGER_PIN = machine.Pin(16, machine.Pin.OUT)
INPUT_PIN = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

sweep_started = False

@INPUT_PIN.irq(trigger=machine.Pin.IRQ_RISING)
def trigger_callback(pin):
    global sweep_started
    sweep_started = True

while True:
    if sweep_started:
        # Generate trigger pulse
        TRIGGER_PIN.value(1)
        time.sleep(0.001)  # Adjust the duration of the trigger pulse if needed
        TRIGGER_PIN.value(0)

        # Perform the frequency sweep
        print("Frequency sweep triggered!")
        # Perform your desired actions here...

        sweep_started = False

    # Do other tasks...
