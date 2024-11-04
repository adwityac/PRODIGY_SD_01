import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = var_unit.get()

        if unit == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            result = f"Fahrenheit: {fahrenheit:.2f} °F\nKelvin: {kelvin:.2f} K"
        elif unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            result = f"Celsius: {celsius:.2f} °C\nKelvin: {kelvin:.2f} K"
        elif unit == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result = f"Celsius: {celsius:.2f} °C\nFahrenheit: {fahrenheit:.2f} °F"
        else:
            result = "Please select a valid unit."

        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for temperature.")

# Set up the main application window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

# Input for temperature
label_temp = tk.Label(root, text="Enter Temperature:")
label_temp.pack(pady=5)

entry_temp = tk.Entry(root)
entry_temp.pack(pady=5)

# Dropdown for selecting the unit
var_unit = tk.StringVar(value="Celsius")
label_unit = tk.Label(root, text="Select Unit:")
label_unit.pack(pady=5)

option_unit = tk.OptionMenu(root, var_unit, "Celsius", "Fahrenheit", "Kelvin")
option_unit.pack(pady=5)

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert_temperature)
button_convert.pack(pady=10)

# Label to display results
label_result = tk.Label(root, text="Converted Temperatures will appear here", wraplength=250)
label_result.pack(pady=5)

# Run the application
root.mainloop()
