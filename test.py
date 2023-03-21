import tkinter
import customtkinter

# Theme stuff
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, darka
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


# init
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("750x300")
app.title("Pulse Step FTIMS")



