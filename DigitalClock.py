#imports the Tk and Label classes from the tkinter module, 
# which provides a set of tools for building GUIs in Python.
from tkinter import Tk, Label
import time

#creates a new Tk object, which represents the main window of the GUI
master = Tk()

#sets the title of the window to "My Digital Clock
master.title("My Digital Clock")

#formats a time tuple
def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    #sets the text of the clock label to the current time
    clock.config(text=timeVar)
    #to be called again after 200 milliseconds (loop)
    clock.after(200, get_time)

#object with a specified font, background color, and foreground (text) color
clock = Label(master, font=("Roboto", 90), bg="#010101", fg="#03A062")

#RESPONSIVENESS:
#places the clock label in the first row and first column of the grid 
# and makes it expand to fill the available space in both the vertical and horizontal directions
clock.grid(row=0, column=0, sticky="nsew")

#specify the layout of the GUI using a grid of rows and columns
clock.grid()
# configure the first row and first column of the grid to have a weight of 1, 
# which means that they will expand to fill the available space in both the vertical 
# and horizontal directions as the window is resized
master.grid_rowconfigure(0, weight=1)
#specifies how the widget should align within its cell. 
# "nsew" means that the widget should expand in all four directions to fill the available space
master.grid_columnconfigure(0, weight=1)

#called once to initialize the clock label with the current time
get_time()

#starts the main event loop (input)
master.mainloop()

#colors used:
#matrix green - #03A062
#binary black - #010101