# Need to be able to send commands to the arduino via a python UI

from tkinter import *
import serial.tools.list_ports
import time

# Window Settings
root = Tk()
root.geometry('500x500')
root.title("FTIMS Panel")

# Teensy Arduino Communication
teensy = serial.Serial("COM4", 9600)
teensy.flushInput()
ser.write((startFreq+';'+endFreq+';'+sweepTime+';'steps+';'\n').encode())

data = ''


# define states for arrduino functions
def process(startFreq, endFreq, sweepTime, steps):


teensy.open()
root.mainloop()
