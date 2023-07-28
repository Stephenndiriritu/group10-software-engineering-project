import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import  sqlite3


class login:
    def __init__(self,top):
        self.top=Toplevel()
        self.top.geometry("1500*500")


class MainWindow:
      def __init__(self, master):
       mainframe = tkinter.Frame(master)
       mainframe.pack()


window = tkinter.Tk()



window.title("DATA CAPTURE FORM")
frame = tkinter.Frame(window ,background="green")
frame.pack()

SPU = tkinter.Label(frame,text=" <<-----COLLEGE STUDENT DATA ",font="time 15 bold")
SPU.grid( row=0,column=3)

find_label= tkinter.Label(frame,text="find")
find_label.grid(row=1,column=4 ,padx=30,pady=10)

find = tkinter.Entry(frame,text="search") 
find.grid(row=1,column=3)

find_label= tkinter.Label(frame,text="Treatement Appointment---->>>",font="time 20 bold")
find_label.grid(row=2,column=3 ,padx=30,pady=10)



def submit_data():

    accepted = accepted_terms_var.get()
    Registration_Status = registered_label_var


    if accepted == "Accepted":

        

          firstname= first_name_entry.get()
          lastname = last_name_entry.get()
          if firstname and lastname:
              gender = gender_combobox.get()
              age = age_spinbox.get()
              nationality = nationality_combobox.get()
              NHIF = NHIF_label_combobox.get()
              registered = registered_label_var.get()
              semesters = semesters_spinbox.get()
              studentnumber = student_number_Entry.get()
              accept_terms = accepted_terms_var.get()
              Registration_Status = registered_label_var.get()
              print("First Name:",firstname, "Last Name:",lastname, "gender:",gender)
              print("age:",age,  "Nationality:",  nationality,  "nhif card:",NHIF)
              print("Accept terms & Conditions:",accept_terms)
              print( "Registration Status:",registered,  "Semester:",semesters,  "Student Number:",studentnumber)
              print("-----------------------------------------------")

              #connection with the database
              conn = sqlite3.connect('SPUdata.db')
              table_create_query = '''CREATE TABLE IF NOT EXISTS Student_table(firstname TEXT,lastname TEXT,gender TEXT,age INT,nationality TEXT,NHIF TEXT,registered TEXT,semesters INT,studentnumber INT,accept_terms TEXT)'''
              conn.execute(table_create_query)
              #insert data
              data_insert_query = '''INSERT INTO student_table( firstname,lastname,gender,age,nationality,NHIF,registered,semesters,studentnumber,accept_terms)VALUES(?,?,?,?,?,?,?,?,?,?)'''
              data_insert_tuple =(firstname,lastname,gender,age,nationality,NHIF,registered,semesters,studentnumber,accept_terms)
              
              cursor=conn.cursor()
              cursor.execute(data_insert_query,data_insert_tuple)
              conn.commit()
              conn.close()

          else:tkinter.messagebox.showwarning(title="Error",message="You have not entered your names")
    else: tkinter.messagebox.showwarning(title= "Error",message="You have not accepted terms & Conditions ")

    #sg.theme=('sandy beach')
    #sg.set_options(font=('helvetica 20'),text_color='black')


   

#window=sg.Window('Registration Portal',size=(700,500),resizable=True)
#3window.set_min_size=True

def retrieve_student_records():
    results=[]
    conn= sqlite3('register_students.db')
    c = conn.cursor()
    query= "SELECT full_name,date_of_birth,gender,home_address,phone_contact from register"
    c.excecute(query)







        
        

#saving student information

student_information_frame = tkinter.LabelFrame(frame, text="student information")
student_information_frame.grid(row= 0, column= 0, padx=20, pady=10 )


first_name_label = tkinter.Label(student_information_frame,text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label (student_information_frame, text="Last Name")
last_name_label.grid(row= 0, column =1)


first_name_entry =tkinter.Entry(student_information_frame)
last_name_entry =tkinter.Entry(student_information_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

gender_label = tkinter.Label(student_information_frame ,text="gender")
gender_combobox = ttk.Combobox(student_information_frame, values = ["male","female",])
gender_label.grid(row= 0, column= 2)
gender_combobox.grid(row=1, column = 2)


age_label =tkinter.Label(student_information_frame, text="age")
age_spinbox = tkinter.Spinbox(student_information_frame, from_= 17,to= 60) 
age_label.grid(row=3,column=0)
age_spinbox.grid(row=4, column=0)

nationality_label = tkinter.Label(student_information_frame, text="Nationality")
nationality_combobox = ttk.Combobox(student_information_frame, values=["African","American","Asian","Antarctica","Australian","European"])
nationality_label.grid(row=3, column=1)
nationality_combobox.grid(row=4, column=1)

NHIF_label = tkinter.Label(student_information_frame, text="nhif card")
NHIF_label_combobox = ttk.Combobox(student_information_frame, values=["YES","NO"])
NHIF_label.grid(row=3,column=2)
NHIF_label_combobox.grid(row=4,column=2)

for widget in student_information_frame.winfo_children():
    widget.grid(padx=10, pady=5)


#courses registration information
course_frame = tkinter.LabelFrame(frame)
course_frame.grid(row=1,column=0, sticky="news",padx=20,pady=10)

registered_label_var = tkinter.StringVar( value="Not Registered ")
registered_label= tkinter.Label(course_frame,text="Registration Status")
registered_check = tkinter.Checkbutton(course_frame,text="Currently Registerd" ,variable=registered_label_var,onvalue="registered",offvalue="Not Registered")
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0 )

semesters_label = tkinter.Label(course_frame , text=" Semester")
semesters_spinbox = tkinter.Spinbox(course_frame,from_=0, to="infinity")
semesters_label.grid(row=0,column=1)
semesters_spinbox.grid(row=1, column=1)


student_number_label = tkinter.Label(course_frame ,text="Student Number")
student_number_Entry = tkinter.Entry(course_frame,text="Student Number")
student_number_label.grid(row=0, column=2)
student_number_Entry.grid(row=1, column=2)


for widget in course_frame.winfo_children():
    widget.grid(padx=10, pady=5)


#Accept terms
terms_frame = tkinter.LabelFrame(frame,text="Terms & Conditions")
terms_frame.grid(row=2,column=0,sticky="new",padx=20,pady=20 , )


accepted_terms_var = tkinter.StringVar( value="Not Accepted")
accept_terms = tkinter.Checkbutton(terms_frame ,text= "Accept terms & Conditions" ,variable = accepted_terms_var, onvalue="Accepted", offvalue= "Not Accepted")
accept_terms.grid (row=0,column=0, )



#Enter data

button =tkinter.Button(frame, text = "submit data",command= submit_data)
button.grid(row=3,column=0 ,sticky="news", padx=20,pady=10)



window.mainloop()





