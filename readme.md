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
	<img width="40%" height="30%" src="https://github.com/venusaur/Pulsed-Step-FTIMS/blob/main/pins.png" alt="Teensy Pin Usage"/>
</p>

## Specifications
### Pseudocode
```python
for i in sweeps
	write high for output pin
	pause
	write low for output pin
	pause
	
	increment freq
	calc new period 
	
	pause
```

## TODO
- Implement way to export data to CSV
- GUI interface via python or C# that communicates via serial
- Test arduino code with traditional IMS 
- Attempt to implement hardware timing instead of software timed code


## Acknowledgements



## References
