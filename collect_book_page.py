import tkinter.ttk
from tkinter import *
import mysql.connector
import datetime
from tkinter import messagebox



class Collect_book_page:

    def __init__(self,root) :



        # ---------------variables--------------

        self.bookid_var = StringVar()
        self.prn_var = StringVar()
        self.name_var = StringVar()
        self.booktitle_var = StringVar()
        self.bookauthor_var = StringVar()
        self.dob_var = StringVar()
        self.dor_var = StringVar()
        self.fine_var = StringVar()





        self.root = root
        self.root.title("Issue Page")
        self.root.geometry("850x450+261+165")
        self.root.minsize(850,450)
        self.root.maxsize(850,450)


        validate_bookid_func = self.root.register(self.validate_bookid)


        head_label = Label(self.root,text="Collect Book",font=("arial",20,"bold"),bg="#249ded",padx=15,pady=15)
        head_label.pack(side=TOP,fill=X)

        main_frame = Frame(self.root,bg="#5cb6f2",height=400)
        main_frame.pack(side=TOP,fill=BOTH)


        



        # ----------------------book id------------------
        id_frame = Frame(main_frame,bg="#5cb6f2",height=40,padx=200,pady=10)
        id_frame.pack(side=TOP,fill=X)


        label_book_id = Label(id_frame, text="Book ID              : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=8)
        label_book_id.grid(row=0, column=3,padx=9,pady=5)
        txt_book_id = Entry(id_frame, font=("arial", 12, "bold"), width=25,textvariable=self.bookid_var,validate="key", validatecommand=(validate_bookid_func, '%P'))
        txt_book_id.grid(row=0, column=4,pady=5)


# --------------fetch btn-------------------
        fetch_button = Button(id_frame,text="Fetch Details",font=("arial",10,"bold"),bg="#045dc2",padx=5,width=10,command=self.fetch_details)
        fetch_button.grid(row=1,column=4,pady=5)



# ***********************8details frame**************************888
        detail_frame = Frame(main_frame,bg="#86caf7",bd=4,height=323)
        detail_frame.pack(side=TOP,fill=X)


    
        


        # ------------prn no----------------
        label_PRN = Label(detail_frame, text="PRN No.          : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=13,padx=2)
        label_PRN.grid(row=0, column=0, sticky=W,padx=5,pady=5)
        txt_PRN_No = Entry(detail_frame, font=("arial", 12, "bold"),textvariable=self.prn_var, width=25 )
        txt_PRN_No.grid(row=0, column=1,padx=5)

        # -------------name------------------
        label_name = Label(detail_frame,text="Name               : ",font=("arial",12,"bold"),bg="#e0f0f0",width = 13,padx=2)
        label_name.grid(row=1,column=0,sticky=W,padx=5,pady=5)
        txt_name = Entry(detail_frame,font=("arial", 12, "bold"),textvariable=self.name_var,width=25)
        txt_name.grid(row=1,column=1,padx=5)





        # ---------------book title------------------------
        label_book_title = Label(detail_frame, text="Book Title   : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_book_title.grid(row=0, column=2,padx=10,pady=5)
        txt_book_title = Entry(detail_frame, font=("arial", 12, "bold"), width=25,textvariable=self.booktitle_var)
        txt_book_title.grid(row=0, column=3,padx=5)


        # ---------------book author------------------------
        label_book_title = Label(detail_frame, text="Book Author   : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_book_title.grid(row=1, column=2,padx=5,pady=5)
        txt_book_title = Entry(detail_frame, font=("arial", 12, "bold"), width=25,textvariable=self.bookauthor_var)
        txt_book_title.grid(row=1, column=3,padx=5)


        # -------------------------------date borrowed--------------
        label_dob = Label(detail_frame, text="Date borrowed  : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=13, padx=4)
        label_dob.grid(row=2, column=0,padx=5,pady=5)
        txt_dob = Entry(detail_frame, font=("arial", 12, "bold"), width=25,textvariable=self.dob_var)
        txt_dob.grid(row=2, column=1,padx=5)


         # -------------------------------date of return--------------
        label_dor = Label(detail_frame, text="Date of return : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_dor.grid(row=2, column=2,padx=5,pady=5)
        txt_dor = Entry(detail_frame, font=("arial", 12, "bold"), width=25,textvariable=self.dor_var)
        txt_dor.grid(row=2, column=3,padx=5)


         # -------------------------------fine--------------
        label_fine = Label(detail_frame, text="Late return Fine : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=13, padx=4)
        label_fine.grid(row=3, column=0,padx=5,pady=5)
        txt_fine = Entry(detail_frame, font=("arial", 12, "bold"), width=25,textvariable=self.fine_var)
        txt_fine.grid(row=3, column=1,padx=5)


        back_button = Button(detail_frame,text="Back",font=("arial",12,"bold"),bg="red",padx=15,width=15,command=self.root.destroy)
        back_button.grid(row=4,column=1,pady=20)

        renew_button = Button(detail_frame,text="Re-New",font=("arial",12,"bold"),bg="#84f542",padx=15,width=15,command=self.renew_book_fun)
        renew_button.grid(row=4,column=2,pady=20)

        collect_button = Button(detail_frame,text="Collect",font=("arial",12,"bold"),bg="#045dc2",padx=15,width=15,command=self.collect_book_fun)
        collect_button.grid(row=4,column=3,pady=20)



    def fetch_details(self):

        if self.bookid_var.get() == "" :
            messagebox.showwarning("Warning","Please enter ID first")
            return
        

        try:
            conn=mysql.connector.connect(host="localhost",username = "root", password = "password",database = "library")
            my_cursor = conn.cursor()
            select_query = "SELECT * FROM book_table WHERE bookid = %s"
            

            search_value = self.bookid_var.get()
            my_cursor.execute(select_query, (search_value,))

            rows = my_cursor.fetchall()

            if len(rows) == 0:
                messagebox.showerror("Error","Book not present in labrary")
                return

            for row in rows:
                if row[0] == None :
                    messagebox.showinfo("Info","Book not issued to anyone")
                    return
                
                self.prn_var.set(row[0])
                self.name_var.set(row[1])
                self.bookauthor_var.set(row[6])
                self.booktitle_var.set(row[7])
                self.dob_var.set(row[8])
                self.dor_var.set(row[9])


                d1 = row[9]
                d2 = datetime.date.today()

                extra_days = (d2 - d1).days

                if extra_days > 0 :
                    fine = extra_days * 5
                    self.fine_var.set(str(fine))
                else:
                    self.fine_var.set("0")

            conn.commit()

            my_cursor.close()
            conn.close()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error connecting to MySQL: {error}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()



    def collect_book_fun(self):

        try:
            conn=mysql.connector.connect(host="localhost",username = "root", password = "password",database = "library")
            my_cursor = conn.cursor()

            select_query = "SELECT * FROM book_table WHERE bookid = %s"
            

            search_value = self.bookid_var.get()
            my_cursor.execute(select_query, (search_value,))

            rows = my_cursor.fetchall()

            for row in rows:
                if row[0] == None :
                    messagebox.showinfo("Info","Book not issued to anyone")
                    return            

            update_query = "UPDATE book_table SET prn = %s, name = %s, branch = %s, year = %s ,mono = %s,dob = %s,dor = %s WHERE bookid = %s"

    
            prn = None
            name = None
            branch =  None
            year = None
            mono = None
            dob = None
            dor = None
            row_id = self.bookid_var.get()



            my_cursor.execute(update_query, (prn,name,branch,year,mono,dob,dor, row_id))
            conn.commit()


            my_cursor.close()
            conn.close()

            messagebox.showinfo("Success","Book collected, data updated successfully")
            self.root.destroy()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error connecting to MySQL: {error}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()



    def renew_book_fun(self):

        try:
            conn=mysql.connector.connect(host="localhost",username = "root", password = "password",database = "library")
            my_cursor = conn.cursor()

            select_query = "SELECT * FROM book_table WHERE bookid = %s"
            

            search_value = self.bookid_var.get()
            my_cursor.execute(select_query, (search_value,))

            rows = my_cursor.fetchall()

            for row in rows:
                if row[0] == None :
                    messagebox.showinfo("Info","Book not issued to anyone")
                    return            

            update_query = "UPDATE book_table SET dob = %s,dor = %s WHERE bookid = %s"

    
            dob = datetime.date.today()
            d2 = datetime.timedelta(days=10)
            dor = dob + d2
            row_id = self.bookid_var.get()



            my_cursor.execute(update_query, (dob,dor, row_id))
            conn.commit()


            my_cursor.close()
            conn.close()

            messagebox.showinfo("Success","Book renewed, data updated successfully")
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
    obj = Collect_book_page(root)
    root.mainloop()











