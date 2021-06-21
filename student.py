##===================================== Student Management System =================================================##

from tkinter import*
from tkinter import ttk
import sqlite3 as db,sys
import studentdata
from tkinter import messagebox, filedialog
import pandas as pd

root=Tk()
root.geometry("1350x750")
root.iconbitmap('./icon/logo.ico')
root.title("KINGMAKER")
root.configure(bg='gold')
title=Label(root,text="STUDENT MANAGEMENT SYSTEM",
            relief=GROOVE,font=("times new roman",40,"bold"),bg="light yellow",fg="gold2")
title.pack(side=TOP,fill=X)


##==============================================Varibles==============================================##

std_id=StringVar()
first_name=StringVar()
sur_name=StringVar()
dob=StringVar()
age=StringVar()
gender=StringVar()
address=StringVar()
mobile=StringVar()


##==============================================Function=============================================##

def iexit():
    i=messagebox.askyesno("Student Data Management","config if you want to exit")
    if i>0:
      sys.exit() 
     
def fetch_data():
    con=db.connect("datafile")
    cur=con.cursor()
    cur.execute("SELECT* FROM student")
    rows=cur.fetchall()
    if len(rows)!=0:
        std_list.delete(*std_list.get_children())
        for row in rows:
            std_list.insert('',END,values=row)
    con.commit()
    con.close()
    
def cleardata():
    text_std_id.delete(0,END)
    text_first_name.delete(0,END)
    text_sur_name.delete(0,END)
    text_dob.delete(0,END)
    text_age.delete(0,END)
    text_gender.set('')
    text_address.delete(0,END)
    text_mobile.delete(0,END)
   

def adddata():
    try:
        if(std_id.get()=="" or first_name.get()=="" or sur_name.get()=="" or dob.get()=="" or
           age.get()=="" or gender.get()=="" or address.get()=="" or mobile.get()==""):
            messagebox.showerror("Erro","All Fields are Required")
        else:
            studentdata.addnew(std_id.get(),first_name.get(),sur_name.get(),
                               dob.get(),age.get(),gender.get(),address.get(),mobile.get())
            cleardata()
            fetch_data()
    except:
        messagebox.showerror("Notification","Roll No. Already Exist Try Another Id....")
        

def displaydata():
    fetch_data()


def studentrec(event):
    global sd
    searchstd=std_list.delete(0,END)
    sd=std_list.get(searchstd)
    
    text_std_id.delete(0,END)
    text_std_id.insert(END,sd[1])
    text_first_name.delete(0,END)
    text_first_name.insert(END,sd[2])
    text_sur_name.delete(0,END)
    text_sur_name.insert(END,sd[3])
    text_dob.delete(0,END)
    text_dob.insert(END,sd[4])
    text_age.delete(0,END)
    text_age.insert(END,sd[5])
    text_gender.delete(0,END)
    text_gender.insert(END,sd[6])
    text_address.delete(0,END)
    text_address.insert(END,sd[7])
    text_mobile.delete(0,END)
    text_mobile.insert(END,sd[8])
    
def deletedata():
    if(len(std_id.get())!=0):
        studentdata.delete(std_id.get())
    fetch_data()
    cleardata()

def searchdata():
    con=db.connect("datafile")
    cur=con.cursor()
    
    if(std_id.get()):
       cur.execute("select * from student where std_id=?",\
                (std_id.get(),))
       
    elif(first_name.get()):
       cur.execute("select * from student where first_name=?",\
                (first_name.get(),))
    
    elif(sur_name.get()):
       cur.execute("select * from student where sur_name=?",\
                (sur_name.get(),))

    elif(dob.get()):
       cur.execute("select * from student where dob=?",\
                (dob.get(),))

    elif(age.get()):
       cur.execute("select * from student where age=?",\
                (age.get(),))

    elif(gender.get()):
       cur.execute("select * from student where gender=?",\
                (gender.get(),))

    elif(address.get()):
       cur.execute("select * from student where address=?",\
                (address.get(),))

    elif(mobile.get()):
       cur.execute("select * from student where mobile=?",\
                (mobile.get(),))
    
    rows=cur.fetchall()
    if len(rows)!=0:
        std_list.delete(*std_list.get_children())
        for row in rows:
            std_list.insert('',END,values=row)
    con.commit()
    text_first_name.delete(0,END)
    text_sur_name.delete(0,END)
    text_dob.delete(0,END)
    text_age.delete(0,END)
    text_gender.delete(0,END)
    text_address.delete(0,END)
    text_mobile.delete(0,END)
    
