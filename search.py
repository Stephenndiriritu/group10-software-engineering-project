from tkinter import *
import sqlite3
from tkinter import ttk,messagebox


class Filter_studentdata:
    def __init__(self,root):
        self.root=root
        self.root.title("auto filter data")
        self.root.geometry("1350*700+0+0")
        self.root.config(bg="purple")

        title=Label(self.root,text="find student data ",font="comic 20 bold italic ")

        #search panel
        self.var_search= StringVar()
        search_label= Label(self.root,text="search by studentnumber",font=("goudy old style",20))
        search_text=Entry(self.root,textvariable=self.var_search,font=("goudy old style"))
        search_text.place(x=500, y=83,width=300,height=30)
        search_text.bind("<key>",self.search)

        #content 

        self_frame = Frame(self.root,relief=RIDGE)
        self_frame.place(x=300,y=150, width=800,height=350)

        scrollbary=Scrollbar(self_frame,orient=VERTICAL)
        scrollbarx=Scrollbar(self_frame,orient=HORIZONTAL)
        self.studenttable= ttk.Treeview(self_frame,columns=("firstname","lastname","gender","age","nationality","NHIF","registered","semesters","studentnumber","accept_terms"))

        scrollbarx.pack(side=BOTTOM,fill=X)
        scrollbary.pack(side=RIGHT,fill=Y)
        scrollbarx.config(command=self.studenttable.xview)
        scrollbary.config(command=self.studenttable.yview)

        self.studenttable.heading("firstname",text="First Name")
        self.studenttable.heading("lastname",text="Last Name")
        self.studenttable.heading("gender",text="gender")
        self.studenttable.heading("age",text="age")
        self.studenttable.heading("Nationality",text="nationality")
        self.studenttable.heading("nhif card",text="NHIF")
        self.studenttable.heading("Registration Status",text="registered")
        self.studenttable.heading("Semester",text="semesters")
        self.studenttable.heading("Student Number",text="studentnumber")
        self.studenttable.heading("Accept terms & Conditions",text="accept_terms")
        self.studenttable["show"]='headings'
        self.studenttable.column("firstname",width=100)
        self.studenttable.column("lastname",width=100)
        self.studenttable.column("gender",width=100)
        self.studenttable.column("age",width=100)
        self.studenttable.column("Nationality",width=100)
        self.studenttable.column("nhif card",width=100)
        self.studenttable.column("Registration Status",width=100)
        self.studenttable.column("Semester",width=100)
        self.studenttable.column("Student Number",width=100)
        self.studenttable.column("Accept terms & Conditions",width=100)
        self.studenttable.pack(fill=BOTH,expand=1)

        self.show()

        #========================================================

        def add(self):
            con =sqlite3.connect(database="SPUdata.db")
            cur=con.cursor()
            cur.execute("select*from student_data where studentnumber=")
            row=cur.fetchone()
            count=110
            for i in range(20):
                cur.execute("insert into student_data(firstname,lastname,gender,age,nationality,NHIF,registered,semesters,studentnumber,accept_terms)"
                            count,row[1]+")
                con.commit()
                count+=1

        def show(self):
                con=sqlite3.connect(database="SPUdata.db")
                cur=con.cursor()
                try:
                     cur.execute("SELECT *FROM studenttable ")
                     rows=cur.fetchall()
                     self.studenttable.delete(*self.studenttable.get_children())
                     for row in rows:
                      self.studenttable.INSERT('',END,values=row)
                      except Exception as ex:
                      messagebox.showerror("Error",f"Error due to{str(ex)}")

                      def search(self,ev):
                      con=sqlite3.connect(database="SPUdata.db")
                      cur=con.cursor()
                       try:
                       cur.execute("SELECT *FROM Student Number where studentnumber like'%"+self.var_search.get()+"%'")
                       row=cur.fetchall()

                      
                     #print row

                     if len(row)>0:
                     
                        self.studenttable.delete(*self.studenttable.get_children())
                          for i in row:
                               self.studenttable.insert('',END,values=i)
                          else:
                               self.studenttable.delete(*self.studenttable.get_children())
                except Exception as ex:
                     messagebox.showerror("Error",f"Error due to {str(ex)}")


                     root=tk()
                          

                
    
