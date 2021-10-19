from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
import pymysql
from tkinter import messagebox
class Login_windows:
    def __init__(self,root):
        self.root=root
        self.root.title("Login From Vijay")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        
        
        
        
        
        
        
        #clock Background
        
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        
        
        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        
        
        #frame
        
        login_frame=Frame(self.root,bg="white")
        
        login_frame.place(x=250,y=100,width=800,height=500)
        
        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        
        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
        
        self.text_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.text_email.place(x=250,y=180,width=350,height=35)
        
        
        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
        
        self.text_pass=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.text_pass.place(x=250,y=280,width=350,height=35)
        
        btn_reg=Button(login_frame,cursor="hand2",command=self.register_windows,text="Register New Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)
        
        
        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20),fg="white",bg="#B00857",cursor="hand2").place(x=250,y=380,width=180,height=40)
        
        self.lbl=Label(self.root,text="\nVijay Dalvi",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        self.working()
    def register_windows(self):
        self.root.destroy()
        import vijay
        
        
    def login(self):
        if self.text_email.get()=="" or self.text_pass.get()=="":
           messagebox.showerror("Error","All Field Are Required",parent=self.root)
        else:
            try:
                
                
                con=pymysql.connect(host="localhost",user="root",password="",database="vijay2022")
                cur=con.cursor()
                cur.execute("select * from dalvi where email=%s and password_name=%s",(self.text_email.get(),self.text_pass.get()))
                row=cur.fetchone()
                if row==None:
                    
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                    
                else:
                    messagebox.showinfo("Sucess","Welcome",parent=self.root)
                    con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To:{str(es)}",parent=self.root)
                
                
        
        
        
        
        
        
        
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        bg=Image.open("vijay.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="red",width=4)
        
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
        
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="green",width=2)
        draw.ellipse((195,195,210,210),fill="black")
        
        clock.save("clock_new.png")
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
        
        
        
root=Tk()
obj=Login_windows(root)
root.mainloop()

 