import tkinter as tk
import random

win = 0
lose = 0

def rps(user):
    global win, lose
    computer = random.randint(1, 5)

    if user == computer:
        var.set("It's a draw. \nNo Points")  
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2) or (user == 4 and computer == 3) or (user == 5 and computer == 4):
        var.set("You win!")
        win += 1
        wins.set(win)
    else:
        var.set("You lose!")
        lose += 1
        wins.set(win)

top = tk.Tk()
top.wm_title("RPS Python GUI")
top.geometry("350x150")

B1 = tk.Button(top, text="Rock", command=lambda: rps(1))
B1.grid(row=0, column=1)
B2 = tk.Button(top, text="Paper", command=lambda: rps(2))
B2.grid(row=0, column=2)
B3 = tk.Button(top, text="Scissors", command=lambda: rps(3))
B3.grid(row=0, column=3)

space = tk.Label(top, text="")
space.grid(row=1)

var = tk.StringVar()
var.set('Welcome!')
l = tk.Label(top, textvariable=var)
l.grid(row=2, column=2)

wins = tk.IntVar()
wins.set(win)
w = tk.Label(top, textvariable=wins)
w.grid(row=4, column=2)

labeled = tk.Label(top, text="Score:")
labeled.grid(row=3, column=2)

top.mainloop()
