
// Default varibles if ones are not given
const float DEFAULT_startFreq = 5; // default starting frequency of the sweep in Hz
const float DEFAULT_endFreq = 1000; // default ending frequency of the sweep in Hz
const int DEFAULT_steps = 5; // default number of steps in the sweep

// Setting Values
int startFreq = DEFAULT_startFreq;
int endFreq = DEFAULT_endFreq; 
int steps = DEFAULT_steps;
int numpts = (endFreq-startFreq)/steps;
int point = 0;
float pulseInterval = 0;
float setFreq = 0;


// Pins
const int TX_OUTPUT = 14;
const int interruptPin = 9;
const int LED = 13;



void constantTimeFreqSweep(float setFreq){
    pulseInterval = (1/setFreq)/2;
    //delay(500);
    digitalWrite(LED, HIGH);
      while  (digitalRead(interruptPin) == HIGH) {
        digitalWrite(TX_OUTPUT, HIGH);
        delay(pulseInterval*1000);  // 50% duty cycle
        digitalWrite(TX_OUTPUT, LOW);
        delay(pulseInterval*1000);  // Delay for the remaining half of the pulse interval
      }
      //delay(500);
    digitalWrite(LED, LOW);
  }

void setup() {
    pinMode(TX_OUTPUT, OUTPUT);
    pinMode(interruptPin, INPUT_PULLDOWN);
    pinMode(LED, OUTPUT);
  }


// Falling edge trigger
void loop() {
    if (digitalRead(interruptPin) == HIGH) {
      setFreq = startFreq + point*steps;
      constantTimeFreqSweep(setFreq);
      point++;
    } 
}

