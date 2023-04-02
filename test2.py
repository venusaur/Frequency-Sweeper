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
from tkinter import *
from functions import *


#--------------------------------------#
        #Graphical Interface#
#--------------------------------------#
root = Tk()
root.geometry('500x500')
root.title("FTIMS Panel")


# Labels for Variables
startFreqLabel = Label(root, text="Starting Freq.")
startFreqLabel.grid(row=0, column=0, padx=10)

endFreqLabel = Label(root, text="End Freq.", justify="left")
endFreqLabel.grid(row=1, column=0, padx=10)

freqStepLabel = Label(root, text="Frequency Step", justify="left")
freqStepLabel.grid(row=2, column=0, padx=10)

setAvgLabel = Label(root, text="Averages", justify="left")
setAvgLabel.grid(row=3, column=0, padx=10)

setPointsLabel = Label(root, text="Number of Points", justify="left")
setPointsLabel.grid(row=4, column=0, padx=10)



# UI Input
startFreqInput = Entry(root, width=10)
startFreqInput.grid(row=0, column=1, pady=10)

endFreqInput = Entry(root, width=10)
endFreqInput.grid(row=1, column=1, pady=10)

freqStepInput = Entry(root, width=10)
freqStepInput.grid(row=2, column=1, pady=10)

setAvgInput = Entry(root, width=10)
setAvgInput.grid(row=3, column=1, pady=10)

setPointsInput = Entry(root, width=10)
setPointsInput.grid(row=4, column=1, pady=10)



#--------------------------------------#
                #User inputs#
#--------------------------------------#
startfreq = int(startFreqInput.get())
print(startfreq) # Debug statement

endfreq = int(endFreqInput.get())
print(endfreq) # Debug Statment

freqstep = int (freqStepInput.get())
print(freqstep) # Debug Statement

averages = int(setAvgInput.get())
print(averages) #Debug statment

numpts = int(setPointsInput.get())
print(numpts) #debug statment

runButton = Button(root, text="RUN SCAN")
runButton.grid(row=2, column=5, padx=50)

print(startfreq)





#--------------------------------------#
        #Background Calculations#
#--------------------------------------#
endfreq += freqstep
samprate = (numpts*startfreq)*averages # Might want to display this value later
numptTot = numpts*averages # Might want to display this value aswell

data = np.empty([numptTot,(endfreq-startfreq)])
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
AI1.timing.cfg_samp_clk_timing(samprate, sample_mode=AcquisitionType.FINITE, samps_per_chan = numptTot)    # Sets timing to collect total number of points requested
AI1.triggers.start_trigger.cfg_dig_edge_start_trig("PFI12")


#--------------------------------------#
        #DAQmx Data Collection#
#--------------------------------------#
startTime = datetime.datetime.now() # Need to output start time

for x in np.arange (startfreq, endfreq, freqstep):  # Iterates over each frequency to collect, collecting numptstot at each step after triggering
    cw.write_one_sample_pulse_frequency(frequency=x, duty_cycle=0.5)
    print(x)
    data['Frequency %d' %(x)] = AI1.read(number_of_samples_per_channel = numptTot)

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


root.mainloop()

