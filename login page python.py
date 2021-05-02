from tkinter import *
class S:
    root=Tk()
    root.geometry('2024x2024')
    root.title("BMS")
    def front(self):
        self.button1=Button(self.root,text="LOGIN", bg='blue',command=self.login)
        self.button1.grid(row=1,column=1,padx=120,pady=350)
        self.button2=Button(self.root,text="NEW USER",bg='blue',command=self.Register)
        self.button2.grid(row=1,column=3,padx=120,pady=350)
       
        
        self.root.mainloop()
    def login(self):
        self.destroy_front()
        self.root.title("LOGIN")
        self.dummy1=Label(self.root)
        self.dummy1.grid(row=0,columnspan=3,pady=150)
        
        
        self.dummy2=Label(self.root)
        self.dummy2.grid(rowspan=4,column=0,padx=250) 
        
        
        username=Label(self.root,text="USER NAME",fg='blue')
        username.grid(row=1, column=1)
        
        e=Entry(self.root)
        e.grid(row=1,column=2)
        
        password=Label(self.root,text="PASSWORD")
        password.grid(row=2, column=1)
        
        e1=Entry(self.root,show='#')
        e1.grid(row=2, column=2)
        
        lobutton=Button(self.root,text="signup",fg='blue')
        lobutton.grid(row=3, column=2)
    def Register(self):
        self.destroy_front()
        
        self.root.title("REGISTER")

        dup=Label(self.root,text=" ")
        dup.grid(rowspan=6,column=0,padx=250)

        dup1=Label(self.root,text=" ")
        dup.grid(row=0,columnspan=6,pady=200)

        name=Label(self.root,text="Name")
        name.grid(row=0 ,column=4)

        entry1=Entry(self.root)
        entry1.grid(row=0 ,column=5)

        address=Label(self.root,text="Address")
        address.grid(row= 1,column=4)

        entry2=Entry(self.root)
        entry2.grid(row=1 ,column=5)

        gender=Label(self.root,text="Gender")
        gender.grid(row=2 ,column=4)

        radio1=Radiobutton(self.root,text="Male")
        radio1.grid(row=2,column=5)

        radio2=Radiobutton(self.root,text="Female")
        radio2.grid(row= 2,column=6)

        mobileno=Label(self.root,text="MobileNo")
        mobileno.grid(row=3 ,column=4)

        entry3=Entry(self.root)
        entry3.grid(row=3 ,column=5)

        email=Label(self.root,text="Email Id")
        email.grid(row=4 ,column=4)

        entry4=Entry(self.root)
        entry4.grid(row=4 ,column=5)

        button=Button(self.root,text="SUBMIT",font=10,bg="green")
        button.grid(row=5,columnspan=10)

    def destroy_front(self):
        self.button1.destroy()
        self.button2.destroy()
        
   
    
obj=S()
obj.front()
