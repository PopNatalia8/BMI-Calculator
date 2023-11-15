from tkinter import *


def bmi_calculator():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100
    gender.get()

    try:
        if gender == 'Male':
            bmi = weight / (height * height)
        else:
            bmi = (weight * 0.9) / (height * height)

        bmi_res.config(text=bmi)
        interpretation = bmi_interpretor(bmi)
        bmi_res.config(text=interpretation)
    except ZeroDivisionError:
        bmi_res.config(text=' ERROR ! You can not have 0 kg or 0 cm !', bg='red')
    except ValueError:
        bmi_res.config(text=' ERROR ! You need to enter an number !', bg='red')
    except Exception as e:
        bmi_res.config(text=' ERROR !', bg='red')
        print(e)


def bmi_interpretor(bmi):
    if bmi < 18.5:
        bmi_res.config(bg='#FEB132')
        return bmi
    elif bmi <= 24.9:
        bmi_res.config(bg='#30A232')
        return bmi
    elif 25.0 <= bmi <= 29.9:
        bmi_res.config(bg='#E96024')
        return bmi
    elif bmi > 29.9:
        bmi_res.config(bg='#C0101B')
        return bmi


window = Tk()
window.geometry('600x400')
window.config(bg='white')
window.title('BMI Calculator')

icon = PhotoImage(file='bmi.png')
window.iconphoto(True, icon)


background_label = Label(window, bg='#D9D9D9', width=77, height=10)
background_label.place(x=21, y=20)

weight_label = Label(window, text='Weight :', bg='#D9D9D9', font=('Fixedsys', 20))
weight_label.place(x=40, y=40)

weight_entry = Entry(window, width=15, font=('Fixedsys', 20))
weight_entry.place(x=190, y=40)

kg_label = Label(window, text='kg', bg='#D9D9D9', font=('Fixedsys', 20))
kg_label.place(x=450, y=40)

height_label = Label(window, text='Height : ', bg='#D9D9D9', font=('Fixedsys', 20))
height_label.place(x=40, y=80)

height_entry = Entry(window, width=15, font=('Fixedsys', 20))
height_entry.place(x=190, y=80)

cm_label = Label(window, text='cm', bg='#D9D9D9', font=('Fixedsys', 20))
cm_label.place(x=450, y=80)

# Create radio buttons to select the gender

gender = StringVar()
gender.set(str(None))
gender_label = Label(window, text='Select :', bg='#D9D9D9', font=('Fixedsys', 20))
gender_label.place(x=40, y=120)

male = Radiobutton(window, text='Male', variable=gender, value='Male', bg='#D9D9D9', font=('Fixedsys', 20))
female = Radiobutton(window, text='Female', variable=gender, value='Female', bg='#D9D9D9', font=('Fixedsys', 20))
male.place(x=200, y=120)
female.place(x=320, y=120)

# Create a calculate button

calculate = Button(window, text='Calculate BMI', borderwidth=0, highlightthickness=0, bg='dark grey', width=34, font=('Fixedsys', 20), command=bmi_calculator)
calculate.place(x=20, y=180)

# Display BMI Results and Interpreter

your_bmi_is = Label(window, text='Your BMI:', bg='#D9D9D9', font=('Fixedsys', 12), width=16, height=3)
your_bmi_is.place(x=20, y=260)

bmi_res = Label(window, font=('Fixedsys', 12), bg='white', width=51, height=3)
bmi_res.place(x=160, y=260)

# bmi_res = Label(window, text='')
# bmi_res.place(x=20, y=260)
# interpretation_label = Label(window, text='')
# interpretation_label.place(x=20, y=300)

label_underweight = Label(window, text='Underweight \n <18.5', foreground="white", width=16, height=3, bg='#FEB132', font=('Fixedsys', 12))
label_underweight.place(x=20, y=315)

label_underweight = Label(window, text='Normal Weight \n 18.5 - 25', foreground="white", width=16, height=3, bg='#30A232', font=('Fixedsys', 12))
label_underweight.place(x=160, y=315)

label_underweight = Label(window, text='Overweight \n 25 - 30', foreground="white", width=16, height=3, bg='#E96024', font=('Fixedsys', 12))
label_underweight.place(x=300, y=315)

label_underweight = Label(window, text='Obese \n >30', width=16, height=3, foreground="white", bg='#C0101B', font=('Fixedsys', 12))
label_underweight.place(x=440, y=315)

window.mainloop()
