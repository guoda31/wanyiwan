import tkinter as tk
import tkinter.messagebox
from tkinter import Frame, Button, Label
from tkinter import RIGHT, BOTH, LEFT, TOP, BOTTOM, X, Y
from main import getSingleStockData


#Window Contents
mainwindow = tk.Tk()
mainwindow.title = ("Single Stock Data Display")
# width * height + distance from left + d from right
mainwindow.geometry('800x500+100+100') 

#Left panel, used for controls
Lframe = Frame(mainwindow, bg="green")
leftLabel = Label(Lframe, text="this is the left frame")
leftLabel.pack(side =TOP)
Lframe.pack(side='left', fill=BOTH) 

#Right panel, used for displays
Rframe = Frame(mainwindow, bg="blue")
Rightlabel = Label(Rframe, text="this is the right frame")
Rightlabel.pack(side=TOP)
Rframe.pack(side=RIGHT, padx = 10, pady = 10)

#listbox in right panel
data = 0
lb = tk.Listbox(Rframe, listvariable = data)
lb.pack(side=RIGHT)

#FUN BUTTON YAY
clicked = False
def hitButton():
    global clicked
    if clicked == False:
        clicked = True
        print(tk.messagebox.showinfo(title="???", message="LOLS"))
    else: 
        print(tk.messagebox.showerror(title="???", message="no more lols"))   

b = Button(Lframe, text="hit for some lols", command=hitButton)

def fetch():
    global data
    name = stocknameTB.get()
    print (name)
    data = getSingleStockData(name)
    print (data)


#get stocks
#textbox for entering stock name
stocknameTB = tk.Entry(Lframe)

#confirm button
getdata = Button(Lframe, text="get data", command=fetch)

stocknameTB.pack(side=BOTTOM)
b.pack(side=TOP)
getdata.pack(side=BOTTOM)   #why is button above textbox??
#Run
mainwindow.mainloop()


