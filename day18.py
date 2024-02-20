# GUI reation with TKinter( advanced version of turtle module)
# advanced python- default arguments , args , kwargs 
import tkinter

window = tkinter.Tk()
window.title("my 1st GUI program")
window.minsize(width=500, height=300)

#labelclass
my_label = tkinter.Label(text="i am a fighter",font=("arial",24,"bold"))
my_label.pack()# none of the abovecode will show up unless we use pack


window.mainloop() #keeps the window open
# advanced python arguments - arguments with default value, INSIDE A FUNCTION HEADER
# FOR EX: TURTLE- MOVE , ALLIGN HAS ALREADY DEFAULT VALUE

# UNLIMITE arguments 
def add(n1, n2):# what if i want to add morethan 2 numb
    return n1 + n2 
# solution is *args
def add(*args): # that args name can be changed but imp is that * before the name
    print(args[1]) # *args puts all in tuple/ also called unlimited positional argument
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6,10,30,40)) # we can add more value as we like, it can take any value

#what if we want to fect *args by name? rather than by position?
def calculate(n, **kwargs): # keyword argument is kwags- we have added two astrics** before name
    print(kwargs) # it unlimited key word argument- we get dictonary with key and value
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)
# this is how tkintet works module lable has **kwags 


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        #self.make = kw["make"]- we can get hold of value with[]method but if didnt specify it whill calling it will crash
        self.model = kw.get("model")# so we use get function to get hold of value, benifit is reuns none even vw didnt specify
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
# this is how we create a class with lots of optional keyword arguments

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)

# TKdocumentation for gui - https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
# TK creating buttons, entry,setting component options

from tkinter import * # BY THIS WE CAN MENTION MODULE DIRECTLY BY IMPORTING ALL CLASS

window = Tk()
window.title("my 1st GUI program")
window.minsize(width=500, height=300)
window.config(padx=200,pady=200) # pading means adding more space around the program

#labelclass
my_label = Label(text="i am a fighter",font=("arial",24,"bold"))
my_label.pack()# none of the abovecode will show up unless we use pack

my_label["text"] = "new text" #1 we can change label text using either 1&2 of this methods
my_label.config(text="new 3 text") #2
#BUTTON
def buttonclick():
    print("i got clicked")
    # to use entry input we code here
    variable1 = input1.get()
    my_label.config(text=variable1)
button = Button(text="click me", command=buttonclick) # we are not calling but the name of the function, this command lets that click to work
button.pack()

#entry
input1 = Entry(width=15)
input1.pack()
window.mainloop()
 

# lets see example project
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()


# TKinter LAYOUT MANAGER
# PACK - packs all wigets(ex:label,button,entry) next to each other/ alyays starts from top/ cant keep presize position
# PLACE - its presize positioning ex: mylabel.place(x=0, y=0)
# GRID -IF 1000 WIDGET THEN HOW WILL PLACE WORK? ex: mylabel.place(column=0, row=0)/ cant place grid & pack in same code

# IN POMODORO WE HAVE USED DYNAMIC TYPING in python
a = 3
a = "ajay"
print(a)
a = 5
print(a)
# only in python just by assigining to other data type we can change the datatype
# python is strongly dynamically typed