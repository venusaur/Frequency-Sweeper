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

# Teensy Arduino Communication
teensy = serial.Serial("COM4", 9600)
teensy.flushInput()
#teensy.write((startFreq+';'+endFreq+';'+sweepTime+';'steps+';'\n').encode()) // tbh idk

data = ''


# define states for arrduino functions
def process(startFreq, endFreq, sweepTime, steps):


#teensy.open()
    root.mainloop()
