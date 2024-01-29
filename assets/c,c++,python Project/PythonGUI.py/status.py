from tkinter import *

def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("READY now")

root=Tk()
root.geometry("455x280")
root.title("status bar")


statusvar=StringVar()
statusvar.set("READY")
sbar=Label(root,textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM , fill=X)
b=Button(root,text="Upload" , command=upload)
b.pack()

root.mainloop()
