import tkinter
import customtkinter

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
startFreq.grid(row=0, column=0, padx=1)

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



# main loop
frame.mainloop()


