
from tkinter import *

from issue_book_page import Issue_book_page
from collect_book_page import Collect_book_page
from add_book_page import Add_book_page
from remove_book_page import Remove_book_page
from view_book_details_page import View_book_page




class Admin_operations:
    def __init__(self,root):




        



        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1280x800+0+0")
        self.root.minsize(1200,800)

        label_title = Label(self.root,text = "LIBRARY MANAGEMENT SYSTEM",bg ="#e0f0f0",fg="blue",font=("arial",20,"bold"),bd = 12,relief=RIDGE,padx=8,pady=8 )
        label_title.pack(side=TOP,fill=X)


        label_title = Label(self.root,text = "Admin Operations",bg ="#e0f0f0",fg="dark blue",font=("arial",18,"bold"),padx=8,pady=8 )
        label_title.pack(side=TOP,fill=X)

        full_frame= Frame(self.root,bg="#e5f28f",bd=9,relief=RIDGE,height=750,padx=2,pady=2)
        full_frame.pack(side=TOP,fill=X)
        


#  ---------------------button frame----------------
        button_frame = Frame(full_frame,bg="#6be3e1",bd=4,relief="groove",width=200,padx=25,pady=12)
        button_frame.place(x=0,y=0,relheight=1)


        issue_book_button = Button(button_frame,text="Issue Book",font=("arial",12,"bold"),padx=15,width=15,command=self.issue_book_function)
        issue_book_button.grid(row=0,column=0,pady=10)

        collect_book_button = Button(button_frame,text="Collect Book",font=("arial",12,"bold"),padx=15,width=15,command=self.collect_book_function)
        collect_book_button.grid(row=1,column=0,pady=10)

        add_book_button = Button(button_frame,text="Add Book",font=("arial",12,"bold"),padx=15,width=15,command=self.add_book_function)
        add_book_button.grid(row=2,column=0,pady=10)

        remove_book_button = Button(button_frame,text="Remove Book",font=("arial",12,"bold"),padx=15,width=15,command=self.remove_book_function)
        remove_book_button.grid(row=3,column=0,pady=10)

        view_book_button = Button(button_frame,text="Veiw Book Details",font=("arial",12,"bold"),padx=15,width=15,command=self.view_details_function)
        view_book_button.grid(row=4,column=0,pady=10)



        back_button = Button(button_frame,text="Back",font=("arial",12,"bold"),bg="red",padx=15,width=15,command=self.root.destroy)
        back_button.grid(row=5,column=0,pady=10)
        








    def issue_book_function(self):
        self.issue_new_win= Toplevel(self.root)
        self.app_admin = Issue_book_page(self.issue_new_win)


    def collect_book_function(self):
        self.collect_new_win= Toplevel(self.root)
        self.app_admin = Collect_book_page(self.collect_new_win)

    
    def add_book_function(self):
        self.add_new_win= Toplevel(self.root)
        self.app_admin = Add_book_page(self.add_new_win)



    def remove_book_function(self):
        self.remove_new_win= Toplevel(self.root)
        self.app_admin = Remove_book_page(self.remove_new_win)


    def view_details_function(self):
        self.view_new_win = Toplevel(self.root)
        self.app_admin = View_book_page(self.view_new_win)







if __name__ == '__main__':
    root = Tk()
    obj = Admin_operations(root)
    root.mainloop()
