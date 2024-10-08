import tkinter
from tkinter import *

def miles_to_km():
    miles_start = float(miles_input.get())
    km = miles_start * 1.609
    kilo_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#labels
is_equal_to = tkinter.Label(text="is equal to", font="Times New Roman")
is_equal_to.grid(column=0, row=1)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

kilo_result = tkinter.Label(text="0")

#input
miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

#button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)




# from tkinter import *
#
# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)
#
# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)
#
# #label
#
# my_label = tkinter.Label(text="I am a label", font=("arial", 24, "bold"))
#
#
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
# my_label.grid(column=0,row=0)
#
# #Button
#
#
#
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
#
# #Entry
# input = Entry(width=10)
# answer = input.pack()
# input.grid(column=3, row=2)
#
# #new button
# button_new = Button(text="I'm new")
# button_new.grid(column=2, row=0)
#
# import turtle
# tim = turtle.Turtle()
# tim.write("some text", font=("Times New Roman", 80, "bold"))
#
#
#
window.mainloop()