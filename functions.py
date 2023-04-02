
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
        #Background Calculations#
#--------------------------------------#

def backgroundCalc(startfreq, endfreq, freqstep, averages, numpts): 
    endfreq += freqstep
    samprate = (numpts*startfreq)*averages # Might want to display this value later
    global numptsTot 
    numptTot = numpts*averages # Might want to display this value aswell


    data = np.empty([numptTot,(endfreq-startfreq)])
    names = ['Frequency %d' % (startfreq)]

    for x in np.arange (1, ((endfreq-startfreq)), freqstep):
        names.append("Frequency %d" % (x+startfreq))         # Can I add a prgress bar for this in UI
        print(x)
    data = pd.DataFrame(data, columns = names)


