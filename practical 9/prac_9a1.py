import tkinter
from tkinter import *
 
window = tkinter.Tk()
C = tkinter.Canvas(window, bg="white", height=250, width=400)
C.pack()

coord = 60, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=359.99, fill="red")
# to rename the title of the window window.title("GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "Hello World!", font=("Arial Bold", 50)).pack()
 
window.mainloop()