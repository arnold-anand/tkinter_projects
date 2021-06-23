from tkinter import *
import pywhatkit as pwk
import datetime
from threading import *

root = Tk()

root.geometry("720x500")

root.title("Help Me Interview someone")

namelist = ["Names Inside the quotes",
            "Names Inside the quotes",
            "Names Inside the quotes",
            "Names Inside the quotes",
            "Names Inside the quotes",
            "Names Inside the quotes",
            "Names Inside the quotes"
            ]

# mobile numbers as integers with country code
mobile_numbers = [

]
i = 0


def threading1():
    # Call work function
    t1 = Thread(target=send_link)
    t1.start()


def threading2():
    t2 = Thread(target=send_alert)
    t2.start()


def send_link():
    candidate, mnum = display_deets()
    now = datetime.datetime.now()
    pwk.sendwhatmsg("+91" + str(mnum), f"{candidate}\nHere's Link for the interview:  \nJoin now", now.hour,
                    now.minute + 1, wait_time=20)
    # +91 is the country code for india. You can change according to your convenience


def send_alert():
    candidate, mnum = display_deets()
    now = datetime.datetime.now()
    pwk.sendwhatmsg("+91" + str(mnum), f"{candidate}\nYour Interview will Begin in 5 minutes.\nAll the best!", now.hour,
                    now.minute + 1, wait_time=30)


def next_person():
    global i
    display_deets()
    i += 1


def display_deets():
    global i
    Label(root, text=str(namelist[i]), bg="white", width=20, font=("Times New Roman", 15)).place(relx=0.5,
                                                                                                 rely=0.3)
    Label(root, text=mobile_numbers[i], bg="white", width=20, font=("Times New Roman", 15)).place(relx=0.5,
                                                                                                  rely=0.4)
    return namelist[i], mobile_numbers[i]


namelable = Label(root, text="Name of the candidate: ", font=("Times New Roman", 15)).place(relx=0.1, rely=0.3)

numlable = Label(root, text="Mobile number: ", font=("Times New Roman", 15)).place(relx=0.1, rely=0.4)

Label(root, text=str(namelist[i]), bg="white", width=20, font=("Times New Roman", 15)).place(relx=0.5,
                                                                                             rely=0.3)
Label(root, text=mobile_numbers[i], bg="white", width=20, font=("Times New Roman", 15)).place(relx=0.5,
                                                                                              rely=0.4)

NxtButton = Button(root, text="Next", font=("Times New Roman", 15), command=next_person).place(relx=0.1, rely=0.6)

AlertButton = Button(root, text="Send Alert", font=("Times New Roman", 15), command=threading2).place(relx=0.5,
                                                                                                      rely=0.6)

linkButton = Button(root, text="Send Link", font=("Times New Roman", 15), command=threading1).place(relx=0.1, rely=0.8)

root.mainloop()
