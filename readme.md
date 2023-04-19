# Frequency Sweeper for Fourier Transform Ion Mobility Spectrometer
Arduino code that sweeps through frequencies on a Teensy for an ion mobility spectrometer. Allows an FTIMS instrument to analyze a wider range of molecular species with high accuracy and precision. 
## Table of Contents
- [Frequency Sweeper](#Frequency-Sweeper-for-Fourier-Transform-Ion-Mobility-Spectrometer)
	- [Table of Contents](#table-of-contents)
	- [System Requirements](#system-requirements)  
	- [Specifications](#specifications)
		- [Pseudocode](#pseudocode)
  	- [To-Do List](#todo)
  	- [Acknowledgements](#acknowledgements)

## System Requirements
- Arduino Teensy Library
- Install python requirements (Not finished)
- Teensy 4.0
<p align="center">
	<img width="60%" height="40%" src="https://github.com/venusaur/Pulsed-Step-FTIMS/blob/main/pins.png" alt="Teensy Pin Usage"/>
</p>

## Specifications
### Pseudocode
```python
    while startfreq != stopFreq {
        write startfreq
        write duty cycle
        increment frequency
        delay 
    }
    reset counter
```

## TODO
- Implement way to export data to CSV
- GUI interface via python or C# that communicates via serial
- Interface 2 Arduinos for data collection and visualization


## Acknowledgements


## References
