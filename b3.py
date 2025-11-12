"""B3. Create a GUI to input Principal amount, rate of interest and number of years,
Calculate Compound interest. When button submit is pressed, Compound interest
should be displayed in a textbox. When clear button is pressed, all contents should
be cleared.
"""

import tkinter as tk  # Import tkinter library for GUI creation

# ---------------------- Function Definitions ----------------------


def clear_content():
    """Clears all input and output fields."""
    principal_entry.delete(0, tk.END)  # Clear the principal entry box
    interest_rate_entry.delete(0, tk.END)  # Clear the interest rate entry box
    years_entry.delete(0, tk.END)  # Clear the years entry box
    result_textbox.delete("1.0", tk.END)  # Clear the result textbox


def calculate_interest():
    """Calculates the compound interest and displays it."""
    try:
        # Get input values from entry boxes (strings → float conversion)
        principal = float(principal_entry.get())
        interest_rate = (
            float(interest_rate_entry.get()) / 100
        )  # Convert percentage to decimal
        years = float(years_entry.get())
    except ValueError:
        # If invalid data entered (e.g., text instead of number)
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, "Please enter proper numeric values.")
        return

    # ---- Main Compound Interest Formula ----
    # CI = P * (1 + r)^t - P
    result = principal * (1 + interest_rate) ** years - principal

    # Clear previous result and display new result
    result_textbox.delete("1.0", tk.END)
    result_textbox.insert(
        tk.END, f"Compound Interest\nfor {years} years: ₹{result:.2f}"
    )


# ---------------------- GUI Layout ----------------------

# Create main window
window = tk.Tk()
window.title("Compound Interest Calculator")  # Window title
window.geometry("400x250")  # Optional: set window size

# Create labels for user input
principal_label = tk.Label(window, text="Principal Amount:")
interest_rate_label = tk.Label(window, text="Interest Rate (%):")
years_label = tk.Label(window, text="Years:")

# Create entry boxes for user input
principal_entry = tk.Entry(window)
interest_rate_entry = tk.Entry(window)
years_entry = tk.Entry(window)

# Create buttons for Calculate and Clear actions
calculate_btn = tk.Button(window, text="Calculate", command=calculate_interest)
clear_btn = tk.Button(window, text="Clear", command=clear_content)

# Create a textbox to show the result
result_textbox = tk.Text(window, height=2, width=30, bd=5)

# ---------------------- Arrange Components using Grid ----------------------

# Labels (left column)
principal_label.grid(column=0, row=0, padx=10, pady=5, sticky="w")
interest_rate_label.grid(column=0, row=1, padx=10, pady=5, sticky="w")
years_label.grid(column=0, row=2, padx=10, pady=5, sticky="w")

# Entry boxes (right column)
principal_entry.grid(column=1, row=0, padx=10, pady=5)
interest_rate_entry.grid(column=1, row=1, padx=10, pady=5)
years_entry.grid(column=1, row=2, padx=10, pady=5)

# Buttons (below entries)
calculate_btn.grid(column=0, row=3, padx=10, pady=10)
clear_btn.grid(column=1, row=3, padx=10, pady=10)

# Result textbox (bottom, spanning both columns)
result_textbox.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Start the Tkinter main event loop
window.mainloop()
