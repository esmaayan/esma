from base64 import b32encode
from tkinter import *

#build screen
screen = Tk()
screen.title('calculator')
screen.geometry('470x350')
screen.iconbitmap('dino.ico')
screen.config(bg='grey')

#build entry
entry = Entry(screen, justify=RIGHT, width=24, font='Verdana 14 bold', bd=5)
entry.grid(row=0, column=0, columnspan=4)

#button command
def write(number):
    new = len(entry.get())
    entry.insert(new, str(number))

def delete():
    entry.delete(0, END)

def buttonplus():
    s1 = entry.get()
    global n1
    n1 = int(s1)

    global m 
    m = 'add'
    entry.delete(0, END)

def buttonsubtraction():
    s1 = entry.get()
    global n1
    n1 = int(s1)

    global m 
    m = 'sub'
    entry.delete(0, END)

def buttonmultiplication():
    s1 = entry.get()
    global n1
    n1 = int(s1)

    global m 
    m = 'multi'
    entry.delete(0, END)

def buttondivide():
    s1 = entry.get()
    global n1
    n1 = int(s1)

    global m 
    m = 'div'
    entry.delete(0, END)

def buttonequal():
    s2 = entry.get()
    global n2 
    n2 = int(s2)

    entry.delete(0, END)

    if m == 'add':
        entry.insert(0, n1+n2)

    if m == 'sub':
        entry.insert(0, n1-n2)

    if m == 'multi':
        entry.insert(0, n1*n2)

    if m == 'div':
        entry.insert(0, n1/n2)



#build button
b1= Button(text='1', font='Times 14 italic', height=2, width=10, command= lambda: write(1))
b2= Button(text='2', font='Times 14 italic', height=2, width=10, command= lambda: write(2))
b3= Button(text='3', font='Times 14 italic', height=2, width=10, command= lambda: write(3))

b4= Button(text='4', font='Times 14 italic', height=2, width=10, command= lambda: write(4))
b5= Button(text='5', font='Times 14 italic', height=2, width=10, command= lambda: write(5))
b6= Button(text='6', font='Times 14 italic', height=2, width=10, command= lambda: write(6))

b7= Button(text='7', font='Times 14 italic', height=2, width=10, command= lambda: write(7))
b8= Button(text='8', font='Times 14 italic', height=2, width=10, command= lambda: write(8))
b9= Button(text='9', font='Times 14 italic', height=2, width=10, command= lambda: write(9))

b0= Button(text='0', font='Times 14 italic', height=2, width=10, command= lambda: write(0))

resetbutton= Button(text='clear', font='Times 14 italic', height=2, width=10, command= lambda: delete())

plusb= Button(text='+', font='Times 14 italic', height=2, width=10, bg='orange', command= lambda: buttonplus() )
subtractionb= Button(text='-', font='Times 14 italic', height=2, width=10, bg='orange', command= lambda: buttonsubtraction() )
multiplicationb= Button(text='*', font='Times 14 italic', height=2, width=10, bg='orange', command= lambda: buttonmultiplication())
divideb = Button(text='/', font='Times 14 italic', height=2, width=10, bg='orange', command= lambda: buttondivide())

equalbutton= Button(text='=', font='Times 14 italic', height=2, width=10, command = lambda: buttonequal())

#grid button
plusb.place(x=360, y= 50 )
subtractionb.place(x=360, y=120)
multiplicationb.place(x=360, y=190)
divideb.place(x=360,y=260)




b1.place(x=0  , y=50)
b2.place(x=120, y=50)
b3.place(x=240, y=50)

b4.place(x=0  , y=120)
b5.place(x=120, y=120)
b6.place(x=240, y=120)

b7.place(x=0  , y=190)
b8.place(x=120, y=190)
b9.place(x=240, y=190)

b0.place(x=120, y=260)
equalbutton.place(x=240, y=260)
resetbutton.place(x=0  , y=260)

screen.mainloop()
