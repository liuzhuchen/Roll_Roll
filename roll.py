import tkinter as tk
#import numpy as np
import random

roll = tk.Tk()
roll.title('ROLL THE DICE')
roll.geometry('400x400')
l = tk.Label(roll,
    text='Roll the dice',
    bg='white',
    font=('Times New Roman', 20),
    width=400, height=2
    )
l.pack()

var=tk.StringVar()
chat = tk.Label(roll,
                textvariable=var,
                font=('Times New Roman', 20),
                bg='white',
                width=400,height=2
                )
chat.pack()

def roll_button():
    number = random.randint(0,99)
    var.set(str(number))
    
roll_b = tk.Button(roll,
                   text='Roll',
                   width=15,height=2,
                   command=roll_button)

roll_b.place(x=120,y=200)



roll.mainloop()
