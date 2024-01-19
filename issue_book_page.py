import tkinter.ttk
from tkinter import *
import mysql.connector
import datetime
from tkinter import messagebox






class Issue_book_page:

    def __init__(self,root) :



        # ---------------variables--------------
        self.prn_var = StringVar()
        self.name_var = StringVar()
        self.branch_var = StringVar()
        self.year_var = StringVar()
        self.mono_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.bookauthor_var = StringVar()
        self.dob_var = StringVar()
        self.dor_var = StringVar()
        



        self.root = root
        self.root.title("Issue Page")
        self.root.geometry("850x450+261+165")
        self.root.minsize(850,450)
        self.root.maxsize(850,450)


        validate_prn_func = self.root.register(self.validate_prn)
        validate_mono_func = self.root.register(self.validate_mono)
        validate_bookid_func = self.root.register(self.validate_bookid)



        head_label = Label(self.root,text="Issue Book",font=("arial",20,"bold"),bg="#49b0f5",padx=15,pady=15)
        head_label.pack(side=TOP,fill=X)

        main_frame = Frame(self.root,bg="#87c9f5",height=400)
        main_frame.pack(side=TOP,fill=X)





        # ------------prn no----------------
        label_PRN = Label(main_frame, text="PRN No.          : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12,padx=2)
        label_PRN.grid(row=1, column=0, sticky=W,padx=5,pady=5)
        txt_PRN_No = Entry(main_frame, font=("arial", 12, "bold"),textvariable=self.prn_var, width=25 ,validate="key", validatecommand=(validate_prn_func, '%P'))
        txt_PRN_No.grid(row=1, column=1)

        # -------------name------------------
        label_name = Label(main_frame,text="Name               : ",font=("arial",12,"bold"),bg="#e0f0f0",width = 12,padx=2)
        label_name.grid(row=2,column=0,sticky=W,padx=5,pady=5)
        txt_name = Entry(main_frame,font=("arial", 12, "bold"),textvariable=self.name_var,width=25)
        txt_name.grid(row=2,column=1)

        # -----------------branch------------
        label_branch = Label(main_frame,text="Branch            : ",font=("arial", 12, "bold"),bg="#e0f0f0",width=12,padx=2)
        label_branch.grid(row=3,column=0,padx=5,pady=5)
        combo_branch = tkinter.ttk.Combobox(main_frame,font=("arial", 12, "bold"),textvariable=self.branch_var,width=23,state="readonly")
        combo_branch["value"] = ("Civil","Computer","Electrical","Electronics and Telecommunication","Instrumentation","Mechanical","Metallurgy","Production")
        combo_branch.grid(row=3,column= 1)



        # -------------year------------
        label_mo_no = Label(main_frame, text="Year                  : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=2)
        label_mo_no.grid(row=4, column=0,padx=5,pady=5)
        combo_year = tkinter.ttk.Combobox(main_frame,font=("arial", 12, "bold"),textvariable=self.year_var,width=23,state="readonly")
        combo_year["value"] = ("First Year","Second Year","Third Year","Fourth Year","M. Tech")
        combo_year.grid(row=4,column= 1)



        # ----------------------mo no-------------------
        label_mo_no=Label(main_frame,text="Mobile No.      : ",font=("arial", 12, "bold"),bg="#e0f0f0",width = 12,padx=2)
        label_mo_no.grid(row=5,column=0,padx=5,pady=5)
        txt_mo_no = Entry(main_frame,font=("arial", 12, "bold"),textvariable=self.mono_var,width=25,validate="key", validatecommand=(validate_mono_func, '%P'))
        txt_mo_no.grid(row=5,column=1,padx=5)



        # ----------------------book id------------------
        label_book_id = Label(main_frame, text="Book ID              : ", font=("arial", 12, "bold"), bg="#e0f0f0",
                            width=12, padx=4)
        label_book_id.grid(row=1, column=2,padx=5,pady=5)
        txt_book_id = Entry(main_frame, font=("arial", 12, "bold"), textvariable=self.bookid_var,width=25,validate="key", validatecommand=(validate_bookid_func, '%P'))
        txt_book_id.grid(row=1, column=3)



        fetch_book_button = Button(main_frame,text="Fetch Details",font=("arial",10,"bold"),bg="#096ad9",padx=5,width=10,command=self.fetch_title_author)
        fetch_book_button.grid(row=1,column=4,pady=5)


        # ---------------book title------------------------
        label_book_title = Label(main_frame, text="Book Title      : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_book_title.grid(row=2, column=2,padx=5,pady=5)
        txt_book_title = Entry(main_frame, font=("arial", 12, "bold"), width=25,textvariable=self.booktitle_var)
        txt_book_title.grid(row=2, column=3)


        # ---------------book author------------------------
        label_book_title = Label(main_frame, text="Book Author   : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_book_title.grid(row=3, column=2,padx=5,pady=5)
        txt_book_title = Entry(main_frame, font=("arial", 12, "bold"), width=25,textvariable=self.bookauthor_var)
        txt_book_title.grid(row=3, column=3)


        # -------------------------------do borrowed--------------
        label_dob = Label(main_frame, text="Date borrowed  : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_dob.grid(row=4, column=2,padx=5,pady=5)
        txt_dob = Entry(main_frame, font=("arial", 12, "bold"), width=25,textvariable=self.dob_var)
        txt_dob.grid(row=4, column=3)


        # -------------------------------date of return--------------
        label_dor = Label(main_frame, text="Date of Return  : ", font=("arial", 12, "bold"), bg="#e0f0f0",width=12, padx=4)
        label_dor.grid(row=5, column=2,padx=10,pady=5)
        txt_dor = Entry(main_frame, font=("arial", 12, "bold"), width=25,textvariable=self.dor_var)
        txt_dor.grid(row=5, column=3)


        # -------------------------------late return fine--------------
        label_fine = Label(main_frame, text="Note : Late return Fine -> Rs.5 per extended day ", font=("arial", 12, "bold"), bg="#e0f0f0",width=40, padx=4)
        label_fine.grid(row=6, column=0,columnspan=3,padx=5,pady=5)
        # txt_fine = Label(main_frame,text="" ,font=("arial", 12, "bold"), width=22)
        # txt_fine.grid(row=6, column=4)



        back_button = Button(main_frame,text="Back",font=("arial",12,"bold"),bg="red",padx=15,width=15,command=self.root.destroy)
        back_button.grid(row=7,column=1,pady=10)



        issue_button = Button(main_frame,text="Issue",font=("arial",12,"bold"),bg="#096ad9",padx=15,width=15,command=self.add_data)
        issue_button.grid(row=7,column=3,pady=10)



    def add_data(self):


        prn = self.prn_var.get()
        name = self.name_var.get()
        branch = self.branch_var.get()
        year = self.year_var.get()
        mono = self.mono_var.get()
        dob = self.dob_var.get()
        dor = self.dor_var.get()
        bookid = self.bookid_var.get()

        if "" in (prn, name, branch, year, mono, dob,dor, bookid):
            messagebox.showwarning("Warning", "Data cannot be added. Please fill in all the fields.")
            return
        if len(prn) <9:
            messagebox.showwarning("Warning", "Length of PRN no. should be 9")
            return
        if len(mono) <10:
            messagebox.showwarning("Warning", "Length of Mobile no. should be 10")
            return
        try:
            conn=mysql.connector.connect(host="localhost",username = "root", password = "password",database = "library")
            my_cursor = conn.cursor()

            query = "SELECT * FROM book_table WHERE bookid = %s"
            my_cursor.execute(query, (bookid,))
            result = my_cursor.fetchall()
            conn.commit()

            print(result)

            for row in result:
                if row[0] != None:
                    messagebox.showerror("Error","Book already issued.")
                    my_cursor.close()
                    conn.close()
                    return


                update_query = "UPDATE book_table SET prn = %s, name = %s, branch = %s, year = %s ,mono = %s,dob = %s,dor = %s WHERE bookid = %s"

                my_cursor.execute(update_query, (prn,name,branch,year,mono,dob,dor, bookid))
                conn.commit()

                my_cursor.close()
                conn.close()

                # print("data added\n")
                messagebox.showinfo("Success","Data added successfully")
                self.root.destroy()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error connecting to MySQL: {error}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()



    

    def fetch_title_author(self):


        try:
            conn=mysql.connector.connect(host="localhost",username = "root", password = "password",database = "library")
            my_cursor = conn.cursor()
            select_query = "SELECT * FROM book_table WHERE bookid = %s"

            # Example value to search for
            search_value = self.bookid_var.get()
            if search_value =="":
                messagebox.showwarning("Warning","Please enter Book ID")
                return
            my_cursor.execute(select_query, (search_value,))

            rows = my_cursor.fetchall()

            if len(rows) == 0:
                messagebox.showerror("Error","Book not present in labrary")
                return


            for row in rows:
                self.bookauthor_var.set(row[6])
                self.booktitle_var.set(row[7])
                

                d1 = datetime.date.today()
                self.dob_var.set(d1)
                d2 = datetime.timedelta(days=10)
                d3 = d1 + d2
                self.dor_var.set(d3)
                

            conn.commit()

            my_cursor.close()
            conn.close()
        

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error connecting to MySQL: {error}")

        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()



    def validate_prn(self,text):
        if len(text) >9:
            messagebox.showwarning("Warning","Max 9 integer only ")
            return False
        if text=="" or text.isdigit():
            return True
        else:
            messagebox.showwarning("Warning","Enter integer only ")
            return False

        
    def validate_mono(self,text):
        if len(text) >10:
            messagebox.showwarning("Warning","Mobile no. can be max 10 digits only ")
            return False
        if text=="" or text.isdigit():
            return True
        else:
            messagebox.showwarning("Warning","Enter integer only ")
            return False
        
    def validate_bookid(self,text):
        if text=="" or text.isdigit():
            return True
        else:
            messagebox.showwarning("Warning","Enter integer only ")
            return False
    



if __name__ == '__main__':
    root = Tk()
    obj = Issue_book_page(root)
    root.mainloop()












