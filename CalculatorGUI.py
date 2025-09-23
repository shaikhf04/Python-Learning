import tkinter as tk

# Function to perform calculation
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "minus":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            result = num1 / num2

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

# Input fields
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 14))
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 14))
entry2.pack()

# Operation buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(button_frame, text="Add", width=10, command=lambda: calculate("add")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Minus", width=10, command=lambda: calculate("minus")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Multiply", width=10, command=lambda: calculate("multiply")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Divide", width=10, command=lambda: calculate("divide")).grid(row=1, column=1, padx=5, pady=5)

# Result display
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=20)

# Start the GUI loop
root.mainloop()
