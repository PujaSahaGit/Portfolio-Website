from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0
root=Tk()
root.geometry("555x566")
root.title("Listbox")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First Item")
Button(root,text="Add Item",command=add).pack()

root.mainloop()
