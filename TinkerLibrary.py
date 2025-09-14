import tkinter as tk

# Create the root window
root = tk.Tk()
root.title("Output Window")
root.geometry("300x100")  # width x height

# Output to be displayed
output_text = "Hello, World!"

# Create a label to show the output
output_label = tk.Label(root, text=output_text, font=("Arial", 16))
output_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
