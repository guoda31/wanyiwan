import tkinter as tk
import tkinter.messagebox
from tkinter import Frame, Button, Label
from tkinter import RIGHT, BOTH, LEFT, TOP, X, Y


#Window Contents
mainwindow = tk.Tk()
mainwindow.title = ("Single Stock Data Display")
# width * height + distance from left + d from right
mainwindow.geometry('200x300+100+100') 

Lframe = Frame(mainwindow)
leftLabel = Label(Lframe, text="this is the left frame")

leftLabel.pack(side =LEFT)
Rframe = Frame(mainwindow)
Rightlabel = Label(Rframe, text="this is the right frame")
Rightlabel.pack(side=RIGHT)
Lframe.pack(side='left')    
Rframe.pack(side=RIGHT, padx = 10, pady = 10)

clicked = False
def hitButton():
    global clicked
    if clicked == False:
        clicked = True
        print(tk.messagebox.showinfo(title="???", message="LOLS"))
    else: 
        print(tk.messagebox.showerror(title="???", message="no more lols"))   

b = Button(Lframe, text="hit for some lols", command=hitButton)
b.pack(side='bottom')
#Run
mainwindow.mainloop()


