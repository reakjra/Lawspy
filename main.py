from gravitation import calculate_gravitational_force
from ohm import calculate_current, calculate_resistance, calculate_voltage
from snell import calculate_refraction_angle
import os
import tkinter as tk
from tkinter import messagebox


def calculate_physics_law():
    selected_law = laws_menu.get()

    try:
        # Gravitational Law Calculation
        if selected_law == laws[0]:
            force = calculate_gravitational_force(float(mass1_entry.get()), float(mass2_entry.get()), float(distance_entry.get()))
            result_label.config(text=f"Gravitational Force: {force} N")

        # Ohm's Law Calculation
        elif selected_law == laws[1]:
            if current_entry.get():
                voltage = calculate_voltage(float(current_entry.get()), float(resistance_entry.get()))
                result_label.config(text=f"Voltage: {voltage} V")
            elif voltage_entry.get():
                current = calculate_current(float(voltage_entry.get()), float(resistance_entry.get()))
                result_label.config(text=f"Current: {current} A")
            elif resistance_entry.get():
                resistance = calculate_resistance(float(voltage_entry.get()), float(current_entry.get()))
                result_label.config(text=f"Resistance: {resistance} Ω")

        # Snell's Law Calculation
        elif selected_law == laws[2]:
            refraction_angle = calculate_refraction_angle(float(incident_angle_entry.get()), float(refractive_index1_entry.get()), float(refractive_index2_entry.get()))
            result_label.config(text=f"Refraction Angle: {refraction_angle} degrees")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def on_law_selection(*args):
    selected_law = laws_menu.get()

    for widget in input_widgets:
        widget.pack_forget()

    if selected_law == laws[0]:  
        show_input_fields(mass1_label, mass1_entry, mass2_label, mass2_entry, distance_label, distance_entry)
    elif selected_law == laws[1]:  
        show_input_fields(voltage_label, voltage_entry, current_label, current_entry, resistance_label, resistance_entry)
    elif selected_law == laws[2]:  
        show_input_fields(incident_angle_label, incident_angle_entry, refractive_index1_label, refractive_index1_entry, refractive_index2_label, refractive_index2_entry)

def show_input_fields(*args):
    for widget in args:
        widget.pack()


input_widgets = []

current_directory = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_directory, "icon.ico")


root = tk.Tk()
root.title("Physics Calculator")
root.geometry("600x400")
root.iconbitmap(icon_path)


choose_label = tk.Label(root, text="Choose the Law:")
choose_label.pack()

laws = ["Gravitational Law", "Ohm's Law", "Snell's Law"]
laws_menu = tk.StringVar(root)
laws_menu.set("Select a Law")  # Default value
laws_dropdown = tk.OptionMenu(root, laws_menu, *laws)
laws_dropdown.pack()


# Gravitational Law widgets
mass1_label = tk.Label(root, text="Mass 1 (kg)")
mass1_entry = tk.Entry(root)
mass2_label = tk.Label(root, text="Mass 2 (kg)")
mass2_entry = tk.Entry(root)
distance_label = tk.Label(root, text="Distance (m)")
distance_entry = tk.Entry(root)

# Ohm's Law widgets
voltage_label = tk.Label(root, text="Voltage (V)")
voltage_entry = tk.Entry(root)
current_label = tk.Label(root, text="Current (A)")
current_entry = tk.Entry(root)
resistance_label = tk.Label(root, text="Resistance (Ω)")
resistance_entry = tk.Entry(root)

# Snell's Law widgets
incident_angle_label = tk.Label(root, text="Incident Angle (degrees)")
incident_angle_entry = tk.Entry(root)
refractive_index1_label = tk.Label(root, text="Refractive Index 1")
refractive_index1_entry = tk.Entry(root)
refractive_index2_label = tk.Label(root, text="Refractive Index 2")
refractive_index2_entry = tk.Entry(root)

input_widgets.extend([mass1_label, mass1_entry, mass2_label, mass2_entry, distance_label, distance_entry,
                      voltage_label, voltage_entry, current_label, current_entry, resistance_label, resistance_entry,
                      incident_angle_label, incident_angle_entry, refractive_index1_label, refractive_index1_entry, refractive_index2_label, refractive_index2_entry])


calculate_button = tk.Button(root, text="Calculate", command=calculate_physics_law)
calculate_button.pack()


result_label = tk.Label(root, text="")
result_label.pack()

laws_menu.trace("w", on_law_selection)

root.mainloop()