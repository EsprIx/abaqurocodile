import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error 

# Connect to the db
connection = mysql.connector.connect(
    host = "185.157.246.165",
    user = "host",
    passwd = "zds>%4jPa_si6e[z_{(4",
    database = "abaque",
    port = "3306"
)

# Variables
values = []
cursor = connection.cursor()

# Init
for i in range(8):
    values.append("init" + str(i))

# Functions
# 0
def question0(sentence):
    label_entry = Label(questions_frame0, text = sentence, font = ("Calibri", 20), fg = "white", bg = "#808080")
    label_entry.pack()
def highButton0():
    high_button = Radiobutton(high_button_frame0, text = "Elevé", font = ("Calibri", 15), bg = "#808080", value = "H", variable = values[0], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")   
    high_button.pack()
def mediumButton0():
    medium_button = Radiobutton(medium_button_frame0, text = "Moyen", font = ("Calibri", 15), bg = "#808080", value = "M", variable = values[0], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    medium_button.pack()
def lowButton0():
    low_button = Radiobutton(low_button_frame0, text = "Faible", font = ("Calibri", 15), bg = "#808080", value = "L", variable = values[0], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    low_button.pack()

# 1
def question1(sentence):
    label_entry = Label(questions_frame1, text = sentence, font = ("Calibri", 20), fg = "white", bg = "#808080")
    label_entry.pack()
def yesButton1():
    yes_button = Radiobutton(yes_button_frame1, text = "Oui", font = ("Calibri", 15), bg = "#808080", value = "Y", variable = values[1], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")   
    yes_button.pack()
def noButton1():
    no_button = Radiobutton(no_button_frame1, text = "Non", font = ("Calibri", 15), bg = "#808080", value = "N", variable = values[1], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    no_button.pack()

# 2
def question2(sentence):
    label_entry = Label(questions_frame2, text = sentence, font = ("Calibri", 20), fg = "white", bg = "#808080")
    label_entry.pack()
def yesButton2():
    yes_button = Radiobutton(yes_button_frame2, text = "Oui", font = ("Calibri", 15), bg = "#808080", value = "Y", variable = values[2], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")   
    yes_button.pack()
def noButton2():
    no_button = Radiobutton(no_button_frame2, text = "Non", font = ("Calibri", 15), bg = "#808080", value = "N", variable = values[2], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    no_button.pack()

# 3
def question3(sentence):
    label_entry = Label(questions_frame3, text = sentence, font = ("Calibri", 20), fg = "white", bg = "#808080")
    label_entry.pack()
def highButton3():
    high_button = Radiobutton(high_button_frame3, text = "Elevé", font = ("Calibri", 15), bg = "#808080", value = "H", variable = values[3], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")   
    high_button.pack()
def mediumButton3():
    medium_button = Radiobutton(medium_button_frame3, text = "Moyen", font = ("Calibri", 15), bg = "#808080", value = "M", variable = values[3], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    medium_button.pack()
def lowButton3():
    low_button = Radiobutton(low_button_frame3, text = "Faible", font = ("Calibri", 15), bg = "#808080", value = "L", variable = values[3], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    low_button.pack()

# 4
def question4(sentence):
    label_entry = Label(questions_frame4, text = sentence, font = ("Calibri", 20), fg = "white", bg = "#808080")
    label_entry.pack()
def highButton4():
    high_button = Radiobutton(high_button_frame4, text = "Elevé", font = ("Calibri", 15), bg = "#808080", value = "H", variable = values[4], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")   
    high_button.pack()
def mediumButton4():
    medium_button = Radiobutton(medium_button_frame4, text = "Moyen", font = ("Calibri", 15), bg = "#808080", value = "M", variable = values[4], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    medium_button.pack()
def lowButton4():
    low_button = Radiobutton(low_button_frame4, text = "Faible", font = ("Calibri", 15), bg = "#808080", value = "L", variable = values[4], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    low_button.pack()

# 5
def question5(sentence):
    label_entry = Label(questions_frame5, text = sentence, font = ("Calibri", 20), fg = "white", bg = "#808080")
    label_entry.pack()
def yesButton5():
    yes_button = Radiobutton(yes_button_frame5, text = "Oui", font = ("Calibri", 15), bg = "#808080", value = "Y", variable = values[5], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")   
    yes_button.pack()
def noButton5():
    no_button = Radiobutton(no_button_frame5, text = "Non", font = ("Calibri", 15), bg = "#808080", value = "N", variable = values[5], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    no_button.pack()

# 6
def question6(sentence):
    label_entry = Label(questions_frame6, text = sentence, font = ("Calibri", 20), fg = "white", bg = "#808080")
    label_entry.pack()
def yesButton6():
    yes_button = Radiobutton(yes_button_frame6, text = "Oui", font = ("Calibri", 15), bg = "#808080", value = "Y", variable = values[6], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")   
    yes_button.pack()
def noButton6():
    no_button = Radiobutton(no_button_frame6, text = "Non", font = ("Calibri", 15), bg = "#808080", value = "N", variable = values[6], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    no_button.pack()

# 7
def question7(sentence):
    label_entry = Label(questions_frame7, text = sentence, font = ("Calibri", 20), fg = "white", bg = "#808080")
    label_entry.pack()
def highButton7():
    high_button = Radiobutton(high_button_frame7, text = "Elevé", font = ("Calibri", 15), bg = "#808080", value = "H", variable = values[7], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")   
    high_button.pack()
def mediumButton7():
    medium_button = Radiobutton(medium_button_frame7, text = "Moyen", font = ("Calibri", 15), bg = "#808080", value = "M", variable = values[7], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    medium_button.pack()
def lowButton7():
    low_button = Radiobutton(low_button_frame7, text = "Faible", font = ("Calibri", 15), bg = "#808080", value = "L", variable = values[7], highlightthickness = 0, bd = 0, activebackground = "#808080", fg = "white", selectcolor= "#696969")  
    low_button.pack()

# Next
def nextButton():
    next_button = Button(next_button_frame, text = "Rechercher", font = ("Calibri", 15), fg = "white", bg = "#A9A9A9", command = next, highlightthickness = 0, bd = 0, height = 2)
    next_button.pack(expand = True, fill = "both") 

def quitButton():
    quit_button = Button(quit_button_frame, text = "Quitter", font = ("Calibri", 15), fg = "white", bg = "#A9A9A9", command = exit, highlightthickness = 0, bd = 0, height = 2)
    quit_button.pack(expand = True, fill = "both") 

def exit():
    root.destroy()

def returnValue(x):
    return x.get()

def next():
    newList = map(returnValue, values)
    if "undefined" not in newList:
        execute(values[0].get(), values[1].get() ,values[2].get() ,values[3].get() ,values[4].get() ,values[5].get() ,values[6].get() ,values[7].get())
    else:
        messagebox.showerror("Erreur", "Veuillez répondre à chaque critère !")
        return

def execute(p1, p2, p3, p4, p5, p6, p7, p8):
    cursor.execute('SELECT * FROM materials WHERE rCorrosion = %s AND cThermique = %s AND cElectrique = %s AND rCompression = %s AND rFlexion = %s AND recyclable = %s AND incinerable = %s AND budget = %s', (p1, p2, p3, p4, p5, p6, p7, p8))
    x = cursor.fetchone()
    if x:
        messagebox.showinfo("Résultat trouvé", "Le " + x[0] + " correspond à tout vos critères !")
    else:
        messagebox.showwarning("Aucun résultat trouvé", "Aucun matériau présent dans notre base de donnée ne correspond à vos critères !")

    print("")
    print("Nous éspérons que nos services vous aurons satisfait.")
    print("")

# Define the root
root = Tk()
root.title("Abaqurocodile")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.minsize(w, h)
root.maxsize(w, h)
root.iconbitmap("logo.ico")
root.config(background = "#808080")

# Other variables
values[0] = StringVar(value = "undefined")
values[1] = StringVar(value = "undefined")
values[2] = StringVar(value = "undefined")
values[3] = StringVar(value = "undefined")
values[4] = StringVar(value = "undefined")
values[5] = StringVar(value = "undefined")
values[6] = StringVar(value = "undefined")
values[7] = StringVar(value = "undefined")

# Create the frames & scrollbar
frame = Frame(root, bg = "#808080")
canvas = Canvas(frame, bg = "#808080")

s = ttk.Style()
s.configure("TFrame", background="#808080") 
scrollable_frame = ttk.Frame(canvas, style = "TFrame")

scrollbar = ttk.Scrollbar(frame, orient = "vertical", command = canvas.yview)
scrollable_frame = ttk.Frame(canvas)

# Config the scrollbar
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((root.winfo_width() / 2, root.winfo_height() / 2), window = scrollable_frame, anchor = "n")
canvas.configure(yscrollcomman = scrollbar.set)

# Create the subframes
title_frame = Frame(scrollable_frame, bg = "#808080")

# 0
questions_frame0 = Frame(scrollable_frame, bg = "#808080")
high_button_frame0 = Frame(scrollable_frame, bg = "#808080")
medium_button_frame0 = Frame(scrollable_frame, bg = "#808080")
low_button_frame0 = Frame(scrollable_frame, bg = "#808080")
# 1
questions_frame1 = Frame(scrollable_frame, bg = "#808080")
yes_button_frame1 = Frame(scrollable_frame, bg = "#808080")
no_button_frame1 = Frame(scrollable_frame, bg = "#808080")
# 2
questions_frame2 = Frame(scrollable_frame, bg = "#808080")
yes_button_frame2 = Frame(scrollable_frame, bg = "#808080")
no_button_frame2 = Frame(scrollable_frame, bg = "#808080")
# 3
questions_frame3 = Frame(scrollable_frame, bg = "#808080")
high_button_frame3 = Frame(scrollable_frame, bg = "#808080")
medium_button_frame3 = Frame(scrollable_frame, bg = "#808080")
low_button_frame3 = Frame(scrollable_frame, bg = "#808080")
# 4
questions_frame4 = Frame(scrollable_frame, bg = "#808080")
high_button_frame4 = Frame(scrollable_frame, bg = "#808080")
medium_button_frame4 = Frame(scrollable_frame, bg = "#808080")
low_button_frame4 = Frame(scrollable_frame, bg = "#808080")
# 5
questions_frame5 = Frame(scrollable_frame, bg = "#808080")
yes_button_frame5 = Frame(scrollable_frame, bg = "#808080")
no_button_frame5 = Frame(scrollable_frame, bg = "#808080")
# 6
questions_frame6 = Frame(scrollable_frame, bg = "#808080")
yes_button_frame6 = Frame(scrollable_frame, bg = "#808080")
no_button_frame6 = Frame(scrollable_frame, bg = "#808080")
# 7
questions_frame7 = Frame(scrollable_frame, bg = "#808080")
high_button_frame7 = Frame(scrollable_frame, bg = "#808080")
medium_button_frame7 = Frame(scrollable_frame, bg = "#808080")
low_button_frame7 = Frame(scrollable_frame, bg = "#808080")
# Next
next_button_frame = Frame(scrollable_frame, bg = "#808080")
# Quit
quit_button_frame = Frame(scrollable_frame, bg = "#808080")

# Add settings to the frames
label_title = Label(title_frame, text = "Abaque numérique", font = ("Calibri", 30), fg = "white", bg = "#808080")
label_title.pack()

label_subtitle = Label(title_frame, text = "Réalisé par Meriadec Labbé, Tom Pinabel et Tom Jurien", font = ("Calibri", 15), fg = "white", bg = "#808080")
label_subtitle.pack()

# Questions
question0("Veuillez indiquer la résistance du matériau à la corrosion")
highButton0()
mediumButton0()
lowButton0()

question1("Veuillez indiquer si le matériau est un conducteur thermique")
yesButton1()
noButton1()

question2("Veuillez indiquer si le matériau est un conducteur électrique")
yesButton2()
noButton2()

question3("Veuillez indiquer la résistance du matériau à la compression")
highButton3()
mediumButton3()
lowButton3()

question4("Veuillez indiquer la résistance du matériau à la flexion")
highButton4()
mediumButton4()
lowButton4()

question5("Veuillez indiquer si vous souhaitez que le matériau soit recyclable")
yesButton5()
noButton5()

question6("Veuillez indiquer si vous souhaitez que le matériau soit incinérable")
yesButton6()
noButton6()

question7("Veuillez indiquer votre budget")
highButton7()
mediumButton7()
lowButton7()

nextButton()
quitButton()

# Show the frames & subframes
title_frame.grid(row = 0, column = 0, pady = 75)

# 0
questions_frame0.grid(row = 1, column = 0, pady = 25)
high_button_frame0.grid(row = 2, column = 0, sticky = W, pady = 5)
medium_button_frame0.grid(row = 2, column = 0, sticky = N, pady = 5)
low_button_frame0.grid(row = 2, column = 0, sticky = E, pady = 5)
# 1
questions_frame1.grid(row = 3, column = 0, pady = 25)
yes_button_frame1.grid(row = 4, column = 0, sticky = W, pady = 5, padx = 100)
no_button_frame1.grid(row = 4, column = 0, sticky = E, pady = 5, padx = 100)
# 2
questions_frame2.grid(row = 5, column = 0, pady = 25)
yes_button_frame2.grid(row = 6, column = 0, sticky = W, pady = 5, padx = 100)
no_button_frame2.grid(row = 6, column = 0, sticky = E, pady = 5, padx = 100)
# 3
questions_frame3.grid(row = 7, column = 0, pady = 25)
high_button_frame3.grid(row = 8 , column = 0, sticky = W, pady = 5)
medium_button_frame3.grid(row = 8, column = 0, sticky = N, pady = 5)
low_button_frame3.grid(row = 8, column = 0, sticky = E, pady = 5)
# 4
questions_frame4.grid(row = 9, column = 0, pady = 25)
high_button_frame4.grid(row = 10, column = 0, sticky = W, pady = 5)
medium_button_frame4.grid(row = 10, column = 0, sticky = N, pady = 5)
low_button_frame4.grid(row = 10, column = 0, sticky = E, pady = 5)
# 5
questions_frame5.grid(row = 11, column = 0, pady = 25)
yes_button_frame5.grid(row = 12, column = 0, sticky = W, pady = 5, padx = 100)
no_button_frame5.grid(row = 12, column = 0, sticky = E, pady = 5, padx = 100)
# 6
questions_frame6.grid(row = 13, column = 0, pady = 25)
yes_button_frame6.grid(row = 14, column = 0, sticky = W, pady = 5, padx = 100)
no_button_frame6.grid(row = 14, column = 0, sticky = E, pady = 5, padx = 100)
# 7
questions_frame7.grid(row = 15, column = 0, pady = 25)
high_button_frame7.grid(row = 16 , column = 0, sticky = W, pady = 5)
medium_button_frame7.grid(row = 16, column = 0, sticky = N, pady = 5)
low_button_frame7.grid(row = 16, column = 0, sticky = E, pady = 5)
# Next
next_button_frame.grid(row = 17, column = 0, sticky = 'EWNS', pady = 25)
# Quit
quit_button_frame.grid(row = 18, column = 0, sticky = 'EWNS', pady = 10)

frame.pack(expand = True, fill = "both")
canvas.pack(side="left", fill="both", expand= True)
scrollbar.pack(side="right", fill="y")

# Show the root
root.mainloop()