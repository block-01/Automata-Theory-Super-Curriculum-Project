import sys
from tkinter import *

def Call():
    msg = Label(window, text = "test")
    msg.place(x=30, y=50)
    button["bg"] = "blue"
    button ["fg"] = "white"
window =Tk()
window.geometry("200x110")
button = Button(text = "click here", command = Call)
button.place(x = 30, y = 20, width=120, height=25)
window.mainloop()

#print ("Hello World")
#test=input("...")