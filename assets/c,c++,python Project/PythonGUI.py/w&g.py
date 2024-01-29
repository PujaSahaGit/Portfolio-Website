from tkinter import *
root=Tk()

def getvalue():
    print(namevalue.get())
    print(dancevalue.get())
root.title("Dance class form")
root.maxsize(700,400)

name=Label(root,text="Student name:-")
name.grid(row=0)
dance=Label(root,text="Dance type:-")
dance.grid(row=1)

namevalue=StringVar()
dancevalue=StringVar()

nameentry=Entry(root,textvariable=namevalue)
nameentry.grid(row=0,column=1)

danceentry=Entry(root,textvariable=dancevalue)
danceentry.grid(row=1,column=1)

b1=Button(text="submit",bg="skyblue",fg="black",command=getvalue).grid()

root.mainloop()