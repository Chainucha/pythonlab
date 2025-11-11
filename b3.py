"""B3. Create a GUI to input Principal amount, rate of interest and number of years,
Calculate Compound interest. When button submit is pressed Compound interest
should be displayed in a textbox. When clear button is pressed all contents should
be cleared."""

import tkinter as tk


def clear_content():
    principal_entry.delete(0, tk.END)
    interest_rate_entry.delete(0, tk.END)
    years_entry.delete(0, tk.END)
    result_textbox.delete("1.0", tk.END)


def calculate_interest():
    try:
        principal = float(principal_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100
        years = float(years_entry.get())
    except ValueError:
        result_textbox.insert(tk.END, "Please enter proper values")
        return
    result = principal * (1 + interest_rate) ** years - principal
    result_textbox.delete("1.0", tk.END)
    result_textbox.insert(tk.END, f"Compound interest \nof {years} : {result:.2f}")


window = tk.Tk()

principal_label = tk.Label(window, text="Principal :")
interest_rate_label = tk.Label(window, text="Interest rate : ")
years_label = tk.Label(window, text="Year :")

result_textbox = tk.Text(window, height=2, width=25, bd=5)

principal_entry = tk.Entry(window)
interest_rate_entry = tk.Entry(window)
years_entry = tk.Entry(window)

calculate_btn = tk.Button(window, text="Calculate", command=calculate_interest)
clear_btn = tk.Button(window, text="Clear", command=clear_content)

principal_label.grid(column=0, row=0)
interest_rate_label.grid(column=0, row=1)
years_label.grid(column=0, row=2)

principal_entry.grid(column=1, row=0)
interest_rate_entry.grid(column=1, row=1)
years_entry.grid(column=1, row=2)

calculate_btn.grid(column=0, row=3)
clear_btn.grid(column=1, row=3)

result_textbox.grid(column=0, row=4, columnspan=2)

window.mainloop()
