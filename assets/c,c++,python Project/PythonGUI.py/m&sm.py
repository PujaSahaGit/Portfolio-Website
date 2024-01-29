from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("813x566")
root.title("Pycharm")
def myfunc():

    print("function")
def help():
    print("i will help you")
    tmsg.showinfo("help","harry will help you")
def rate():
    print("rate us")
    value=tmsg.askquestion("was it?")
    if value=="yes":
        msg="great"
    else:
        msg="tell"
    tmsg.showinfo("experience", msg)
def divya():
    ans=tmsg.askretrycancel("diviya as friend","sorry")
    if ans:
        print("retry")
    else:
        print("good")
    

#mymenu=Menu(root)
#mymenu.add_command(label="File",command=myfunc)
#mymenu.add_command(label="Exit",command=quit)
#root.config(menu=mymenu)

yourmenubar=Menu(root)
m1=Menu(yourmenubar,tearoff=0)
m1.add_command(label="New pro", command=myfunc)
m1.add_separator()
m1.add_command(label="save", command=myfunc)
m1.add_command(label="print", command=myfunc)
root.config(menu= yourmenubar)
yourmenubar.add_cascade(label="file", menu=m1)

m2=Menu(yourmenubar,tearoff=0)
m2.add_command(label="New pro", command=myfunc)
m2.add_separator()
m2.add_command(label="save", command=myfunc)
m2.add_command(label="print", command=myfunc)
root.config(menu= yourmenubar)
yourmenubar.add_cascade(label="edit", menu=m2)

m3=Menu(yourmenubar,tearoff=0)
m3.add_command(label="New pro", command=myfunc)
m3.add_separator()
m3.add_command(label="save", command=help)
m3.add_command(label="print", command=rate)

m3.add_command(label="befriend divya", command=divya)

root.config(menu= yourmenubar)
yourmenubar.add_cascade(label="help", menu=m3)


root.mainloop()