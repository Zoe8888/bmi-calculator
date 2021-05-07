# Creating a BMI calculator
from tkinter import *
from tkinter import messagebox


root = Tk()
# Creating a title
root.title("BMI Calculator")
# Setting the window size
root.geometry("700x500")
# Setting a background color
root.config(bg="#47d16c")

# Creating & positioning the header with a background color
header = Label(root, text="Ideal Body Mass Index Calculator", bg="#47d16c")
header.place(relx=0.2, rely=0)

# Creating & positioning the frame with a background color
frame = Frame(root, width=500, height=200, borderwidth=1, relief="ridge", bg="#65e687")
frame.place(relx=0.1, rely=0.1)

# Creating & positioning the weight label & entry point with a background color
label_weight = Label(frame, text="Weight (kg) : ", bg="#65e687")
label_weight.place(relx=0, rely=0)
entry_weight = Entry(frame)
entry_weight.place(relx=0.5, rely=0)

# Creating & positioning the height label & entry point with a background color
label_height = Label(frame, text="Height (cm) : ", bg="#65e687")
label_height.place(relx=0, rely=0.1)
entry_height = Entry(frame)
entry_height.place(relx=0.5, rely=0.1)

# Creating & positioning the age label & entry point with a background color
label_age = Label(frame, text="Age", bg="#65e687")
label_age.place(relx=0, rely=0.2)
entry_age = Entry(frame)
entry_age.place(relx=0.5, rely=0.2)

# Creating & positioning the gender label with a background color
label_gender = Label(frame, text="Gender :", bg="#65e687")
label_gender.place(relx=0, rely=0.3)


# Setting the gender menu options
options = ["Select..", "Male", "Female"]
variable = StringVar(frame)
variable.set(options[0])
gender_menu = OptionMenu(frame, variable, *options)
gender_menu.place(relx=0.5, rely=0.3)


# Defining the function used to calculate the BMI and the ideal BMI
def calculate_ideal_bmi():
    try:
        float(entry_weight.get())
        float(entry_height.get())
        float(entry_age.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * int(entry_weight.get())) / ((int(entry_height.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            entry_ideal_BMI.config(state='normal')
            entry_ideal_BMI.insert(0, result)
            entry_ideal_BMI.config(state='readonly')
            result_bmi = int(entry_weight.get()) / ((int(entry_height.get()) / 100) ** 2)
            entry_BMI.config(state='normal')
            entry_BMI.insert(0, round(result_bmi, 1))
            entry_BMI.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * int(entry_weight.get())) / ((int(entry_height.get()) / 100) ** 2)) + (
                    0.03 * int(entry_age.get())) + 11
            result = round(result, 1)
            entry_ideal_BMI.config(state='normal')
            entry_ideal_BMI.insert(0, result)
            entry_ideal_BMI.config(state='readonly')
            result_bmi = int(entry_weight.get()) / ((int(entry_height.get()) / 100) ** 2)
            entry_BMI.config(state='normal')
            entry_BMI.insert(0, round(result_bmi, 1))
            entry_BMI.config(state='readonly')
        # Setting the various conditions for the analysis
        if result_bmi <= 18.5:
            analysis.config(text="You are underweight")
        elif 18.5 <= result_bmi < 25:
            analysis.config(text="You are normal weight")
        elif 25 <= result_bmi < 30:
            analysis.config(text="You are overweight")
        elif result_bmi >= 30:
            analysis.config(text="You are obese")
    except ValueError:
        messagebox.showerror(title=None, message='Gender was not specified or invalid entry was given')
        delete()


# Defining the function that makes the "Clear" button operational
def delete():
    entry_weight.delete(0, END)
    entry_weight.focus()
    entry_height.delete(0, END)
    entry_age.delete(0, END)
    entry_BMI.config(state="normal")
    entry_BMI.delete(0, END)
    entry_BMI.config(state="readonly")
    entry_ideal_BMI.config(state="normal")
    entry_ideal_BMI.delete(0, END)
    entry_ideal_BMI.config(state="readonly")
    variable.set(options[0])
    analysis.config(text='')


# Creating & positioning the BMI calculate button
button_calculate = Button(root, text="Calculate Ideal Body Mass Index", command=calculate_ideal_bmi)
button_calculate.place(relx=0.3, rely=0.5)

# Creating & positioning the BMI label & entry point with a background color
label_BMI = Label(root, text="BMI: ", bg="#47d16c")
label_BMI.place(relx=0.2, rely=0.6)
entry_BMI = Entry(root, bg="white", state="readonly")
entry_BMI.place(relx=0.4, rely=0.6)

# Creating & positioning the ideal BMI label & entry point with a background color
label_ideal_BMI = Label(root, text="Ideal BMI", bg="#47d16c")
label_ideal_BMI.place(relx=0.2, rely=0.7)
entry_ideal_BMI = Entry(root, bg="white", state="readonly")
entry_ideal_BMI.place(relx=0.4, rely=0.7)

# Creating & positioning conclusion with a background color.
# It informs the user the state of their weight (eg. overweight, underweight, etc)
label_analysis = Label(root, text="Category", bg="#47d16c")
label_analysis.place(relx=0.2, rely=0.8)
analysis = Label(root, width="20")
analysis.place(relx=0.4, rely=0.8)

# Creating & positioning the clear button
button_clear = Button(root, text="Clear", command=delete)
button_clear.place(relx=0.3, rely=0.9)

# Creating & positioning the exit button
button_exit = Button(root, text="Exit", command="exit")
button_exit.place(relx=0.5, rely=0.9)

root.mainloop()
