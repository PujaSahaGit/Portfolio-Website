from tkinter import *
def Puja(event):
    print(f"you clicked on the button{event.x},{event.y}")
root=Tk()
root.title("Events in tkinter")
root.geometry("644x334")
Widget=Button(root, text="Click me plz")

Widget.pack()
Widget.bind('<Button-1>' ,Puja)
Widget.bind('<Double-1>' , quit)
root.mainloop()
