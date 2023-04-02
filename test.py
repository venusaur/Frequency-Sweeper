#--------------------------------------#
                #IMPORTS#
#--------------------------------------#
import nidaqmx
from nidaqmx.stream_writers import CounterWriter
from nidaqmx.constants import AcquisitionType
import datetime
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import tkinter
import customtkinter

#--------------------------------------#
        #Graphical Interface#
#--------------------------------------#
# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Frame intialization
frame = customtkinter.CTk()
frame.geometry("750x300")
frame.title("Pulse Step FTIMS")


# UI Elements
startFreq = customtkinter.CTkLabel(frame, text="Starting Freq.")
startFreq.grid(row=0, column=0, padx=10)

startFreq = customtkinter.CTkLabel(frame, text="Starting Freq.", justify="left")
startFreq.grid(row=0, column=0, padx=10)

endFreq = customtkinter.CTkLabel(frame, text="End Freq.", justify="left")
endFreq.grid(row=1, column=0, padx=10)

freqStep = customtkinter.CTkLabel(frame, text="Frequency Step", justify="left")
freqStep.grid(row=2, column=0, padx=10)

setAvg = customtkinter.CTkLabel(frame, text="Averages", justify="left")
setAvg.grid(row=3, column=0, padx=10)

setPoints = customtkinter.CTkLabel(frame, text="Number of Points", justify="left")
setPoints.grid(row=4, column=0, padx=10)



# UI input
startFreqInput = customtkinter.CTkEntry(frame, width=100, height=30)
startFreqInput.grid(row=0, column=1, pady=10)

endFreqInput = customtkinter.CTkEntry(frame, width=100, height=30)
endFreqInput.grid(row=1, column=1, pady=10)

freqStepInput = customtkinter.CTkEntry(frame, width=100, height=30)
freqStepInput.grid(row=2, column=1, pady=10)

setAvgInput = customtkinter.CTkEntry(frame, width=100, height=30)
setAvgInput.grid(row=3, column=1, pady=10)

setPointsInput = customtkinter.CTkEntry(frame, width=100, height=30)
setPointsInput.grid(row=4, column=1, pady=10)


#--------------------------------------#
                #User inputs#
#--------------------------------------#
startfreq = int(startFreqInput.get())  
endfreq = int(endFreqInput.get())
freqstep = int(freqStepInput.get())
averages = int(setAvgInput.get())
numpts = int(setPointsInput.get())


#--------------------------------------#
        #Background Calculations#
#--------------------------------------#
endfreq += freqstep
samprate = (numpts*startFreq)*averages # Might want to display this value later
numptsTot = numpts*averages # Might want to display this value aswell

data = np.empty([numptsTot,(endfreq-startfreq)])
names = ['Frequency %d' % (startfreq)]

for x in np.arange (1, ((endfreq-startfreq)), freqstep):
    names.append("Frequency %d" % (x+startfreq))         # Can I add a prgress bar for this in UI

data = pd.DataFrame(data, columns = names)


#--------------------------------------#
        #DAQmx Initialization#
#--------------------------------------#
CO1 = nidaqmx.Task()    #Initializes Counter Output
CO1.co_channels.add_co_pulse_chan_time("Dev1/ctr0") # This is where I want to investigate with rp\
CO1.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
cw = CounterWriter(CO1.out_stream, True)

CO1.start()     #Starts Counter

AI1 = nidaqmx.Task()    #Initializes Analog Input on Channel 0 (Differential measurement)
AI1.ai_channels.add_ai_voltage_chan("Dev1/ai0") # Investigate this as well 
AI1.timing.cfg_samp_clk_timing(samprate, sample_mode=AcquisitionType.FINITE, samps_per_chan = numptsTot)    # Sets timing to collect total number of points requested
AI1.triggers.start_trigger.cfg_dig_edge_start_trig("PFI12")


#--------------------------------------#
        #DAQmx Data Collection#
#--------------------------------------#
startTime = datetime.datetime.now() # Need to output start time

for x in np.arange (startfreq, endfreq, freqstep):  # Iterates over each frequency to collect, collecting numptstot at each step after triggering
    cw.write_one_sample_pulse_frequency(frequency=x, duty_cycle=0.5)
    print(x)
    data['Frequency %d' %(x)] = AI1.read(number_of_samples_per_channel = numptsTot)

endTime = datetime.datetime.now() # Need to output End Time

timeTot = endTime - startTime # Need to output total time

CO1.stop()
CO1.close()

AI1.stop()
AI1.close()

#--------------------------------------#
        #Data Processing#
#--------------------------------------#
avg = []                # initializes empty array to store average values in.
for column in data:     # iterates over each column in the data dataframe to find average
    avg.append(data[column].mean())
    

#print(avg)     # Might want to display this value aswell


output = pd.DataFrame(np.arange(startfreq, endfreq, freqstep), columns = ['Frequency']) #Creates new dataframe for the final output, populates with the frequencies tested
output['Average Signal'] = avg   # Output this value as well



# main loop
frame.mainloop()


