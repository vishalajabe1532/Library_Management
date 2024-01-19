import tkinter.ttk
from tkinter import *
import mysql.connector
import datetime
from tkinter import messagebox



class Remove_book_page:

    def __init__(self,root) :


        # ---------------variables--------------
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.bookauthor_var = StringVar()



        self.root = root
        self.root.title("Remove Book Page")
        self.root.geometry("850x450+261+165")
        self.root.minsize(850,450)
        self.root.maxsize(850,450)


        validate_bookid_func = self.root.register(self.validate_bookid)


        head_label = Label(self.root,text="Remove Book",font=("arial",20,"bold"),bg="#2ba1f0",padx=15,pady=15)
        head_label.pack(side=TOP,fill=X)

        main_frame = Frame(self.root,bg="#7bc0ed",height=400)
        main_frame.pack(side=TOP,fill=X)


        # ----------------------book id------------------
        label_book_id = Label(main_frame, text="Book ID      : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_book_id.grid(row=1, column=0,padx=10,pady=5)
        txt_book_id = Entry(main_frame, font=("arial", 12, "bold"), width=30,textvariable=self.bookid_var,validate="key", validatecommand=(validate_bookid_func, '%P'))
        txt_book_id.grid(row=1, column=1)


        # ------------fetch btn
        fetch_book_button = Button(main_frame,text="Fetch Details",font=("arial",10,"bold"),bg="#1375ed",padx=5,width=10,command=self.fetch_book_details)
        fetch_book_button.grid(row=2,column=1,pady=5,padx=10)



        # ---------------book author------------------------
        label_book_title = Label(main_frame, text="Book Author    : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_book_title.grid(row=3, column=0,padx=10,pady=5)
        txt_book_title = Entry(main_frame, font=("arial", 12, "bold"), width=35,textvariable=self.bookauthor_var)
        txt_book_title.grid(row=3, column=1)


        # ---------------book title------------------------
        label_book_title = Label(main_frame, text="Book Title   : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_book_title.grid(row=4, column=0,padx=10,pady=5)
        txt_book_title = Entry(main_frame, font=("arial", 12, "bold"), width=35,textvariable=self.booktitle_var)
        txt_book_title.grid(row=4, column=1)

        



        back_button = Button(main_frame,text="Back",font=("arial",12,"bold"),bg="red",padx=15,width=15,command=self.root.destroy)
        back_button.grid(row=6,column=1,pady=10)

        remove_button = Button(main_frame,text="Remove Book",font=("arial",12,"bold"),bg="#1375ed",padx=15,width=15,command=self.remove_book_fun)
        remove_button.grid(row=6,column=4,pady=10)



    def fetch_book_details(self):

        bookid = self.bookid_var.get()

        if self.bookid_var.get() == "" :
            messagebox.showwarning("Warning","Please enter ID first")
            return

        try:
            conn=mysql.connector.connect(host="localhost",username = "root", password = "password",database = "library")
            my_cursor = conn.cursor()



            query = "SELECT * FROM book_table WHERE bookid = %s"
            my_cursor.execute(query, (bookid,))
            result = my_cursor.fetchone()
            conn.commit()



            if result is not None:
                
                select_query = "SELECT * FROM book_table WHERE bookid = %s"

                search_value = self.bookid_var.get()
                my_cursor.execute(select_query, (search_value,))

                rows = my_cursor.fetchall()

                for row in rows:
                    self.bookauthor_var.set(row[6])
                    self.booktitle_var.set(row[7])
                
                conn.commit()
                

            else:
                messagebox.showerror("Error","Book with entered ID not present in database")


            my_cursor.close()
            conn.close()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error connecting to MySQL: {error}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()




    def remove_book_fun(self):
        bookid = self.bookid_var.get()

        conn=mysql.connector.connect(host="localhost",username = "root", password = "password",database = "library")
        my_cursor = conn.cursor()



        query = "SELECT * FROM book_table WHERE bookid = %s"
        my_cursor.execute(query, (bookid,))
        result = my_cursor.fetchone()
        conn.commit()



        if result is not None:
            query="DELETE FROM book_table WHERE bookid = %s"
            my_cursor.execute(query,(bookid,))
            conn.commit()
            my_cursor.close()
            conn.close()
            messagebox.showinfo("Success","Book Removed")
            self.root.destroy()

        else:
            messagebox.showerror("Error","Book with entered ID not present in database")

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
    obj = Remove_book_page(root)
    root.mainloop()







