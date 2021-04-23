from tkinter import *

window = Tk()
window.title("Kilogram Converter")

def kg_to():
    # Converting to grams
    kg = float(e1_value.get())
    grams = kg * 1000
    t1.delete("1.0", END)
    t1.insert(END,grams)
    
    # Converting to pounds
    pounds = kg * 2.204062
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    
    #Converting to ounces
    ounces = kg * 35.274
    t3.delete("1.0", END)
    t3.insert(END, ounces)
    
l1 = Label(window, text="Enter kilogram amount: ")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Kilograms to grams")
l2.grid(row = 1, column = 0)

l2 = Label(window, text = "Kilograms to pounds")
l2.grid(row = 1, column = 1)

l3 = Label(window, text = "Kilograms to ounces")
l3.grid(row = 1, column = 2)

e1_value = IntVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row = 0, column = 1)

b1 = Button(window, text="Convert", command=kg_to)
b1.grid(row = 0, column = 2)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 2, column = 0)

t2 = Text(window, height = 1, width = 20)
t2.grid(row = 2, column = 1)

t3 = Text(window, height = 1, width = 20)
t3.grid(row = 2, column = 2)

window.mainloop()