def updatedata():
    if(len(std_id.get())!=0):
        studentdata.delete(std_id.get())
    if(len(std_id.get())!=0):
        studentdata.addnew(std_id.get(),first_name.get(),sur_name.get(),dob.get(),age.get(),
                           gender.get(),address.get(),mobile.get())
    cleardata()
    fetch_data()

def exportdata():
        ff = filedialog.asksaveasfilename()
        gg = std_list.get_children()
        std_id,first_name,sur_name,dob,age,gender,address,mobile=[],[],[],[],[],[],[],[]
        for i in gg:
            content = std_list.item(i)
            pp = content['values']
            std_id.append(pp[0]),first_name.append(pp[1]),sur_name.append(pp[2]),dob.append(pp[3]),age.append(pp[4]),
            gender.append(pp[5]),address.append(pp[6]),mobile.append(pp[7])
        dd = ['Roll No.','First Name','Surname','D.O.B','Age','Gender','Address','Mobile No.']
        df = pd.DataFrame(list(zip(std_id,first_name,sur_name,dob,age,gender,address,mobile)),columns=dd)
        paths = r'{}.csv'.format(ff)
        df.to_csv(paths.format(ff,),index=False)
        messagebox.showinfo('Notification', 'Student Data Saved{}......'.format(paths))
        

def get_cursor(ev):
    try:
        cursor_rows=std_list.focus()
        contents=std_list.item(cursor_rows)
        row=contents['values']
        std_id.set(row[0])
        first_name.set(row[1])
        sur_name.set(row[2])
        dob.set(row[3])
        age.set(row[4])
        gender.set(row[5])
        address.set(row[6])
        mobile.set(row[7])
    except:
        return 0


##==============================================Frames============================================================##

mainframe=Frame(root,bd=4,relief=RIDGE,bg="deep sky blue")
mainframe.place(x=20,y=100,width=530,height=600)

dataframeleft=LabelFrame(mainframe,bd=1,width="400",height="700" ,padx=35,pady=3,relief=GROOVE,bg="light sky blue",
                         fg="dark slate blue",font=('times new roman',20,'bold'),text="Students INFO")
dataframeleft.pack(side=TOP)

buttonframe=Frame(mainframe,bd=0,relief=RIDGE,bg="light sky blue")
buttonframe.place(x=0.5,y=496,width=520,height=94)

a=Frame(root,bd=4,relief=GROOVE,bg="gold2")
a.place(x=560,y=100,width=780,height=600)

dataframeright=LabelFrame(a,bd=1,width="780",height="700" ,padx="20",relief=RIDGE,bg="snow",fg="dark slate blue",
                          font=('times new roman',20,'bold'),text="Students Details")
dataframeright.pack(side=TOP)


##==============================================Table Frame============================================================##

table_frame=Frame(dataframeright,bd=4,relief=RIDGE,bg="black")
table_frame.place(x=9,y=10,width=730,height=530)

scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=Scrollbar(table_frame,orient=VERTICAL)
std_list=ttk.Treeview(table_frame,columns=("std_id","first_name","sur_name","dob","age","gender","address","mobile"),
                      xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=std_list.xview)
scroll_y.config(command=std_list.yview)
std_list.heading("std_id",text="Roll No")
std_list.heading("first_name",text="First Name")
std_list.heading("sur_name",text="Surname")
std_list.heading("dob",text="D.O.B.")
std_list.heading("age",text="Age")
std_list.heading("gender",text="Gender")
std_list.heading("address",text="Address")
std_list.heading("mobile",text="Mobile")

std_list['show']='headings'
std_list.column("std_id",width=25)
std_list.column("first_name",width=70)
std_list.column("sur_name",width=100)
std_list.column("dob",width=40)
std_list.column("age",width=10)
std_list.column("gender",width=30)
std_list.column("address",width=150)
std_list.column("mobile",width=50)

std_list.pack(fill=BOTH,expand=1)
std_list.bind("<ButtonRelease-1>",get_cursor)


##========================================================label and Entry Area========================================##

label_std_id=Label(dataframeleft,font=("times new roman",20,"bold"),text="Roll No",bg="red",fg="white")
label_std_id.grid(row=0,column=0,pady=1,padx=1,stick="w")
text_std_id=Entry(dataframeleft,font=('arial',17,'bold'),textvariable=std_id,width=22,bd=5,relief=GROOVE)
text_std_id.grid(row=0,column=1,pady=1,padx=15,stick="w")
        
