import random
from tkinter import *
from tkinter import messagebox

#pick a random word
randomNumber = str(random.randint(1000, 9999))

# build screen
window = Tk()
window.title('guess number game')
window.geometry('500x300+500+50')
window.config(bg='#d7c0e5')

#timer 
tlabel= Label(window, bg='yellow', height=2, width=18)
tlabel.place(x=360 ,y=5)

# build entry
entry0 = Entry(window, bg='light grey', width=1, font= 'Helvetica 20 bold')
entry0.place(x=210, y=200)

entry1 = Entry(window, bg='light grey', width=1, font= 'Helvetica 20 bold')
entry1.place(x=260, y=200)

entry2 = Entry(window, bg='light grey', width=1, font= 'Helvetica 20 bold')
entry2.place(x=310, y=200)

entry3 = Entry(window, bg='light grey', width=1, font= 'Helvetica 20 bold')
entry3.place(x=360, y=200)

# confirm button
confirmButton = Button(window, text='confirm', bg='light grey', fg='black', font= 'Verdana 10 bold',
                       height=5, width=20, command= lambda: check())

confirmButton.place(x=10, y=200)

# label
label = Label(window, bg='#d7c0e5', height=10, width=25) 
label.place(x=10, y=5)

# check
def check():
    entry00 = str(entry0.get())
    entry11 = str(entry1.get())
    entry22 = str(entry2.get())
    entry33 = str(entry3.get())

    labelnew = Label(window, bg='#d7c0e5', height=10, width=35)
    labelnew.place(x=10, y=5)

    if randomNumber[0] == entry00:
        check00t = Label(labelnew, text='1. number is true',fg='green',bg= '#d7c0e5' , font='Verdana 10 bold')
        check00t.place(x=10 ,y=10)
    else:
        check00f = Label(labelnew, text='1. number is false, try again!!!',fg='red',bg= '#d7c0e5' , font='Verdana 10 bold')
        check00f.place(x=10 ,y=10)

    if randomNumber[1] == entry11:
        check11t = Label(labelnew, text='2. number is true',fg='green' ,bg= '#d7c0e5' ,font='Verdana 10 bold')
        check11t.place(x=10 ,y=40)
    else:
        check11f = Label(labelnew, text='2. number is false, try again!!!',fg='red' ,bg= '#d7c0e5' , font='Verdana 10 bold')
        check11f.place(x=10 ,y=40)

    if randomNumber[2] == entry22:
        check22t = Label(labelnew, text='3. number is true',fg='green' ,bg= '#d7c0e5' ,font='Verdana 10 bold')
        check22t.place(x=10 ,y=70)
    else:
        check22f = Label(labelnew, text='3. number is false, try again!!!',fg='red' ,bg= '#d7c0e5' , font='Verdana 10 bold')
        check22f.place(x=10 ,y=70)

    if randomNumber[3] == entry33:
        check33t = Label(labelnew, text='4. number is true',fg='green' ,bg= '#d7c0e5' ,font='Verdana 10 bold')
        check33t.place(x=10 ,y=100)
    else:
        check33f = Label(labelnew, text='4. number is false, try again!!!',fg='red' ,bg= '#d7c0e5' , font='Verdana 10 bold')
        check33f.place(x=10 ,y=100)

    if randomNumber == entry00 + entry11 + entry22 + entry33:
        messagebox.showinfo('congrats!!!', 'you win!!!!')
        

    


window.mainloop()