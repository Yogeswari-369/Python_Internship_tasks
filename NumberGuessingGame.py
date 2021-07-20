
from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
root.geometry("500x500")
root.title("Number Guessing Game")



def GenerateNumberFunc():
    global Number
    Number = randint(1,20)
    messagebox.showinfo("A Number was Generated!", "Please Guess the Number")

def GuessNumberFunc():
    global Number
    UserResponse = AnswerEntry.get()
    UserResponse = int(UserResponse)
    if UserResponse > Number:
        ResultLabel.config(text="Incorrect! Guess Lower Number", fg="Red")
    elif UserResponse < Number:
        ResultLabel.config(text="Incorrect! Guess Higher Number", fg="Red")
    else:
        ResultLabel.config(text="You Guess was  Correct...! The Number was {}".format(Number), fg="Green")
        AnswerEntry.delete(0, "end")




Title = Label(root, text="Number Guessing Game", font=("Bold",30))
Title.pack()
MainFrame = Frame(root)
MainFrame.pack(pady=60)
GuessNumLabel = Label(MainFrame, text="Guess a number from 1 to 20:", font=("Arial",20))
GuessNumLabel.pack()
AnswerEntry = Entry(MainFrame, font=("Arial", 16))
AnswerEntry.pack(pady=10)
GenerateNumberBtn = Button(MainFrame, text="Generate Number", width=16, font=("Arial", 16), background="white", command=GenerateNumberFunc)
GenerateNumberBtn.pack()
GuessBtn = Button(MainFrame, text="Guess", width=16, font=("Arial", 16), background="white", command=GuessNumberFunc)
GuessBtn.pack(pady=5)
ResultLabel = Label(MainFrame, text="", font=("Arial", 16))
ResultLabel.pack()


root.mainloop()
