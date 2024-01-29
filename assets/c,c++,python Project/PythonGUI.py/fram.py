from tkinter import *
root=Tk()
root.geometry("655x333")
f1=Frame(root , bg="green", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT ,fill=Y)
f2=Frame(root,bg="green", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP ,fill=X)
l=Label(f1, text="Project Tkinter-Python")
l.pack(pady=142)

l=Label(f2, text="WELCOME to Python", font="Helvetica 16 bold")
l.pack()
root.mainloop()