import time
from tkinter import * 

window = Tk()
window.geometry('400x200+300+20')
window.title('clock')
window.config(bg = '#036057')


def clock():
    hour   = time.strftime('%H')
    minute = time.strftime('%M')    
    second = time.strftime('%S')      
    am_pm  = time.strftime('%p') 
    day    = time.strftime('%A')

    label2.config(text = day, bg = '#036057', fg ='#e5e5e5', font= ('Helvetica', 30) )

    label.config(text = hour + ':' + minute + ':' + second + ' ' + am_pm, font= ('Helvetica', 30), bg = '#036057', fg ='#e5e5e5')
    label.after(1000, clock)


label = Label(window, text = '')
label.pack(pady=20)


label2 = Label(window, text = '')
label2.pack(pady=10)


clock()
window.mainloop()