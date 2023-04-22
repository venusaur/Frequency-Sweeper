#include <ADC.h>
#include <Arduino.h>

#if defined(__IMXRT1062__)
extern "C" uint32_t set_arm_clock(uint32_t frequency);
#endif

ADC *adc = new ADC();

const int PIN = 13;

int startFreq = 1;
int startfreqv = startFreq;
int steps = 10;
int stopFreq = 100;

#define BUFFER_SIZE (1L << 8)
uint16_t buffer[BUFFER_SIZE];
uint8_t buffer_count = BUFFER_SIZE;

void freqScan(int startFreq, int stopFreq, int steps){
    while (startfreqv <= stopFreq){
        analogWriteFrequency(LED_BUILTIN, startfreqv);
        analogWrite(LED_BUILTIN, 128);
        startfreqv += steps;
        delay(2000);
    }
    startfreqv = startFreq;
}

/*
void freqScan(int startFreq, int stopFreq, int steps){
    for(int freq = startFreq; freq <= stopFreq; freq += steps){
        analogWriteFrequency(LED_BUILTIN, freq);
        analogWrite(LED_BUILTIN, 128);
        delay(2000);
    }
}
*/

void setup() {
    Serial.begin(115200);

    adc->adc0->setAveraging(4);
    adc->adc0->setResolution(12);
    adc->adc0->setConversionSpeed(ADC_CONVERSION_SPEED::HIGH_SPEED);
    adc->adc0->setSamplingSpeed(ADC_SAMPLING_SPEED::VERY_HIGH_SPEED);
    adc->adc0->startContinuous(PIN);

    set_arm_clock(1000000); // set clock speed to 1 MHz
}

void loop() {
    freqScan(startFreq, stopFreq, steps);
}

