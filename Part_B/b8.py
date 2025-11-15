# ---------------------- IMPORT REQUIRED LIBRARIES ----------------------
import pandas as pd  # For data handling (reading/writing CSV)
import matplotlib.pyplot as plt  # For plotting bar graphs
from tkinter import messagebox, Label, Frame, Tk, Entry, Button, END
import tkinter as tk  # For GUI elements

# ---------------------- SAMPLE MOCK DATA ----------------------
# Used for quick testing — can be written into CSV file with a button click
data = """Batmans,2017,2018,2019,2020
virat,2501,1855,2203,1223
Steve,2340,2250,2003,1153
Azam,1750,2147,1896,1008
Rohit,1463,1985,1854,1638
William,1256,1785,1874,1974"""

# The CSV file used to store or read data
file = "test.csv"


# ---------------------- FUNCTION TO DELETE ALL DATA ----------------------
def delete_data():
    """Clears all data from the CSV file."""
    try:
        with open(file, "w") as f:
            f.write("")  # Empty file
        messagebox.showinfo("Deleted", "All data deleted successfully!")
    except FileNotFoundError:
        messagebox.showerror("Error", "File does not exist.")


# ---------------------- FUNCTION TO INSERT MOCK DATA ----------------------
def mockup_data():
    """Writes pre-defined mock data into the CSV file."""
    try:
        with open(file, "w") as f:
            f.write(data.strip())
        messagebox.showinfo("Mock Data", "Mock data written successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write mock data: {e}")


# ---------------------- FUNCTION TO SAVE USER DATA ----------------------
def save_data():
    """Saves data entered by the user into the CSV file."""

    # Get all inputs from text fields
    batmans = batman_entry.get()
    y2017 = entry_2017.get()
    y2018 = entry_2018.get()
    y2019 = entry_2019.get()
    y2020 = entry_2020.get()

    # Validate all fields
    if not (batmans and y2017 and y2018 and y2019 and y2020):
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    # Create a DataFrame from user input
    data = pd.DataFrame(
        [[batmans, int(y2017), int(y2018), int(y2019), int(y2020)]],
        columns=["Batmans", "2017", "2018", "2019", "2020"],
    )

    # If file exists, append data to existing file
    try:
        exist = pd.read_csv(file)
        df = pd.concat([exist, data], ignore_index=True)
    # If file not found, create a new one
    except FileNotFoundError:
        df = data

    # Save DataFrame back to CSV
    df.to_csv(file, index=False)
    messagebox.showinfo("Success", f"Data for {batmans} saved")

    # Clear input fields
    batman_entry.delete(0, END)
    entry_2017.delete(0, END)
    entry_2018.delete(0, END)
    entry_2019.delete(0, END)
    entry_2020.delete(0, END)


# ---------------------- FUNCTION TO SHOW BAR GRAPH ----------------------
def show_graph():
    """Reads data from CSV and displays bar chart (both in terminal and GUI)."""
    try:
        df = pd.read_csv(file)
        if df.empty:
            messagebox.showwarning("No Data", "No data available to show.")
            return
    except FileNotFoundError:
        messagebox.showwarning(
            "File Error", "No data file found. Please save some data first."
        )
        return

    # Plot bar chart using pandas' built-in plot function
    df.plot(x="Batmans", kind="bar", figsize=(8, 5))

    # Customize graph labels and layout
    plt.title("Batman Performance Over Years")
    plt.xlabel("Batman")
    plt.ylabel("Performance")
    plt.tight_layout()

    # Show the graph in a separate Matplotlib window (terminal)
    plt.show()


# ---------------------- GUI SETUP SECTION ----------------------
window = Tk()
window.title("Batmans Data Entry")
window.geometry("400x600")

# Title label
Label(window, text="Enter Batmans Performance Data:", font=("Arial", 14, "bold")).pack(
    pady=10
)

# Frame to hold entry fields
frame = Frame(window)
frame.pack(pady=10)

# Labels for table headers
Label(frame, text="Batman").grid(row=0, column=0)
Label(frame, text="2017").grid(row=0, column=1)
Label(frame, text="2018").grid(row=0, column=2)
Label(frame, text="2019").grid(row=0, column=3)
Label(frame, text="2020").grid(row=0, column=4)

# Entry widgets for data input
batman_entry = Entry(frame)
entry_2017 = Entry(frame, width=5)
entry_2018 = Entry(frame, width=5)
entry_2019 = Entry(frame, width=5)
entry_2020 = Entry(frame, width=5)

# Arrange entry widgets in grid
batman_entry.grid(row=1, column=0, padx=5)
entry_2017.grid(row=1, column=1, padx=5)
entry_2018.grid(row=1, column=2, padx=5)
entry_2019.grid(row=1, column=3, padx=5)
entry_2020.grid(row=1, column=4, padx=5)

# Buttons for operations
Button(window, text="Save Data", command=save_data).pack(pady=10)
Button(window, text="Show Bar Graph", command=show_graph).pack(pady=5)
Button(window, text="Delete All Data", command=delete_data).pack(pady=5)
Button(window, text="Insert Mockup Data", command=mockup_data).pack(pady=5)

# Start Tkinter event loop
window.mainloop()
