import sqlite3 as db

def studentdata():
    con=db.connect("datafile")
    cur=con.cursor()
    cur.execute("create table if not exists student(std_id integer primary key,first_name text,sur_name text,dob text,age text,gender text,address text,\
                mobile text)")
    con.commit()
    con.close()

def addnew(std_id,first_name,sur_name,dob,age,gender,address,mobile):
    con=db.connect("datafile")
    cur=con.cursor()
    cur.execute("create table if not exists student(std_id integer primary key,first_name text,sur_name text,dob text,age text,gender text,address text,mobile text)")
    cur.execute("insert into student values(:std_id,:first_name,:sur_name,:dob,:age,:gender,:address,:mobile)",(std_id,first_name,sur_name,dob,age,gender,address,mobile))
    con.commit()
    con.close()

def delete(std_id):
    con=db.connect("datafile")
    cur=con.cursor()
    cur.execute("delete from student where std_id=:std_id",(std_id,))
    cur=con.commit()
    con.close()

def update(id,std_id="",first_name="",sur_name="",dob="",age="",gender="",address="",mobile=""):
    con=db.connect("datafile")
    cur=con.cursor()
    cur.execute("insert into student values(:std_id,:first_name,:sur_name,:dob,:age,:gender,:address,:mobile)",(std_id,first_name,sur_name,dob,age,gender,address,mobile))

    con.commit()
    con.close()

    
