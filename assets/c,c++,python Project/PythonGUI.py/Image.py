from tkinter import *
from PIL import Image, ImageTk
puja_root=Tk()
puja_root.geometry("900x704")
puja_root.minsize(130,220)
heading=Label(text="My album")
heading.pack()

#photo=PhotoImage(file="android-chrome-512x512.png")
#for jpg image
image=Image.open("downloadg.jpg")
image1=Image.open("downloadg1.jpg")
image2=Image.open("downloadg2.jpg")
image3=Image.open("downloadg3.jpg")

photo=ImageTk.PhotoImage(image)
photo1=ImageTk.PhotoImage(image1)
photo2=ImageTk.PhotoImage(image2)
photo3=ImageTk.PhotoImage(image3)

Puja_label=Label(image=photo)
Puja_label1=Label(image=photo1)
Puja_label2=Label(image=photo2)
Puja_label3=Label(image=photo3)
Puja_label.pack()
Puja_label1.pack()
Puja_label2.pack()
Puja_label3.pack()


puja_root.mainloop()


