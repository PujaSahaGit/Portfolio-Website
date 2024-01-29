from tkinter import *
window = Tk()

window.geometry("600x250")
frame = Frame(window,bg="Yellowgreen",borderwidth=5)
frame.pack()

def one():
    print("You have press button 1")

def two():
    print("You have press button 2")

def three():
    print("You have press button 3")

def four():
    print("You have press button 4")

button1 = Button(frame,text="1",command=one)
button1.pack(side=LEFT,padx=10)

button2 = Button(frame,text="2",command=two)
button2.pack(side=LEFT,padx=10)

button3 = Button(frame,text="3",command=three)
button3.pack(side=LEFT,padx=10)

button4 = Button(frame,text="4",command=four)
button4.pack(side=LEFT,padx=10)

window.mainloop()
