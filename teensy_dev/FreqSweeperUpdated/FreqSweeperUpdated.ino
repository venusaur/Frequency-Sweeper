//PROJECT NAME: FTIMS - Frequency Sweeper for Ion Mobility Spectroscopy
//CONTRIBUTORS:
//    Saned Gharari - sgharari24@my.whitworth.edu
//    Dr. Eric Davis - ericdavis@whitworth.edu

//PURPOSE: Sweeps through frequencies and stores output for a pcb ion mobility spectrometer 

//References: https://github.com/kongmunist/TeensyDAQ-Fast

//LAST UPDATED: 04.18.23

#include <ADC.h>


ADC *adc = new ADC(); // initialize analog-to-dig  

// Required defined pins on Teensy board
const int PIN = 13; 
const int buttonPin = 4; // Need to see what pin is actually needed


// Default varibles if ones are not given
/*
const int DEFAULT_startFreq = 1000; // default starting frequency of the sweep in Hz
const int DEFAULT_stopFreq = 2000; // default ending frequency of the sweep in Hz
const int DEFAULT_steps = 100; // default number of steps in the sweep
*/

int startFreq = 20; // Starting frequency of the sweep in Hz
int startfreqv = startFreq; // Used to reset starting frequency at end of while loop
int steps = 10; // Number of steps in the sweep
int stopFreq = 120; // Ending frequency of the sweep in Hz


// Additional Vars
int averages = 4; 
int run = 0; 
bool writing = 0; 
bool clk = 0;
float mult; 
int val; 

// Defines a constant BUFFER_SIZE to be equal to the value of 2 to the power of 8, which is 256. It then declares an array of unsigned 16-bit integers named buffer with a length of BUFFER_SIZE, or 256 elements.
#define BUFFER_SIZE (1L << 8)
uint16_t buffer[BUFFER_SIZE];
uint8_t buffer_count = BUFFER_SIZE;

// Function that sweeps and increments through frequencies on Teensy Arduino
//Input         : startFreq - starting freqency of the sweep in Hz
//              : stopFreq - ending frequency of the sweep in Hz
//              : steps - number of steps in the sweep
void freqScan(int startFreq, int stopFreq, int steps){
    while (startfreqv != stopFreq){
      analogWriteFrequency(LED_BUILTIN, startfreqv); // 
      analogWrite(LED_BUILTIN, 128); // 
      startfreqv += steps; //
      delay(2000); // 
    }
  startfreqv = startFreq;
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(1152000); // Setting data rate
  // pinMode(LED_BUILTIN, OUTPUT); 
  pinMode(LED_BUILTIN, INPUT); 
  pinMode(10, OUTPUT); 

  // Setting PWM resoution 
  // ADC fast setup
  adc->adc0->setAveraging(averages);
  adc->adc0->setResolution(12);
  adc->adc0->setConversionSpeed(ADC_CONVERSION_SPEED::HIGH_SPEED);
  adc->adc0->setSamplingSpeed(ADC_SAMPLING_SPEED::VERY_HIGH_SPEED);
  adc->adc0->startContinuous(PIN);
  


  // Calculates a floating-point value mult based on the maximum value that can be read from an analog-to-digital converter (ADC) connected to an Arduino or similar microcontroller.
  mult = 33000.0/adc->adc0->getMaxValue();   
}


void loop() {
  // put your main code here, to run repeatedlyz
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

  if(Serial.available()){
    while(Serial.available()){
        Serial.read(); 
      }

      clk = 0;
      digitalWriteFast(10, clk);
  }
  
   // Keep adding until overflow. Then we know the buffer is full
    // while (buffer_count){ 
      if (adc->adc0->isComplete() && writing){
        val = (uint16_t)adc->adc0->analogReadContinuous();
        // Serial.write(val);
        Serial.println(val);

        digitalWriteFast(10,!clk);
        clk = !clk;
      }
 
}
