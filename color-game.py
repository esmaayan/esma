import random
import tkinter
from tkinter import messagebox

# variables
colour = ['red','blue','green','pink','black','yellow','orange','white','purple','brown']
time_limit = 30
score = 0 
new_colour  = random.choice(colour)
text_colour  = random.choice(colour)

# start game (function that will start the game.)
def startGame(event):
     
    if time_limit == 30:
         
        # start the countdown timer.
        leftTime()
         
    # run the function to
    # choose the next colour.
    instructions2.destroy()
    nextColour()

# next colour
def nextColour():
    global new_colour, text_colour, score

    if entry.get().lower()== new_colour.lower():
             
        score += 1
        # clear the text entry box.
    entry.delete(0, tkinter.END)

    # change the colour to type, by changing the
    # text _and_ the colour to a random colour value
    new_colour  = random.choice(colour)
    text_colour = random.choice(colour)
    colourLabel.config(fg = str(new_colour), text = str(text_colour))
         
    # update the score.
    labelScore.config(text = "score: " + str(score))

# left time
def leftTime():
    global time_limit
    if time_limit > 0:
        time_limit -=1
        timeLabel.config(text=f'time left : {time_limit}')
        # call the lefttime function again after 1000 milliseconds (1 second).
        gameScreen.after(1000, leftTime)
    else:
        messagebox.showinfo('score', f'your score is {score}!')

# create game gameScreen
gameScreen = tkinter.Tk()
gameScreen.title('colour-game')
gameScreen.iconbitmap('crayon.ico')
gameScreen.geometry('300x300+700+100')
gameScreen.resizable(False, False)
gameScreen.config(bg = 'light grey' )

# colour label
colourLabel = tkinter.Label( gameScreen, text = new_colour, fg = text_colour, height=2, width=10, font=('Arial Bold',30), bg = 'light grey')
colourLabel.place( x = 30, y = 50)

# time label
timeLabel = tkinter.Label( gameScreen, text = (f'time left : {time_limit}' ), font=('Helvetica', 12), bg = 'light grey')
timeLabel.place( x = 10, y = 20)

# create entry 
entry = tkinter.Entry(gameScreen, bg='light grey', width=15, font= 'Helvetica 20')
entry.place(x = 30, y = 150)
entry.focus_set()

# score label
labelScore = tkinter.Label(gameScreen, text = (f"score : {score}"), font = ('Helvetica', 12), bg = "light grey")
labelScore.place(x = 10, y = 40)

# reset function
def reset():
    pass

# create menu
my_menu = tkinter.Menu(gameScreen)
gameScreen.config(menu= my_menu)

#options
options_menu = tkinter.Menu(my_menu, tearoff = False, bg= 'light grey')
my_menu.add_cascade(label = 'options', menu = options_menu)
options_menu.add_command(label='reset game', command = reset)

# instructions
instructions1 = tkinter.Label(gameScreen, text = "type in the colour of the words,\n and not the word text!",
                            font = ('Helvetica', 12), bg = "light grey")
instructions1.place( x = 35, y=200)

instructions2 = tkinter.Label(gameScreen, text = "press Enter to start", font = ('Arial bold', 14),fg= 'dark grey', bg = "light grey")
instructions2.place( x = 60, y=250)

gameScreen.bind('<Return>', startGame)

# game loop
gameScreen.mainloop()