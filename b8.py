import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox, Label, Frame, Tk, Entry, Button, END
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data = """Batmans,2017,2018,2019,2020
virat,2501,1855,2203,1223
Steve,2340,2250,2003,1153
Azam,1750,2147,1896,1008
Rohit,1463,1985,1854,1638
William,1256,1785,1874,1974"""

file = "test.csv"


def delete_data():
    try:
        with open(file, "w") as f:
            f.write("")  # write nothing
        messagebox.showinfo("Deleted", "All data deleted successfully!")
    except FileNotFoundError:
        messagebox.showerror("Error", "File does not exist.")


def mockup_data():
    try:
        # Write mock sample data to the file
        with open(file, "w") as f:
            f.write(data.strip())
        messagebox.showinfo("Mock Data", "Mock data written successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write mock data: {e}")


def save_data():
    batmans = batman_entry.get()
    y2017 = entry_2017.get()
    y2018 = entry_2018.get()
    y2019 = entry_2019.get()
    y2020 = entry_2020.get()

    if not (batmans and y2017 and y2018 and y2019 and y2020):
        messagebox.showwarning("Input Error", "Please fill all field")
        return

    data = pd.DataFrame(
        [[batmans, int(y2017), int(y2018), int(y2019), int(y2020)]],
        columns=["Batmans", "2017", "2018", "2019", "2020"],
    )

    try:
        exist = pd.read_csv(file)
        df = pd.concat([exist, data], ignore_index=True)
    except FileNotFoundError:
        df = data

    df.to_csv(file, index=False)
    messagebox.showinfo("Success", f"Data for {batmans} saved")

    batman_entry.delete(0, END)
    entry_2017.delete(0, END)
    entry_2018.delete(0, END)
    entry_2019.delete(0, END)
    entry_2020.delete(0, END)


def show_graph():
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
    fig, ax = plt.subplots(figsize=(8, 5))
    df.plot(x="Batmans", kind="bar", figsize=(8, 5), ax=ax)
    plt.title("Batman Performance Over Years")
    plt.xlabel("Batman")
    plt.ylabel("Performance")
    plt.tight_layout()
    # plt.show()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


window = Tk()
window.title("Batmans data Entry")
window.geometry("400x600")

Label(window, text="Enter Batmans Performance data:", font=("Arial", 14, "bold")).pack(
    pady=10
)

frame = Frame(window)
frame.pack(pady=10)

Label(frame, text="Batman").grid(row=0, column=0)
Label(frame, text="2017").grid(row=0, column=1)
Label(frame, text="2018").grid(row=0, column=2)
Label(frame, text="2019").grid(row=0, column=3)
Label(frame, text="2020").grid(row=0, column=4)


batman_entry = Entry(frame)
entry_2017 = Entry(frame, width=5)
entry_2018 = Entry(frame, width=5)
entry_2019 = Entry(frame, width=5)
entry_2020 = Entry(frame, width=5)


batman_entry.grid(row=1, column=0, padx=5)
entry_2017.grid(row=1, column=1, padx=5)
entry_2018.grid(row=1, column=2, padx=5)
entry_2019.grid(row=1, column=3, padx=5)
entry_2020.grid(row=1, column=4, padx=5)

Button(window, text="Save data", command=save_data).pack(pady=10)

Button(window, text="Show bar graph", command=show_graph).pack(pady=5)

Button(window, text="Delete all data", command=delete_data).pack(pady=5)
Button(window, text="Insert mockup data", command=mockup_data).pack(pady=5)
window.mainloop()
