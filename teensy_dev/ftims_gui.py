# Need to be able to send commands to the arduino via a python UI

from tkinter import *
import serial.tools.list_ports
import time

# Window Settings
root = Tk()
root.geometry('500x500')
root.title("FTIMS Panel")


# define states for arduono functions



# Teensy Arduino Communication
teensy = serial.Serial('com3', 9600)
print("Reset Arduino")
time.sleep(3)
teensy.write(bytes('L', 'UTF-8'))



teensy.open()
root.mainloop()
