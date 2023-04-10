# Frequency Sweeper for Fourier Transform Ion Mobility Spectrometer

## Table of Contents
- [Frequency Sweeper](#)
	- [Table of Contents](#table-of-contents)
	- [What is this?](#what-is-this)
	- [System Requirements](#system-requirements)  
	- [Specifications](#specifications)
		- [Pseudocode](#pseudocode)
  	- [Development notes](#development-notes)
  	- [Acknowledgements](#acknowledgements)

## What is this?
The purpose of this project is to sweep through frequencies on an ion mobility spectrometer. By sweeping frequencies over a range of values, the FTIMS instrument can analyze a wide range of molecular species with high accuracy and precision. 

## System Requirements
- Teensy 4.0
- Arduino Library
- Install python requirements (Not finished)

[Add labeled image of Teensy board with pins used]

## Specification
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
- GUI interface via python or C# that communicates via serial
- Test arduino code with traditional IMS 
- Attempt to implement hardware timing instead of software timed code


## Acknowledgements



## References
