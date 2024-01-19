
from tkinter import *
from admin_page import Admin_operations
from tkinter import messagebox



class Admin_login_win:

    def __init__(self,root) :
        self.root = root
        self.root.title("Admin Login")
        self.root.geometry("580x360+341+249")
        self.root.minsize(580,360)
        self.root.maxsize(580,360)



        # -------------variables-------------
        self.id_var = StringVar()
        self.password_var = StringVar()



       

        head_label = Label(self.root,text="Admin Login",font=("arial",12,"bold"),width=575,height=2,bg="#ecf54c")
        head_label.pack(side=TOP,fill=X)


        full_frame= Frame(self.root,bg="#e5f28f",bd=4,width=580,height=330)
        full_frame.place(x=0,y=40)

        id_label = Label(full_frame,text="ID               :",font=("arial",11,"bold"),bg="#dff7da",padx=2,pady=1,bd=2,relief="groove")
        id_label.place(x=150,y=25)
        id_entry = Entry(full_frame,font=("arial",11,"bold"),bg="#dff7da",bd=2,relief="groove",textvariable=self.id_var)
        id_entry.place(x=250,y=25)


        password_label = Label(full_frame,text="Password  :",font=("arial",11,"bold"),bg="#dff7da",padx=2,pady=1,bd=2,relief="groove")
        password_label.place(x=150,y=65)
        password_entry = Entry(full_frame,show="*",font=("arial",11,"bold"),bg="#dff7da",bd=2,relief="groove",textvariable=self.password_var)
        password_entry.place(x=250,y=65)


        back_button = Button(full_frame,text="Back",font=("arial",11,"bold"),pady=2,padx=14,bd=2,bg="#f27777",command=self.root.destroy)
        back_button.place(x=150,y=150)



        login_button = Button(full_frame,text="Login",font=("arial",11,"bold"),fg="white",pady=2,padx=14,bd=2,bg="#31eb2a",command=self.login)
        login_button.place(x=350,y=150)


    def login(self):
        id = self.id_var.get()
        password = self.password_var.get()

        if not id or not password:
            messagebox.showerror("Login Failed", "Please enter both ID and password")
            return
        
        if id == "Admin" and password == "Admin@123" :
             self.open_new_win()

        


    

    def open_new_win(self):
        self.open_new_win = Toplevel(self.root)
        self.app_admin = Admin_operations(self.open_new_win)



            




        



if __name__ == '__main__':
    root = Tk()
    obj = Admin_login_win(root)
    root.mainloop()