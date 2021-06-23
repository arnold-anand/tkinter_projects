from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def details():
    f = open('Form details.txt', 'a+')
    f.write(f"Name:  {name_entry.get()}")
    f.write('\n')
    f.write(f"Email:  {email_entry.get()}")
    f.write('\n')
    if gen_checkm.get() == 1:
        f.write('Gender:  Male')
    else:
        f.write('Gender:  Female')
    f.write('\n')
    f.write(f"Country: {drop.get()}")
    f.write('\n')
    if prog_java.get() == 1:
        f.write('Programming Language:  Java')
    else:
        f.write('Programming Language:  Python')
    f.write('\n\n')
    f.seek(0, 2)
    f.close()


def ask():
    details()
    status = messagebox.showinfo(title="Submission", message="Your form has been submitted!")
    if status == 'ok':
        root.quit()


root = Tk()
root.geometry("600x450")
root.title("Registration Form")

tit = Label(root, text="Registration form", font=("Times New Roman", 24)).place(anchor=W, relx=0.01, rely=0.1)

name = Label(root, text="Full Name *", font=("Times New Roman", 14)).place(anchor=W, relx=0.01, rely=0.25)
email = Label(root, text="E-mail *", font=("Times New Roman", 14)).place(anchor=W, relx=0.01, rely=0.35)
gen = Label(root, text="Gender *", font=("Times New Roman", 14)).place(anchor=W, relx=0.01, rely=0.45)
count = Label(root, text="Country *", font=("Times New Roman", 14)).place(anchor=W, relx=0.01, rely=0.55)
lang = Label(root, text="Programming *", font=("Times New Roman", 14)).place(anchor=W, relx=0.01, rely=0.65)

name_entry = StringVar()
email_entry = StringVar()
gen_checkm = IntVar()
gen_checkf = IntVar()
prog_py = IntVar()
prog_java = IntVar()
clicked = StringVar()
countries = ['Africa', 'Australia', 'India', 'United Kingdom', 'United States of America', 'USSR']

ne = Entry(root, textvariable=name_entry, width=70).place(anchor=W, rely=0.25, relx=0.2)
ee = Entry(root, textvariable=email_entry, width=70).place(anchor=W, rely=0.35, relx=0.2)

gcm = Checkbutton(root, variable=gen_checkm, text='Male').place(anchor=W, rely=0.45, relx=0.2)
gcf = Checkbutton(root, variable=gen_checkf, text='Female').place(anchor=W, rely=0.45, relx=0.3)

drop = ttk.Combobox(root, value=countries, text='Select your country', state='readonly')
drop.place(anchor=W, rely=0.55, relx=0.2)

prog1 = Checkbutton(root, variable=prog_java, text='Java').place(anchor=W, rely=0.65, relx=0.23)
prog2 = Checkbutton(root, variable=prog_py, text='Python').place(anchor=W, rely=0.65, relx=0.33)

submit = Button(root, text="Submit", bg="red", width=7, height=1, command=ask, font=12).place(anchor=W, rely=0.75,
                                                                                              relx=0.01)
root.mainloop()
