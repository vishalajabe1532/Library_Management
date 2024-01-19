import tkinter.ttk
from tkinter import *
import mysql.connector
import datetime
from tkinter import messagebox






class Add_book_page:

    def __init__(self,root) :


        # ---------------variables--------------
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.bookauthor_var = StringVar()



        self.root = root
        self.root.title("Add Page")
        self.root.geometry("850x450+261+165")
        self.root.minsize(850,450)
        self.root.maxsize(850,450)



        validate_bookid_func = self.root.register(self.validate_bookid)



        head_label = Label(self.root,text="Add Book",font=("arial",20,"bold"),bg="#169cf5",padx=15,pady=15)
        head_label.pack(side=TOP,fill=X)

        main_frame = Frame(self.root,bg="#86caf7",height=900)
        main_frame.pack(side=TOP,fill=X)


        # ----------------------book id------------------
        label_book_id = Label(main_frame, text="Book ID      : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_book_id.grid(row=1, column=0,padx=10,pady=5)
        txt_book_id = Entry(main_frame, font=("arial", 12, "bold"), width=30,textvariable=self.bookid_var,validate="key", validatecommand=(validate_bookid_func, '%P'))
        txt_book_id.grid(row=1, column=1)



        # ---------------book author------------------------
        label_book_title = Label(main_frame, text="Book Author    : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_book_title.grid(row=2, column=0,padx=10,pady=5)
        txt_book_title = Entry(main_frame, font=("arial", 12, "bold"), width=30,textvariable=self.bookauthor_var)
        txt_book_title.grid(row=2, column=1)


        # ---------------book title------------------------
        label_book_title = Label(main_frame, text="Book Title   : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_book_title.grid(row=3, column=0,padx=10,pady=5)
        txt_book_title = Entry(main_frame, font=("arial", 12, "bold"), width=30,textvariable=self.booktitle_var)
        txt_book_title.grid(row=3, column=1)

        



        back_button = Button(main_frame,text="Back",font=("arial",12,"bold"),bg="red",padx=15,width=15,command=self.root.destroy)
        back_button.grid(row=6,column=1,pady=20)

        add_button = Button(main_frame,text="Add Book",font=("arial",12,"bold"),bg="#1375ed",padx=15,width=15,command=self.add_book_fun)
        add_button.grid(row=6,column=4,pady=20)



    def add_book_fun(self):
        bookid = self.bookid_var.get()
        bookauthor = self.bookauthor_var.get()
        booktitle = self.booktitle_var.get()
        if "" in  (bookid,bookauthor,booktitle):
            messagebox.showerror("Error","Please enter details first")
            return
        
            
        try:
            conn=mysql.connector.connect(host="localhost",username = "root", password = "password",database = "library")
            my_cursor = conn.cursor()



            query = "SELECT * FROM book_table WHERE bookid = %s"
            my_cursor.execute(query, (bookid,))
            result = my_cursor.fetchone()
            conn.commit()



            if result is not None:
                messagebox.showwarning("Warning","Book with same ID already present.\nPlease change ID.")
                return
                
            else:
                try:
                    query = "INSERT INTO book_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
                    prn = None
                    name = None
                    branch = None
                    year = None
                    mono = None
                    dob = None
                    dor = None
                    my_cursor.execute(query, (prn, name, branch, year, mono, bookid, bookauthor, booktitle, dob,dor))
                    conn.commit()
                    messagebox.showinfo("Success", "Book added successfully!")
                except mysql.connector.Error as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
            my_cursor.close()
            conn.close()
            self.root.destroy()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error connecting to MySQL: {error}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()


    def validate_bookid(self,text):
        if text=="" or text.isdigit():
            return True
        else:
            messagebox.showwarning("Warning","Enter integer only ")
            return False




if __name__ == '__main__':
    root = Tk()
    obj = Add_book_page(root)
    root.mainloop()







