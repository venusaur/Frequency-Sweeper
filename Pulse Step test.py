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
import tkinter as tk
from tkinter.filedialog import asksaveasfile


#--------------------------------------#
        #Graphical Interface#
#--------------------------------------#
# Create an instance of tkinter frame or window
window = tk.Tk()

# Set the size of the tkinter window
window.geometry("700x350")

tk.Label(window, text="Starting Frequency: ", font=('Calibri 10')).pack()
startFreq = tk.Entry(window, width=35)
startFreq.pack()

tk.Label(window, text="Ending Frequency: ", font=('Calibri 10')).pack()
endFreq = tk.Entry(window, width=35)
endFreq.pack()

tk.Label(window, text="Frequency Step: ", font=('Calibri 10')).pack()
freqStep = tk.Entry(window, width=35)
freqStep.pack()

tk.Label(window, text="Frequency Step: ", font=('Calibri 10')).pack()
freqStep = tk.Entry(window, width=35)
freqStep.pack()

tk.Label(window, text="Averages: ", font=('Calibri 10')).pack()
average = tk.Entry(window, width=35)
average.pack()

tk.Label(window, text="Number of Points: ", font=('Calibri 10')).pack()
numP = tk.Entry(window, width=35)
numP.pack()


#--------------------------------------#
                #User inputs#
#--------------------------------------#
startfreq = int(float(startFreq.get()))          # Starting Frequency
endfreq = int(endFreq.get())              # Ending Frequency
freqstep = int(freqStep.get())            # Steps in frequency between scans

averages = int(average.get())             # Number of averages at each frequency step - SOFTWARE WILL USE THIS VALUE TO CALCULATE TIME REQUIRED AT LOWEST FREQUENCY USE THE TRIGGER TO AVERAGE THIS SAME AMOUNT OF TIME AT EACH STEP
numpts = int(numP.get())                  # Number of data points to take at each frequency setp


#--------------------------------------#
        #Background Calculations#
#--------------------------------------#
endfreq = endfreq + freqstep            #Corrects for numpy arange's inability to iterate to a number (otherwise it would stop 1 freqstep below the end freq)
samprate = (numpts*startfreq)*averages  #Calculates the sampling rate based on averges, startfreq, and numpts
numptstot = numpts*averages             #Calculates how many points to take after trigger

data = np.empty([numptstot,(endfreq-startfreq)])
names = ['Frequency %d' % (startfreq)]

for x in np.arange (1, ((endfreq-startfreq)), freqstep):
    names.append("Frequency %d" % (x+startfreq))

data = pd.DataFrame(data, columns = names)  #Initializes DataFrame for collecting data. DataFrame at this point is arranged with 1 column per frequency to be stepped.

#--------------------------------------#
        #DAQmx Initialization#
#--------------------------------------#

CO1 = nidaqmx.Task()    #Initializes Counter Output
CO1.co_channels.add_co_pulse_chan_time("Dev1/ctr0")
CO1.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
cw = CounterWriter(CO1.out_stream, True)

CO1.start()     #Starts Counter

AI1 = nidaqmx.Task()    #Initializes Analog Input on Channel 0 (Differential measurement)
AI1.ai_channels.add_ai_voltage_chan("Dev1/ai0")
AI1.timing.cfg_samp_clk_timing(samprate, sample_mode=AcquisitionType.FINITE, samps_per_chan = numptstot)    #Sets timing to collect total number of points requested
AI1.triggers.start_trigger.cfg_dig_edge_start_trig("PFI12") #Sets triggering to counter output - WILL ONLY TRIGGER FOR INITIAL AQUISITION; WILL COLLECT DATA THROUGHOUT PULSING AT EACH FREQSTEP

#--------------------------------------#
        #DAQmx Data Collection#
#--------------------------------------#
starttime = datetime.datetime.now()
print(starttime)
for x in np.arange (startfreq, endfreq, freqstep):  # Iterates over each frequency to collect, collecting numptstot at each step after triggering
    cw.write_one_sample_pulse_frequency(frequency=x, duty_cycle=0.5)
    print(x)
    data['Frequency %d' %(x)] = AI1.read(number_of_samples_per_channel = numptstot)
endtime = datetime.datetime.now()
print(endtime)

tottime = endtime - starttime
print(tottime)
#print(data)        #Uncomment to display raw data as collected for debugging

#Stop all DAQmx tasks to reserve device memory
CO1.stop()
CO1.close()

AI1.stop()
AI1.close()

#--------------------------------------#
        #Data Processing#
#--------------------------------------#

avg = []                # initializes empty array to store average values in.
for column in data:     # iterates over each column in the data dataframe to find average
    #print(data[column].values)
    avg.append(data[column].mean())
    #print(avg)

#print(avg)     #uncomment to display average array for debugging

output = pd.DataFrame(np.arange(startfreq, endfreq, freqstep), columns = ['Frequency']) #Creates new dataframe for the final output, populates with the frequencies tested
output['Average Signal'] = avg   #Adds average to output Dataframe

#print(output)      #Uncomment to display data in table format

#fig = plt.plot(output, output['Frequency'], output["Average Signal"]) #Plots data using default settings
#plt.show()  #Displays data


#--------------------------------------#
        #Fourier Transform#
#--------------------------------------#
fft = np.fft.fft(output["Average Signal"])

#print(fft)
t=np.arange(np.shape(fft)[0])
freq = np.fft.fftfreq(t.shape[-1])


#--------------------------------------#
        #File Output#
#--------------------------------------#
Fourier = pd.DataFrame()        #Creates Dataframe for storing all collected data and assigns each column to the respective portions of the FFT collected.
Fourier['Signal Freq']=output['Frequency']
Fourier['Signal']=output['Average Signal']
Fourier['Freq']=freq
Fourier['fft']=fft.real
Fourier['fft_imag']=fft.imag

#print(Fourier)
Fourier.to_csv((asksaveasfile(initialfile = 'Untitled.csv', defaultextension='.csv', filetypes=[("CSV Files","*.csv"),("All Files", "*.*")])), sep=',',index=False, line_terminator='\n')   #Calls a file dialog box to save the data

#fig1 = plt.plot(freq, fft.real, freq, fft.imag)
#plt.show()

window.mainloop()
