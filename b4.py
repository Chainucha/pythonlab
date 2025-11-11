"""B4. Write a GUI program to implement Simple Calculator.(+,-,*,/,%,DOT) user
proper validations."""

from tkinter import *


def button_click(value):
    current = display.get()
    display.delete(0, END)
    display.insert(END, current + str(value))


def button_clear():
    display.delete(0, END)


def button_equal():
    try:
        expr = display.get()
        if not expr:
            return
        result = eval(expr)
        display.delete(0, END)
        display.insert(END, result)
    except ZeroDivisionError:
        display.delete(0, END)
        display.insert(END, "Error: Division by 0")
    except Exception:
        display.delete(0, END)
        display.insert(END, "Invalid Input")


window = Tk()
window.title("Calculator")
window.geometry("400x600")
display = Entry(window, justify=RIGHT, bd=5)
display.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

button = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("%", 4, 2),
    ("+", 4, 3),
]

for text, row, col in button:
    Button(
        window,
        text=text,
        command=lambda val=text: button_click(val),
        bd=3,
    ).grid(row=row, column=col, sticky="nsew")

Button(window, text="=", bd=3, command=button_equal).grid(
    row=5, column=2, columnspan=2, sticky="nsew"
)

Button(window, text="C", bd=3, command=button_clear).grid(
    row=5, column=0, columnspan=2, sticky="nsew"
)

# --- Make columns/rows expand equally ---
for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(6):
    window.rowconfigure(i, weight=1)

window.mainloop()
