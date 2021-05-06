# Creating a BMI calculator
import tkinter
from tkinter import *


root = tkinter.Tk()
root.title("BMI Calculator")
root.geometry("800x600")

header = Label(root, text="Ideal Body Mass Index Calculator")
header.place(relx=0, rely=0)

frame = Frame(root, width=500, height=200, borderwidth=1, relief="ridge")
frame.place(relx=0.1, rely=0.1)

# Create GUI
label_weight = tkinter.Label(frame, text="Weight (kg) : ").place(relx=0, rely=0)
entry_weight = tkinter.Entry(frame).place(relx=0.5, rely=0)

label_height = tkinter.Label(frame, text="Height (cm) : ").place(relx=0, rely=0.1)
entry_height = tkinter.Entry(frame).place(relx=0.5, rely=0.1)

label_gender = tkinter.Label(frame, text="Gender :").place(relx=0, rely=0.2)

label_age = tkinter.Label(frame, text="Age").place(relx=0, rely=0.3)
entry_age = tkinter.Entry(frame).place(relx=0.5, rely=0.3)


gender_menu = OptionMenu(frame, variable, *options, command=activate).place(relx=0.2, rely=0.2)

def activate(*args):
    if args == "Select...":
        age.config(state='normal')


options = ["Select...", "Male", "Female"]
variable = StringVar(frame)
variable.set(option[0])
gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place()
# Creating a function
def calculate_bmi():
    weight = float(entry_weight.get())
    height = float(entry_height.get())
    bmi = (round(weight / (height / 100) ** 2), 2)
    label_BMI['text'] = f"BMI: {bmi}"


def calculate_ideal_bmi():
    weight = float(entry_weight.get())
    height = float(entry_height.get())
    age = int(entry_age.get())
    ideal_female_bmi = (round(0.5 * weight / (height / 100) ** 2 + 0.03 * age + 11), 2)
    ideal_male_bmi = (round(0.5 * weight / (height / 100) ** 2 + 11.5), 2)


def delete():
    entry_weight.delete(0, 'end')
    entry_height.delete(0, 'end')
    entry_age.delete(0, 'end')
    entry.config(state="normal")
    entry.delete(0, END)
    # Converting the answer back to read only
    entry.config(state="readonly")


button_calculate = tkinter.Button(root, text="Calculate Ideal Body Mass Index", command=calculate_bmi)
button_calculate.place(relx=0.2, rely=0.4)

label_BMI = tkinter.Label(root, text="BMI: ").place(relx=0, rely=0.5)
entry = tkinter.Entry(root, bg="white", state="readonly").place(relx=0.5, rely=0.5)

label_ideal_BMI = tkinter.Label(root, text="Ideal BMI").place(relx=0, rely=0.6)
entry_ideal_BMI = tkinter.Entry(root, bg="white", state="readonly").place(relx=0.5, rely=0.6)

button_clear = Button(root, text="Clear", command=delete).place(relx=0.2, rely=0.7)
button_exit = Button(root, text="Exit", command="exit").place(relx=0.5, rely=0.7)

root.mainloop()