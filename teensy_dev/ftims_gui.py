# Need to be able to send commands to the arduino via a python UI
from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
import time as time
import numpy as np
import re
import csv
import struct

# Window Settings
root = Tk()
root.geometry('500x500')
root.title("FTIMS Panel")

input_freq_start = input("Enter starting frequency: ") # input Frequencies
input_freq_stop = input("Enter stopping frequency: ")
input_freq_step = input("Enter frequency stepsize: ")









# define states for teensy functions



# Teensy Arduino Communication
teensy = serial.Serial('com3', 9600) # Adjust for COM port and speed of teensy
print("Reset Arduino") # debug Sstatement
teensy.flushInput() # Flush input buffer
teensy.write(bytes('L', 'UTF-8'))



#teensy.open()
root.mainloop()
