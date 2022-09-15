# optional question 1
# import sqlite3
# conn=sqlite3.connect('lab5_optionalQ1db.sqlite')
# curs=conn.cursor()
# tblcmd='create table employees (employee_id int,first_name varchar(30),last_name varchar(30),email varchar(30),phone_numberhire_data int(10),job_id int,salary int,commission varchar(30),manager_id int,department_id int)'
# curs.execute(tblcmd)
# conn.commit()
# curs.execute("insert into employees values(01,'SUBHAM','GUPTA','subham12@gmail.com','6376136761','12','100000','Mr Gupta','13','100')")
# conn.commit()
# a=curs.execute('select * from employees')
# for r in a.fetchall():
#     print(r)
# curs.execute("insert into employees values(01,'Lakshay','Gupta','lakshay01@gmail.com','6376136761','12','200000','Mr Gupta','13','100')")
# conn.commit()
# a=curs.execute('select * from employees where salary > 25000')
# for r in a.fetchall():
#     print(r)

# optional question 2
# import sqlite3
# conn=sqlite3.connect('lab5_optionalQ2db.sqlite')
# curs=conn.cursor()
# tblcmd="create table Student (Reg_no int,stud_name varchar(30),sex varchar(6))"
# curs.execute(tblcmd)
# conn.commit()
# tblcmd="create table Dept (Dept_no int PRIMARY KEY,dept_name varchar(30))"
# curs.execute(tblcmd)
# conn.commit()
# curs.execute('insert into Student values(01,"SUBHAM GUPTA","MALE")')
# curs.execute('insert into Dept values(100,"BCT")')
# curs.execute('insert into Student values(03,"SHREYA SRIVASTAVA","FEMALE")')
# conn.commit()
# curs.execute('insert into Student values(04,"Naika","FEMALE")')
# conn.commit()
# a=curs.execute('select * from student')
# for r in a:
#     print(r[0],r[1])
# a=curs.execute('select * from Dept')
# for r in a:
#     print(r[0],r[1])
# a=curs.execute('select * from Student')
# for r in a:
#     c=r[1]
#     if(c[-1]=='a' and c[-2]=='k'):
#         print(c)
# a=curs.execute('select * from Student where sex ="FEMALE"')
# for r in a:
#     print(r[1])
# a=curs.execute('select * from Student')
# b=[]
# for r in a:
#     b.append(r[1])
# b.sort(reverse=True)
# print(b)

# question 1
# import sqlite3
# conn=sqlite3.connect('lab5_Q1db.sqlite')
# curs=conn.cursor()
# # tblcmd="create table recipes (id int(11),name varchar(400),description text,category_id int(11),chef_id int(255),created datetime)"
# # curs.execute(tblcmd)
# # conn.commit()
# curs.execute("insert into recipes values(145,'RAJ','Best chef',1,'BL00002',datetime('now'))")
# curs.execute("insert into recipes values(145,'RAJ','Best chef',1,'BL00005',datetime('now'))")
# curs.execute("insert into recipes values(145,'Pakora','Best chef',1,'BL00005',datetime('now'))")
# curs.execute("insert into recipes values(145,'Rice','Best chef',1,'BL00005',datetime('now'))")
# conn.commit()
# a=curs.execute("select * from recipes where chef_id = 'BL00002'")
# for r in a:
#     print(r)
# a=curs.execute("select * from recipes")
# for r in a:
#     print(r)
# a=curs.execute("select * from recipes where name LIKE 'P%'")
# for r in a:
#     print(r)

# # question 2
# import sqlite3
# conn=sqlite3.connect('lab5_Q2db.sqlite')
# curs=conn.cursor()
# tblcmd="create table movie (Movie_ID int,Movie_Name varchar(20), Genre varchar(10),Language varchar(30),Rating real)"
# curs.execute(tblcmd)
# conn.commit()
# curs.execute('insert into movie values (102,"You","Horror","Hindi",3.0)')
# curs.execute('insert into movie values (12,"Me","Action","Hindi",5.0)')
# curs.execute('insert into movie values (100,"u","Romance","English",4.0)')
# conn.commit()
# curs.execute('UPDATE movie SET Rating=(Rating +0.1*Rating)')
# conn.commit()
# curs.execute('Delete from movie where Movie_ID =102')
# conn.commit()
# a=curs.execute('select * from movie where Rating > 3.0')
# for r in a:
#     print(r)

# # question 3
# import sqlite3
# conn=sqlite3.connect('lab5_Q3db.sqlite')
# curs=conn.cursor()
# tblcmd="create table Product (ID int,Prod_name varchar(40),Supplier_id int,Unit_price int,Package int, OrderID int)"
# curs.execute(tblcmd)
# conn.commit()
# tblcmd="create table OrderItem (ID int,Order_id int,Product_id int,Unit_price int,Quantity int,FOREIGN KEY(ID,Order_id) REFERENCES Product(ID,OrderID))"
# curs.execute(tblcmd)
# conn.commit()
# curs.execute('insert into Product values (11,"Wheat","Farmer",500,10,137)')
# conn.commit()
# curs.execute('insert into OrderItem values (11,137,10,500,12)')
# conn.commit()
# curs.execute('insert into Product values (15,"HELLO",132,5,450,2)')
# conn.commit()
# a=curs.execute('select Quantity from OrderItem')
# for r in a:
#     print(r)
# a=curs.execute('select Unit_Price from Product ORDER BY Supplier_id')
# for r in a:
#     print(r)
# # a=curs.execute('select Prod_name, OrderID, Supplier_id from Product')
# for r in a:
#     print(r)

# # question 4
# import sqlite3
# conn=sqlite3.connect('lab5_Q4db.sqlite')
# curs=conn.cursor()
# tblcmd="create table job (job_id int,job_title varchar(40),Min_Salary int,Max_Salary int,Package int,UNIQUE(job_id) ON CONFLICT IGNORE)"
# curs.execute(tblcmd)
# conn.commit()
# curs.execute('insert into job values (11,"Programmer",50000,500000,1000000)')
# conn.commit()
# curs.execute('insert into job values (13,"Programmer",50000,500000,1000000)')
# conn.commit()
# curs.execute('insert into job values (11,"Programmer",50000,500000,1000000)')
# # conn.commit()

# question 5
# import sqlite3
# conn = sqlite3.connect('lab5_Q5db.sqlite')
# curs = conn.cursor()
# tblcmnd = "create table job_history (employee_id int,start_date int,end_date int,job_id int PRIMARY KEY,department_id int,UNIQUE(employee_id) ON CONFLICT IGNORE)"
# curs.execute(tblcmnd)
# curs.execute('insert into job_history values (?,?,?,?,?)',(11,23,30,1,10))
# conn.commit()
# cmnd = "create table job (job_id int,FOREIGN KEY(job_id) REFERENCES job_history(job_id))"
# curs.execute(cmnd)
# curs.execute('insert into job values (1)')
# conn.commit()
# conn.execute("PRAGMA foreign_keys = ON;")
# conn.execute("PRAGMA foreign_keys = 1")
# curs.execute('insert into job values (2)')
# conn.commit()