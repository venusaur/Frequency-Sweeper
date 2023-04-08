//PROJECT NAME: FTIMS - Frequency Sweeper for Ion Mobility Spectroscopy
//CONTRIBUTORS:
//    Saned Gharari - sgharari@whitworth.edu

//PURPOSE: Sweeps through frequencies and stores output for a pcb ion mobility spectrometer 
//References: 
//LAST UPDATED: 04.07.23


IntervalTimer timer; // https://www.pjrc.com/teensy/td_timing_IntervalTimer.html 

// Required defined pins on Teensy board
const int TX_OUTPUT = 1;
const int DAC_PIN = 14; // Teensy analog pin

// Default varibles if ones are not given
const int DEFAULT_startFreq = 1000; // default starting frequency of the sweep in Hz
const int DEFAULT_endFreq = 2000; // default ending frequency of the sweep in Hz
const int DEFAULT_sweepTime = 5000; // default duration of the sweep in milliseconds
const int DEFAULT_steps = 100; // default number of steps in the sweep

// Sweeping varibles (varibles that will be set via gui interface in future)
int startFreq = 0;
int endFreq = 0; 
int sweepTime = 0;
int steps = 0; 

/*
int startFreq = DEFAULT_startFreq;
int endFreq = DEFAULT_endFreq; 
int sweepTime = DEFAULT_sweepTime;
int steps = DEFAULT_steps = 100; 
*/


// Function that sweeps and increments through frequencies on Teensy Arduino
//Input         : startFreq - starting freqency of the sweep in Hz
//              : endFreq - ending frequency of the sweep in Hz
//              : sweepTime - duration of the sweep in milliseconds
//              : steps - number of steps in the sweep
inline void ftimsPulse(int startFreq, int endFreq, int sweepTime, int steps){
    int period = 1000000 / startFreq; // Calculate the period of the starting frequency
    int stepSize = (endFreq - startFreq) / steps; // Calculate the frequency step size
    int stepTime = sweepTime / steps; // Calculate the time for each step

    for (int i = 0; i < steps; i++) {
      digitalWrite(TX_OUTPUT, HIGH); // Set the output pin high
      delayMicroseconds(period / 2); // Wait for half of the period
      digitalWrite(TX_OUTPUT, LOW); // Set the output pin low
      delayMicroseconds(period / 2); // Wait for the other half of the period

      startFreq += stepSize; // Increment the frequency
      period = 1000000 / startFreq; // Calculate the period for the new frequency

      delay(stepTime); // Wait for the step time
    }
}
// There was a possible idea of moving the writes to the TX pin to a different function and then utilize a timer for more precise measurements



// Setup
void setup() {
  Serial.begin(115200); // Setting data rate
  pinMode(TX_OUTPUT, OUTPUT); // Setting Pin mode
  pinMode(DAC_PIN, OUTPUT); // Analog out pin

  // Setting Initial State
  digitalWrite(TX_OUTPUT, LOW);
  
  // Setting PWM resoution 
  analogWriteResolution(12);
}

// Main loop
void loop() { 
  dataStr[0] = 0; 
  


  ftimsPulse(startFreq, endFreq, sweepTime, steps);  
}

