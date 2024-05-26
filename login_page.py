from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import os
from main import Main_Studio
from signup_page import SignUp
import credentials as cr

class login_page:
    def __init__(self, root):
        self.window = root
        self.window.title("Omega Studio")
        self.window.geometry("800x550")
        self.window.config(bg = "white")
        self.window.wm_iconbitmap("3.ico")
        self.window.resizable(False,False)

        self.frame2 = Frame(self.window, bg = "white")
        self.frame2.place(x=10,y=-80,relwidth=1, relheight=1,)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=195,y=150,width=500,height=450)

        self.email_label = Label(self.frame3,text="Email Address", font=("helvetica",20,"bold"),bg="white", fg="black").place(x=50,y=40)
        self.email_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="white",fg="gray",borderwidth=2)
        self.email_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3,text="Password", font=("helvetica",20,"bold"),bg="white", fg="black").place(x=50,y=120)
        self.password_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="white",fg="gray",show="*",borderwidth=2)
        self.password_entry.place(x=50, y=160, width=300)

        self.login_button = Button(self.frame3,text="Log In",command=self.login_func,font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=50,y=200,width=300)

        self.forgotten_pass = Button(self.frame3,text="Forgotten password?",command=self.forgot_func,font=("times new roman",10, "bold"),bd=0,cursor="hand2",bg="white",fg="blue").place(x=125,y=260,width=158)

        self.create_button = Button(self.frame3,text="Create New Account",command=self.redirect_window,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=68,y=320,width=265)


    def login_func(self):
        if self.email_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Omega Studio","All fields are required",parent=self.window)
        else:
            try:
                connection=pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and password=%s",(self.email_entry.get(),self.password_entry.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Omega Studio","Invalid USERNAME & PASSWORD",parent=self.window)
                else:
                    messagebox.showinfo("Omega Studio","Login Successfully",parent=self.window)
                    self.reset_fields()
                    connection.close()
                    self.window.destroy()

                    
                    Main_Studio(root)

            except Exception as e:
                messagebox.showerror("Omega Studio",f"Error due to {str(e)}",parent=self.window)

    def forgot_func(self):
        if self.email_entry.get()=="":
            messagebox.showerror("Omega Studio", "Please enter your Email Id",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s", self.email_entry.get())
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Omega Studio", "Email Id doesn't exists")
                else:
                    connection.close()

                    self.root=Toplevel()
                    self.root.title("Omega Studio")
                    self.root.geometry("400x440+450+200")
                    self.root.wm_iconbitmap("3.ico")
                    self.root.resizable(False,False)
                    self.root.config(bg="white")
                    self.root.focus_force()
                    self.root.grab_set()

                    title3 = Label(self.root,text="Change your password",font=("times new roman",20,"bold"),bg="white").place(x=38,y=10)

                    title5 = Label(self.root, text="Select your question", font=("times new roman", 15, "bold"), bg="white").place(x=95,y=85)

                    self.sec_ques = ttk.Combobox(self.root,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.sec_ques['values'] = ("Select","What's your pet name?","Your first teacher name","Your birthplace", "Your favorite movie")
                    self.sec_ques.place(x=67,y=120, width=270)
                    self.sec_ques.current(0)
                    
                    title6 = Label(self.root, text="Answer", font=("times new roman", 15, "bold"), bg="white").place(x=160,y=160)

                    self.ans = Entry(self.root,font=("arial"),borderwidth=2)
                    self.ans.place(x=67,y=195,width=270)

                    title7 = Label(self.root, text="New Password", font=("times new roman", 15, "bold"), bg="white").place(x=122,y=235)

                    self.new_pass = Entry(self.root,font=("arial"),borderwidth=2)
                    self.new_pass.place(x=67,y=270,width=270)

                    self.create_button = Button(self.root,text="Submit",command=self.change_pass,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=95,y=340,width=200)

            except Exception as e:
                messagebox.showerror("Omega Studio", f"{e}")
                
      
    def change_pass(self):
        if self.email_entry.get() == "" or self.sec_ques.get() == "Select" or self.new_pass.get() == "":
            messagebox.showerror("Omega Studio", "Please fill the all entry field correctly")
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and question=%s and answer=%s", (self.email_entry.get(),self.sec_ques.get(),self.ans.get()))
                row=cur.fetchone()

                if row == None:
                    messagebox.showerror("Omega Studio", "Please fill the all entry field correctly")
                else:
                    try:
                        cur.execute("update student_register set password=%s where email=%s", (self.new_pass.get(),self.email_entry.get()))
                        connection.commit()

                        messagebox.showinfo("Successful", "Password has changed successfully")
                        connection.close()
                        self.reset_fields()
                        self.root.destroy()

                    except Exception as er:
                        messagebox.showerror("Omega Studio", f"{er}")
                        
            except Exception as er:
                        messagebox.showerror("Omega Studio", f"{er}")
            

    def redirect_window(self):
        root = Tk()
        obj = SignUp(root)
        root.mainloop()

    def reset_fields(self):
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)

if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()