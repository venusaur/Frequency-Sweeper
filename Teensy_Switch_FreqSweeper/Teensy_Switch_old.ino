#include <ADC.h>

ADC *adc = new ADC(); // initialize analog-to-dig  

// Used to set teensy clock speed 
#if defined(__IMXRT1062__)
extern "C" uint32_t set_arm_clock(uint32_t frequency);
#endif


// Default varibles if ones are not given
const float DEFAULT_startFreq = 10; // default starting frequency of the sweep in Hz
const float DEFAULT_endFreq = 1000; // default ending frequency of the sweep in Hz
const int DEFAULT_steps = 100; // default number of steps in the sweep
const float DEFAULT_timeInterval = 1.0; // Default time 1 second between pulses

// Setting Values
int startFreq = DEFAULT_startFreq;
int endFreq = DEFAULT_endFreq; 
float timeInterval = DEFAULT_timeInterval; 
int steps = DEFAULT_steps;

// Pins
const int TX_OUTPUT = 13;
const byte interruptPin = 12;
volatile bool fallingEdgeDetected = false;


void handleInterrupt() {
  fallingEdgeDetected = true;
}

void constantTimeFreqSweep(float startFreq, float endFreq, float timeInterval, int steps){
  float frequencyStep = (endFreq - startFreq) / steps;
  float pulseInterval = 1.0 / startFreq;
  int numPulses = timeInterval / pulseInterval;

  for (int i = 0; i < steps; i++) {
    float frequency = startFreq + i * frequencyStep;
    pulseInterval = 1.0 / frequency;
    numPulses = timeInterval / pulseInterval;
      
      for (int j = 0; j < numPulses; j++) {
        digitalWrite(TX_OUTPUT, HIGH);
        delayMicroseconds(pulseInterval * 500);  // s50% duty cycle
        digitalWrite(TX_OUTPUT, LOW);
      
        Serial.print("Pulse generated at frequency: ");
        Serial.println(frequency);
      
        delayMicroseconds(pulseInterval * 500);  // Delay for the remaining half of the pulse interval
      }
    }
  delay(1000);
}

void setup() {
    Serial.begin(115200);
    
    // Setting PWM resoution 
    // ADC fast setup
    adc->adc0->setAveraging(4);
    adc->adc0->setResolution(12);
    adc->adc0->setConversionSpeed(ADC_CONVERSION_SPEED::HIGH_SPEED);
    adc->adc0->setSamplingSpeed(ADC_SAMPLING_SPEED::VERY_HIGH_SPEED);
    adc->adc0->startContinuous(TX_OUTPUT);

    set_arm_clock(1000000); // set clock speed to 1 MHz

    pinMode(TX_OUTPUT, OUTPUT);
    pinMode(interruptPin, INPUT);
    attachInterrupt(digitalPinToInterrupt(interruptPin), handleInterrupt, FALLING);
  }
}

// Falling edge trigger
void loop() {
    if (fallingEdgeDetected) {
      constantTimeFreqSweep(startFreq, endFreq, timeInterval, steps); 
      fallingEdgeDetected = false;
    }
  delay(0.1); 
}

