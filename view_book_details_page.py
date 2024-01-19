import tkinter.ttk
from tkinter import *
import mysql.connector
from tkinter import messagebox





class View_book_page:

    def __init__(self,root) :
        self.root = root
        self.root.title("View Book Details")
        self.root.geometry("850x450+261+165")
        self.root.minsize(850,450)
        self.root.maxsize(850,450)

        self.search_var = StringVar()



        head_label = Label(self.root,text="Book Details",font=("arial",20,"bold"),bg="#3ea7ed",padx=15,pady=15)
        head_label.pack(side=TOP,fill=X)


        main_frame = Frame(self.root,bg="#a2d7fa",height=600)
        main_frame.pack(side=TOP,fill=BOTH)


        search_frame= Frame(main_frame,bg="#a2d7fa",height=80)
        search_frame.pack(side=TOP,fill=X)

        txt_label = Label(search_frame,text="Enter Book Title/Author Name :",font=("arial",10,"bold"),padx=10,pady=2)
        txt_label.grid(row=0,column=0,padx=10,pady=6)

        search_entry = Entry(search_frame,textvariable=self.search_var,font=("arial",10,"bold"))
        search_entry.grid(row=0,column=1,padx=10,pady=6)

        search_button = Button(search_frame, text="Search",font=("arial",10,"bold"), bg="#1871de",command=self.perform_search)
        search_button.grid(row=0,column=3,padx=10,pady=6)


        reset_button = Button(search_frame, text="Display all Data",font=("arial",10,"bold"), bg="#1871de",command=self.fetch_data)
        reset_button.grid(row=0,column=5,padx=10,pady=6)




        table_frame=Frame(main_frame,bd=2,relief=RIDGE,padx=2,bg="#e0f0f0",height=400)
        table_frame.pack(side=TOP,fill=X)

        back_button = Button(main_frame,text="Back",font=("arial",12,"bold"),bg="red",padx=15,width=15,command=self.root.destroy)
        back_button.pack(side=TOP,pady=30)

        table_scroll_bar_x = tkinter.ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        table_scroll_bar_y = tkinter.ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.library_table=tkinter.ttk.Treeview(table_frame,column=("prn","name","branch","year","mo_no","bookid","bookauthor","booktitle","dateborrowed","dateofreturn"),xscrollcommand=table_scroll_bar_x.set,yscrollcommand=table_scroll_bar_y.set)


        table_scroll_bar_x.pack(side=BOTTOM,fill=X)
        table_scroll_bar_y.pack(side=RIGHT,fill=Y)

        table_scroll_bar_x.config(command=self.library_table.xview)
        table_scroll_bar_y.config(command=self.library_table.yview)
        self.library_table.heading("prn",text="PRN")
        self.library_table.heading("name", text="Name")
        self.library_table.heading("branch", text="Branch")
        self.library_table.heading("year", text="Year")
        self.library_table.heading("mo_no", text="Mo. No.")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("bookauthor", text="Book Author")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("dateborrowed", text="Date borrowed")
        self.library_table.heading("dateofreturn", text="Date of Return")
        

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


        self.library_table.column("prn", width=100)
        self.library_table.column("name",width=120 )
        self.library_table.column("branch",width=120)
        self.library_table.column("year", width=120)
        self.library_table.column("mo_no",width=120 )
        self.library_table.column("bookid",width=120 )
        self.library_table.column("bookauthor",width=150 )
        self.library_table.column("booktitle",width=230 )
        self.library_table.column("dateborrowed", width=120)
        self.library_table.column("dateofreturn", width=120)


        self.fetch_data()




    def fetch_data(self):
            
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password ="password",database ="library")
            my_cursor  = conn.cursor()
            my_cursor.execute("select * from library.book_table")
            rows= my_cursor.fetchall()

            if len(rows) != 0:
                self.library_table.delete(*self.library_table.get_children())
                for t in rows:
                    self.library_table.insert("",END,values=t)
                conn.commit()

            my_cursor.close()
            conn.close()
        
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error connecting to MySQL: {error}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()


    def perform_search(self):

        search_keywords = self.search_var.get()

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="password", database="library")
            my_cursor = conn.cursor()

            query = "SELECT * FROM book_table WHERE booktitle LIKE %s OR bookauthor LIKE %s"
            my_cursor.execute(query, ('%' + search_keywords + '%', '%' + search_keywords + '%'))

            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.library_table.delete(*self.library_table.get_children())
                for t in rows:
                    self.library_table.insert("", END, values=t)
                conn.commit()
            else:
                messagebox.showinfo("Search Results", "No matching records found.")

            my_cursor.close()
            conn.close()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error connecting to MySQL: {error}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()




if __name__ == '__main__':
    root = Tk()
    obj = View_book_page(root)
    root.mainloop()







