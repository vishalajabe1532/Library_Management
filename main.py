import tkinter.ttk
from tkinter import *
from admin_login_page import Admin_login_win






class Welcome_page:

    def __init__(self,root) :
        self.root = root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1280x800+0+0")
        self.root.minsize(800,400)


        bgimg=PhotoImage(file = "welcome_image.gif")

        bg_label = Label(self.root, image=bgimg)
        bg_label.place(x=0,y=0,relheight=1,relwidth=1)


        full_frame = Frame(self.root,bg="#e6e7f7",border=3,relief="groove")
        full_frame.pack(side=TOP,fill=Y,pady=100)

        
        head_txt_label = Label(full_frame,text="LIBRARY MANAGEMENT",font=("arial",30,"bold"),fg="#0b17bd",bg="#e6e7f7")
        head_txt_label.pack(side=TOP,padx=50)


        instruct_txt_label = Label(full_frame,text="\nThis is a RPPOOP Project Developed by-\n Anuj Abhang : 112103003\nVishal Ajabe : 112103007",font=("arial",10,"bold"),fg="black",bg="#e6e7f7")
        instruct_txt_label.pack(side=TOP,padx=50)



        login_frame = Frame(full_frame,border=4,bg="#bdc1f2")
        login_frame.pack(side=TOP,pady=5,fill=X)

        admin_select_button = Button(login_frame,text="ADMIN LOGIN",command=self.admin_login,font=("arial",10,"bold"),bg="#9ca1f0",width=50,padx=45)
        admin_select_button.grid(row=0,column=0,padx=30,pady=30)

        # student_select_button = Button(login_frame,text="STUDENT",font=("arial",10,"bold"),bg="#9ca1f0",width=20,padx=45)
        # student_select_button.grid(row=0,column=1,padx=13,pady=6)


        exit_button = Button(login_frame,text="Exit",font=("arial",10,"bold"),bg="#fc5a03",width=20,padx=45,command=self.root.destroy)
        exit_button.grid(row=1,column=0,padx=33,pady=17)




        self.root.mainloop()



    def admin_login(self):
        self.new_win= Toplevel(self.root)
        self.app_admin = Admin_login_win(self.new_win)
       




    




if __name__ == '__main__':
    root = Tk()
    obj = Welcome_page(root)
    # root.mainloop()