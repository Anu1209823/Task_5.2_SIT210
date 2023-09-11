# Import necessary libraries
from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
from gpiozero import LED

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Initialize GPIO pins using gpiozero
red = LED(14)
blue = LED(15)
green = LED(18)

# Initialize the GUI window
win = Tk()
win.title("GUI Interface")  # Set the title of the window
win.geometry("250x180")  # Set the window size
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")
uv = StringVar()

# Functions to control LEDs
def ledRed():
    red.on()
    blue.off()
    green.off()

def ledBlue():
    red.off()
    blue.on()
    green.off()
def ledGreen():
    red.off()
    blue.off()
    green.on()

def allOn():
    red.on()
    blue.on()
    green.on()
def allOFF():
    red.off()
    blue.off()
    green.off()

# Function to clean up GPIO and close the window
def close():
    GPIO.cleanup()
    win.destroy()
# GUI Widgets
Label(win, text="Choose an option!!", font=myFont, padx=14).pack()
Radiobutton(win, text="Red", font=myFont, command=ledRed, bg='red', height=1, width=27, bd=3, variable=uv,
            value="LED: Red").pack(anchor="w")
Radiobutton(win, text="Blue", font=myFont, command=ledBlue, bg='blue', height=1, width=27, bd=3, variable=uv,
            value="LED: Blue").pack(anchor="w")
Radiobutton(win, text="Green", font=myFont, command=ledGreen, bg='green', height=1, width=27, bd=3, variable=uv,
            value="LED: Green").pack(anchor="w")
Radiobutton(win, text="All", font=myFont, command=allOn, bg='yellow', height=1, width=27, bd=3, variable=uv,
            value="LED: All").pack(anchor="w")
Radiobutton(win, text="None", font=myFont, command=allOFF, bg='purple', height=1, width=27, bd=3, variable=uv,
            value="LED: None").pack(anchor="w")
Button(win, text="Exit", font=myFont, command=close, bg='grey').pack(anchor="w")

# Define a protocol to handle window close button
win.protocol("WM_DELETE_WINDOW", close)

# Start the GUI main loop
win.mainloop()
