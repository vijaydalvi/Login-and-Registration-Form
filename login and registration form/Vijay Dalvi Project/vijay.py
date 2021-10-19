from  tkinter import *
from tkinter import ttk,messagebox
import pymysql

from PIL import Image ,ImageTk
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Regiseration Window")
        self.root.geometry("1350x700+0+0")
       #--bg-image
        self.bg=ImageTk.PhotoImage(file="12.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)


        #--left

        self.left=ImageTk.PhotoImage(file="32.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        #--Registar frame


        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)


        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        
        #----row--1
        
        
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        
        self.f_name=Entry(frame1,font=("times new roman",15,"bold"),bg="lightgray")
        self.f_name.place(x=50,y=130,width=250)
        


        last_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)

        self.last_name=Entry(frame1,font=("times new roman",15,"bold"),bg="lightgray")
        self.last_name.place(x=370,y=130,width=250)
          #- row2
        contact_name=Label(frame1,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)

        self.contact_name=Entry(frame1,font=("times new roman",15,"bold"),bg="lightgray")
        self.contact_name.place(x=50,y=200,width=250)
       
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)

        self.email_name=Entry(frame1,font=("times new roman",15,"bold"),bg="lightgray")
        self.email_name.place(x=370,y=200,width=250)
       #-row-3

        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)

        self.comboquestion=ttk.Combobox(frame1,font=("times new roman",15,"bold"),state='readonly',justify=CENTER)
        self.comboquestion['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.comboquestion.place(x=50,y=270,width=250)
        self.comboquestion.current(0)
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)

        self.answer_name=Entry(frame1,font=("times new roman",15,"bold"),bg="lightgray")
        self.answer_name.place(x=370,y=270,width=250)

      #--row4

        password_name=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)

        self.password_name=Entry(frame1,font=("times new roman",15,"bold"),bg="lightgray")
        self.password_name.place(x=50,y=340,width=250)
       
        conpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)

        self.conpassword_name=Entry(frame1,font=("times new roman",15,"bold"),bg="lightgray")
        self.conpassword_name.place(x=370,y=340,width=250)
        #--Terms

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",15,)).place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="122.png")
        btn_Regisrer=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)

        btn_login=Button(self.root,text="Sign In",command=self.login_windows,bg="green",fg="white",font=("times new roman",20),bd=0,cursor="hand2").place(x=180,y=580,width=150)
    def login_windows(self):
        self.root.destroy()
        import SignIn
        
        
    def clear(self):
        self.f_name.delete(0,END) 
        self.last_name.delete(0,END) 
        self.contact_name.delete(0,END) 
        self.email_name.delete(0,END) 
        self.comboquestion.delete(0,END)
        self.answer_name.delete(0,END) 
        self.password_name.delete(0,END) 
        self.conpassword_name.delete(0,END)
        
    








    def register_data(self):
        if self.f_name.get()=="" or self.last_name.get()=="" or self.contact_name.get()=="" or self.email_name.get()=="" or self.comboquestion.get()=="Select" or self.answer_name.get()=="" or self.password_name.get()=="" or self.conpassword_name.get()=="" : 
              messagebox.showerror("Error","All Field Are Required",parent=self.root)
        elif self.password_name.get()!=self.conpassword_name.get():
              messagebox.showerror("Error","Password & Confirm Password Should be Same",parent=self.root)

        elif self.var_chk.get()==0:
              messagebox.showerror("Error","Please Agree Our Terms & Conditions",parent=self.root)

        else:
            try:
               con=pymysql.connect(host="localhost",user="root",password="",database="vijay2022")
               cur=con.cursor()
               cur.execute("select *from dalvi where email=%s",self.email_name.get())
               row=cur.fetchone()
               #print(row)
               if row!=None:
                messagebox.showerror("Error","User Alredy Exit Please Try With Another Email",parent=self.root)
               else:     
                     cur.execute("insert into dalvi(f_name,last_name,contact_name,email,question,answer,password_name)values(%s,%s,%s,%s,%s,%s,%s)",
              
               
               
                                    ( self.f_name.get(),
                                      self.last_name.get(),
                                      self.contact_name.get(),
                                      self.email_name.get(),
                                      self.comboquestion.get(),
                                      self.answer_name.get(),
                                      self.conpassword_name.get()
                                    ))
                     con.commit()
                     con.close()
                     self.clear()
                     messagebox.showinfo("Sucess","Register Sucessful",parent=self.root)
            except  Exception as es:
                     messagebox.showerror("Error",f"Error Due to:  {str(es)}",parent=self.root)
             
             
             
             
             
            



        
         
         
       
       
         
               
root=Tk()
obj=Register(root)
root.mainloop()