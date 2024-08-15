
import tkinter as tk
from tkinter import messagebox

def main():
    """Main function to input weight and height, calculate BMI, and display the category."""

    def calculate_bmi(weight, height):
        """Calculate BMI using weight (kg) and height (m)."""
        bmi = weight / (height ** 2)
        return bmi

    def bmi_category(bmi):
        """Determine the BMI category."""
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        result_text.set(f"Your BMI is: {bmi:.2f}\nYou are classified as: {category}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator 🔥")
root.geometry("435x350")
root.configure(bg="#1e1e1e")

# Font settings
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
emoji_font = ("Segoe UI Emoji", 14)  # Use a font that supports color emojis

# Welcome message
welcome_msg = tk.Label(root, text="Welcome to the BMI Calculator!!! 👋", font=emoji_font, fg="white", bg="#1e1e1e")
welcome_msg.pack(pady=10)

# Weight label and entry
label_weight = tk.Label(root, text="Enter Your Weight (kg):", font=label_font, fg="white", bg="#1e1e1e")
label_weight.pack()

entry_weight = tk.Entry(root, font=entry_font, fg="white", bg="#333", insertbackground="white")
entry_weight.pack(pady=5)

# Height label and entry
label_height = tk.Label(root, text="Enter Your Height (m):", font=label_font, fg="white", bg="#1e1e1e")
label_height.pack(pady=10)

entry_height = tk.Entry(root, font=entry_font, fg="white", bg="#333", insertbackground="white")
entry_height.pack(pady=5)

# Button to calculate BMI
btn_calculate = tk.Button(root, text="Calculate BMI 📊", font=emoji_font, fg="white", bg="#ff4500", command=main)
btn_calculate.pack(pady=20)

# Result label
result_text = tk.StringVar()
label_result = tk.Label(root, textvariable=result_text, justify="left", font=label_font, fg="white", bg="#1e1e1e")
label_result.pack(pady=10)

# Start the main loop
root.mainloop()
