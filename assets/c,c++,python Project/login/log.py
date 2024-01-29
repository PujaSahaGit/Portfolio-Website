from tkinter  import*

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1340x700+0+0")

        self.bg_icon=ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon=PhotoImage(file="images/user.png")
        self.pass_icon=PhotoImage(file="images/pass.png")

        bg_lbl=Label(self.root,image=self.bg_icon).pack() 
        title=Label(self.root,text="Login_System",front=("times new roman",40,"bold"),bg="pink",fg="blue",bd=10,relief="GROOVE")
        title.place(x=0,y=0,relwidtg=1)
        
root=Tk()
obj=Login_System(root)
root.mainloop()