label_first_name=Label(dataframeleft,font=("times new roman",20,"bold"),text="First Name",bg="red",fg="white")
label_first_name.grid(row=1,column=0,pady=1,padx=1,stick="w")
text_first_name=Entry(dataframeleft,font=('arial',17,'bold'),textvariable=first_name,width=22,bd=5,relief=GROOVE)
text_first_name.grid(row=1,column=1,pady=10,padx=15,stick="w")

label_sur_name=Label(dataframeleft,font=('times new roman',20,'bold'),text="Sur Name",bg="red",fg="white")
label_sur_name.grid(row=2,column=0,pady=10,padx=5,stick="w")
text_sur_name=Entry(dataframeleft,font=('arial',17,'bold'),textvariable=sur_name,width=22,bd=5,relief=GROOVE)
text_sur_name.grid(row=2,column=1,pady=10,padx=15,stick="w")

label_dob=Label(dataframeleft,font=('arial',20,'bold'),text="D.O.B.",bg="red",fg="white")
label_dob.grid(row=3,column=0,pady=10,padx=5,stick="w")
text_dob=Entry(dataframeleft,font=('arial',17,'bold'),textvariable=dob ,width=22,bd=5,relief=GROOVE)
text_dob.grid(row=3,column=1,pady=10,padx=15,stick="w")

label_age=Label(dataframeleft,font=('arial',20,'bold'),text="Age" ,bg="red",fg="white")
label_age.grid(row=4,column=0,pady=10,padx=5,stick="w")
text_age=Entry(dataframeleft,font=('arial',17,'bold'),textvariable=age ,width=22,bd=5,relief=GROOVE)
text_age.grid(row=4,column=1,pady=10,padx=15,stick="w")

label_gender=Label(dataframeleft,font=('arial',20,'bold'),text="Gender" ,bg="red",fg="white")
label_gender.grid(row=5,column=0,pady=10,padx=5,stick="w")
text_gender=ttk.Combobox(dataframeleft,textvariable=gender,font=("arial",17,"bold"),state='readonly')
text_gender['values']=("Male","Female","Other")
text_gender.grid(row=5,column=1,padx=15,pady=10)


label_address=Label(dataframeleft,font=('arial',20,'bold'),text="Address" ,bg="red",fg="white")
label_address.grid(row=6,column=0,pady=10,padx=5,stick="w")
text_address=Entry(dataframeleft,font=('arial',17,'bold'),textvariable=address ,width=22,bd=5,relief=GROOVE)
text_address.grid(row=6,column=1,pady=10,padx=15,stick="w")

label_mobile=Label(dataframeleft,font=('arial',20,'bold'),text="Mobile" ,bg="red",fg="white")
label_mobile.grid(row=7,column=0,pady=10,padx=5,stick="w")
text_mobile=Entry(dataframeleft,font=('arial',17,'bold'),textvariable=mobile ,width=22,bd=5,relief=GROOVE)
text_mobile.grid(row=7,column=1,pady=10,padx=15,stick="w")


##==============================================Button Widge=====================================================##

btn_add=Button(buttonframe,text="Add",width=10,height=1,bd=4,command=adddata).grid(row=0,column=0,padx=10,pady=10)

btn_display=Button(buttonframe,text="Show All",height=1,width=10,bd=4,command=displaydata).grid(row=0,column=1,
                                                                                               padx=10,pady=1)

btn_clear=Button(buttonframe,text="Clear",height=1,width=10,bd=4,command=cleardata).grid(row=0,column=2,
                                                                                         padx=10,pady=1)

btn_delete=Button(buttonframe,text="Delete",height=1,width=10,bd=4,command=deletedata).grid(row=0,column=3,
                                                                                            padx=10,pady=1)

btn_search=Button(buttonframe,text="Search",height=1,width=10,bd=4,command=searchdata).grid(row=0,column=5,
                                                                                            padx=10,pady=1)

btn_update=Button(buttonframe,text="Export",height=1,width=10,bd=4,command=exportdata).grid(row=1,column=2,
                                                                                            padx=10,pady=1)

btn_update=Button(buttonframe,text="Update",height=1,width=10,bd=4,command=updatedata).grid(row=1,column=1,
                                                                                            padx=10,pady=1)

btn_exit=Button(buttonframe,text="Exit",height=1,width=10,bd=4,command=iexit).grid(row=1,column=3,
                                                                                   padx=10,pady=1)

root.mainloop()
