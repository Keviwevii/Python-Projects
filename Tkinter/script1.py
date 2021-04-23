# We should import everything from tkinter
from tkinter import *

# This creates our actual window
window = Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)
b1 = Button(window,text="Execute", command=km_to_miles)
# You can use grid or pack to assign the buttons places
b1.grid(row = 0, column = 0)


e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 2)

window.mainloop()