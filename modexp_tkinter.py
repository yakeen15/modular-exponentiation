import tkinter as tk
from mod_exp import modexp
def calculate_result():
    # Get input values from entry boxes
    value1 = entry1.get()
    value2 = entry2.get()
    value3 = entry3.get()

    # Perform calculation (Example: Concatenate the three values)
    result = modexp(int(value1),int(value2),int(value3))

    # Display result in the output box
    output_text.configure(state='normal')
    output_text.delete('1.0', 'end')
    output_text.insert('end', result)
    output_text.configure(state='disabled')

# Create the main window
window = tk.Tk()

# Set the title of the window
window.title("Modular exponentiation")
window.iconbitmap("calc.ico")
window.geometry("400x300")

# Create placeholder labels
placeholder_label1 = tk.Label(window, text="Base")
placeholder_label1.pack()

# Create input boxes
entry1 = tk.Entry(window)
entry1.pack()

placeholder_label2 = tk.Label(window, text="Exponent")
placeholder_label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

placeholder_label3 = tk.Label(window, text="Modulus")
placeholder_label3.pack()

entry3 = tk.Entry(window)
entry3.pack()

placeholder_label4 = tk.Label(window, text="(Base^Exponent) % Modulus")
placeholder_label4.pack()

# Create output box
output_text = tk.Text(window, height=5, width=30)
output_text.configure(state='disabled')
output_text.pack()

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_result)
calculate_button.pack()

# Start the Tkinter event loop
window.mainloop()
