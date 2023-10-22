# Import necessary libraries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

# Set the GPIO mode to BCM
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Initialize LED objects for Red, White, and Green LEDs
Red = LED(16)
White = LED(20)
Green = LED(21)

# Create a Tkinter window
win = Tk()
win.title("LED BLINK")
myFont = tkinter.font.Font(family='Arial', size=12, weight="bold")

# Variable to store the selected LED color
selected_color = StringVar()

# LED Control Functions

# Function to control the LEDs based on the selected color
def control_led():
    color = selected_color.get()
    if color == "Red":
        if Red.is_lit:
            Red.off()
        else:
            Red.on()
            White.off()
            Green.off()
    elif color == "White":
        if White.is_lit:
            White.off()
        else:
            White on()
            Red off()
            Green off()
    elif color == "Green":
        if Green.is_lit:
            Green off()
        else:
            Green.on()
            Red.off()
            White.off()

# Code for EXIT
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Create radio buttons for selecting LED colors

redRadio = Radiobutton(win, text="Red LED", variable=selected_color, value="Red", font=myFont, command=control_led)
redRadio.grid(row=0, column=1)

whiteRadio = Radiobutton(win, text="White LED", variable=selected_color, value="White", font=myFont, command=control_led)
whiteRadio.grid(row=0, column=3)

greenRadio = Radiobutton(win, text="Green LED", variable=selected_color, value="Green", font=myFont, command=control_led)
greenRadio.grid(row=0, column=6)

# Create an "EXIT" button

exitButton = Button(win, text="EXIT WINDOW", font=myFont, command=close, bg='red')
exitButton.grid(row=2, column=3)

# Set up an action to handle window close event
win.protocol("WM_DELETE_WINDOW", close)

# Start the Tkinter main event loop
win.mainloop()
