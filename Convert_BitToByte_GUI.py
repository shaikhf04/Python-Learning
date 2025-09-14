import tkinter as tk
from tkinter import ttk, messagebox

units = ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]
factors = {
    "bit": 1,
    "byte": 8,
    "kilobyte": 8 * 1024,
    "megabyte": 8 * 1024**2,
    "gigabyte": 8 * 1024**3,
    "terabyte": 8 * 1024**4,
    "petabyte": 8 * 1024**5,
}


def convert():
    try:
        val = float(entry_value.get())
        from_u = combo_from.get()
        to_u = combo_to.get()

        if from_u not in factors or to_u not in factors:
            messagebox.showerror("Error", "Please select valid units.")
            return

        # Convert to bits
        val_in_bits = val * factors[from_u]

        # Convert bits to target
        result = val_in_bits / factors[to_u]

        label_result.config(text=f"{val} {from_u}(s) = {result} {to_u}(s)")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric value.")


# GUI setup
root = tk.Tk()
root.title("Bit-Byte Conversion")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

ttk.Label(frame, text="Value:").grid(row=0, column=0, sticky="w")
entry_value = ttk.Entry(frame)
entry_value.grid(row=0, column=1)

ttk.Label(frame, text="From Unit:").grid(row=1, column=0, sticky="w")
combo_from = ttk.Combobox(frame, values=units, state="readonly")
combo_from.grid(row=1, column=1)
combo_from.current(0)

ttk.Label(frame, text="To Unit:").grid(row=2, column=0, sticky="w")
combo_to = ttk.Combobox(frame, values=units, state="readonly")
combo_to.grid(row=2, column=1)
combo_to.current(1)

btn_convert = ttk.Button(frame, text="Convert", command=convert)
btn_convert.grid(row=3, column=0, columnspan=2, pady=10)

label_result = ttk.Label(frame, text="")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
