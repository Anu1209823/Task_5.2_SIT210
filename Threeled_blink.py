# Import necessary libraries
from tkinter import *  # Import the Tkinter library for creating the GUI
import tkinter.font  # Import the font module from tkinter for text styling
from gpiozero import LED  # Import the LED module from gpiozero for controlling LEDs
import RPi.GPIO  # Import the RPi.GPIO module for working with Raspberry Pi GPIO pins

# Set the GPIO mode to BCM
RPi.GPIO.setmode(RPi.GPIO.BCM)  # Set the GPIO numbering mode to BCM (Broadcom SOC channel numbering)

# Initialize LED objects for Red, White, and Green LEDs
Red = LED(16)  # Initialize an LED object for the Red LED on GPIO pin 16
White = LED(20)  # Initialize an LED object for the White LED on GPIO pin 20
Green = LED(21)  # Initialize an LED object for the Green LED on GPIO pin 21

# Create a Tkinter window
win = Tk()  # Create a main Tkinter window

win.title("LED BLINK")  # Set the title of the window to "LED BLINK"
myFont = tkinter.font.Font(family='Arial', size=12, weight="bold")  # Define a font style

# Variable to store the selected LED color
selected_color = StringVar()  # Create a StringVar to store the selected LED color

# LED Control Functions

# Function to control the LEDs based on the selected color
def control_led():
    color = selected_color.get()  # Get the selected LED color from the StringVar
    if color == "Red":
        if Red.is_lit:
            Red.off()  # Turn off the Red LED if it is lit
        else:
            Red.on()  # Turn on the Red LED if it is not lit
            White.off()  # Turn off the White LED
            Green.off()  # Turn off the Green LED
    elif color == "White":
        if White.is_lit:
            White.off()  # Turn off the White LED if it is lit
        else:
            White.on()  # Turn on the White LED if it is not lit
            Red.off()  # Turn off the Red LED
            Green.off()  # Turn off the Green LED
    elif color == "Green":
        if Green.is_lit:
            Green.off()  # Turn off the Green LED if it is lit
        else:
            Green.on()  # Turn on the Green LED if it is not lit
            Red.off()  # Turn off the Red LED
            White.off()  # Turn off the White LED

# Code for EXIT
def close():
    RPi.GPIO.cleanup()  # Clean up the GPIO configuration
    win.destroy()  # Close the Tkinter window

# Create radio buttons for selecting LED colors

redRadio = Radiobutton(win, text="Red LED", variable=selected_color, value="Red", font=myFont, command=control_led)
redRadio.grid(row=0, column=1)  # Create a radio button for the Red LED and place it in the window

whiteRadio = Radiobutton(win, text="White LED", variable=selected_color, value="White", font=myFont, command=control_led)
whiteRadio.grid(row=0, column=3)  # Create a radio button for the White LED and place it in the window

greenRadio = Radiobutton(win, text="Green LED", variable=selected_color, value="Green", font=myFont, command=control_led)
greenRadio.grid(row=0, column=6)  # Create a radio button for the Green LED and place it in the window

# Create an "EXIT" button

exitButton = Button(win, text="EXIT WINDOW", font=myFont, command=close, bg='red')  # Create an exit button
exitButton.grid(row=2, column=3)  # Place the exit button in the window

# Set up an action to handle window close event
win.protocol("WM_DELETE_WINDOW", close)  # Define a function to handle the window close event

# Start the Tkinter main event loop
win.mainloop()  # Start the Tkinter main event loop to display the GUI and handle user interactions
