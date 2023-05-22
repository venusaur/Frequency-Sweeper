//PROJECT NAME: FTIMS - Frequency Sweeper for Ion Mobility Spectroscopy
//CONTRIBUTORS:
//    Saned Gharari - sgharari24@my.whitworth.edu
//    Dr. Eric Davis - ericdavis@whitworth.edu

//PURPOSE: Sweeps through frequencies and stores output for a pcb ion mobility spectrometer 
//LAST UPDATED: 04.21.23
/* -------------------------------------------------------------------------------------------*/

#include <ADC.h>
#include <Arduino.h>

// Used to set teensy clock speed 
#if defined(__IMXRT1062__)
extern "C" uint32_t set_arm_clock(uint32_t frequency);
#endif

ADC *adc = new ADC(); // initialize analog-to-dig  

// Required defined pins on Teensy board
const int PIN = 13;
const int buttonPin = 4; // Need to see what pin is actually needed


// Sweeping varibles 
int startFreq = 1; // starting frequency  
int startfreqv = startFreq; // resetting counter
int steps = 10; // steps to increment frequncy scanner
int stopFreq = 500; // stop frequncy

// Additional Vars
int run = 0; 


// Buffer to store vars
// Defines a constant BUFFER_SIZE to be equal to the value of 2 to the power of 8, which is 256. 
// It then declares an array of unsigned 16-bit integers named buffer with a length of BUFFER_SIZE, or 256 elements.
// #define BUFFER_SIZE (1L << 8) 
uint16_t const BUFFER_SIZE = 10000;
uint16_t buffer[BUFFER_SIZE];
uint8_t buffer_count = BUFFER_SIZE;


// Function that sweeps and increments through frequencies on Teensy Arduino
//Input         : startFreq - starting freqency of the sweep in Hz
//              : stopFreq - ending frequency of the sweep in Hz
//              : steps - number of steps in the sweep
void freqScan(int startFreq, int stopFreq, int steps){
    while (startfreqv <= stopFreq){
        analogWriteFrequency(LED_BUILTIN, startfreqv);
        analogWrite(LED_BUILTIN, 128);
        startfreqv += steps;
        delay(2000);  
    }
    // reset loop with new starting frequncy
    startfreqv = startFreq;
}

void freqScanOutput(int startFreq, int stopFreq, int steps) {
  int currentFreq = startFreq;
  while (currentFreq <= stopFreq) {
    analogWriteFrequency(LED_BUILTIN, currentFreq);
    analogWrite(LED_BUILTIN, 128);
    Serial.print("Frequency: ");
    Serial.println(currentFreq);
    currentFreq += steps;
    delay(2000);
  }
}


void setup() {
    Serial.begin(115200);
    Serial.println("Test");
    // Setting PWM resoution 
    // ADC fast setup
    adc->adc0->setAveraging(4);
    adc->adc0->setResolution(12);
    adc->adc0->setConversionSpeed(ADC_CONVERSION_SPEED::HIGH_SPEED);
    adc->adc0->setSamplingSpeed(ADC_SAMPLING_SPEED::VERY_HIGH_SPEED);
    adc->adc0->startContinuous(PIN);

    set_arm_clock(1000000); // set clock speed to 1 MHz
}

void loop() {
  // function call
  freqScan(startFreq, stopFreq, steps);

  // Code to start / stop frequency scan
  if(digitalRead(buttonPin) == LOW){
    if(run == 0) {
      run = 255; 
    }
    else  {
      run = 0; 
    }
  }
  
  // Run Code when pressed / stopped when pressed again
  if(run > 0){
    freqScan(startFreq, stopFreq, steps); 
  }







}