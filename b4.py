"""B4. Write a GUI program to implement Simple Calculator (+, -, *, /, %, .)
Use proper validations.
"""

from tkinter import *

# --------------------- FUNCTIONS ---------------------

def button_click(value):
    """Adds the clicked button's value to the current text in the display."""
    current = display.get()              # Get current value from display (as string)
    display.delete(0, END)               # Clear display
    display.insert(END, current + str(value))  # Append new value


def button_clear():
    """Clears the display."""
    display.delete(0, END)


def button_equal():
    """Evaluates the expression and shows the result."""
    try:
        expr = display.get()             # Get expression from display
        if not expr:                     # Check if empty
            return
        result = eval(expr)              # Evaluate the mathematical expression
        display.delete(0, END)
        display.insert(END, result)      # Display result
    except ZeroDivisionError:
        # Handle division by zero separately
        display.delete(0, END)
        display.insert(END, "Error: Division by 0")
    except Exception:
        # Handle any other invalid input
        display.delete(0, END)
        display.insert(END, "Invalid Input")

# --------------------- GUI LAYOUT ---------------------

# Create the main application window
window = Tk()
window.title("Calculator")               # Set window title
window.geometry("400x600")               # Set initial window size

# Entry widget (display area)
display = Entry(window, justify=RIGHT, bd=5, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

# List of calculator buttons (text, row, column)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("%", 4, 2), ("+", 4, 3),
]

# Create all digit and operator buttons
for text, row, col in buttons:
    Button(
        window,
        text=text,                        # Text shown on button
        command=lambda val=text: button_click(val),  # Add digit/operator to display
        bd=3,
        font=("Arial", 18),
    ).grid(row=row, column=col, sticky="nsew")

# Equal (=) button
Button(
    window,
    text="=", 
    bd=3,
    font=("Arial", 18),
    command=button_equal
).grid(row=5, column=2, columnspan=2, sticky="nsew")

# Clear (C) button
Button(
    window,
    text="C", 
    bd=3,
    font=("Arial", 18),
    command=button_clear
).grid(row=5, column=0, columnspan=2, sticky="nsew")

# --------------------- RESPONSIVE GRID ---------------------

# Make all columns and rows expand equally when window is resized
for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(6):
    window.rowconfigure(i, weight=1)

# Start the Tkinter main loop
window.mainloop()
