import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="registration"
  )
print(mydb)

mycursor = mydb.cursor()

def GetValue(event):
  e1.delete(0,END)
  e2.delete(0, END)
  e3.delete(0, END)
  e4.delete(0, END)
  row_id = listBox.selection()[0]
  select = listBox.set(row_id)
  e1.insert(0,select['ID'])
  e2.insert(0, select['Student Name'])
  e3.insert(0, select['Course'])
  e4.insert(0, select['Form Number'])

def Add():
  studid = e1.get()
  studname = e2.get()
  coursename = e3.get()
  formno = e4.get()

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="registration"
  )

  mycursor = mydb.cursor()

  try:
    sql = "INSERT INTO record (id, stname, course, formno) VALUES (%s, %s, %s, %s)"
    val = (studid, studname, coursename,formno)
    mycursor.execute(sql, val)
    mydb.commit()
    lastid= mycursor.lastrowid
    messagebox.showinfo("information", "Record inserted successfully...")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e1.focus_set()

  except Exception as e:
    print(e)
    mydb.rollback()
    mydb.close()

def Update():
  studid = e1.get()
  studname = e2.get()
  coursename = e3.get()
  formno = e4.get()

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="registration"
  )

  mycursor = mydb.cursor()

  try:
    sql = "UPDATE record set stname = %s, course= %s, formno=%s where id=%s"
    val = (studname, coursename, formno, studid)
    mycursor.execute(sql, val)
    mydb.commit()
    lastid = mycursor.lastrowid
    messagebox.showinfo("information", "Record Updated Successfully...")

    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e1.focus_set()

  except Exception as e:

    print(e)
    mydb.rollback()
    mydb.close()

def Delete():
  studid = e1.get()

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="registration"
  )

  mycursor = mydb.cursor()

  try:
    sql = "DELETE FROM record where id = %s"
    val = (studid,)
    mycursor.execute(sql, val)
    mydb.commit()
    lastid = mycursor.lastrowid
    messagebox.showinfo("information", "Record Deleted Successfully")

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e1.focus_set()

  except Exception as e:

    print(e)
    mydb.rollback()
    mydb.close()

def Show():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="registration"
  )

  mycursor = mydb.cursor()

  mycursor.execute("SELECT id, stname, course, formno FROM record")
  records = mycursor.fetchall()
  print(records)

  for i, (id, stname, course, formno) in enumerate(records, start=1):
    listBox.insert("", "end", values=(id, stname, course, formno))
    mydb.close()


'''mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="registration"
  )
print(mydb)

mycursor = mydb.cursor()
'''
'''
mycursor.execute("CREATE DATABASE registration")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
'''
#mycursor.execute("CREATE TABLE record ( id INTEGER, stname VARCHAR(20), course VARCHAR(20), formno INTEGER)")
#mycursor.execute("ALTER TABLE record ADD PRIMARY KEY (id)")


root=Tk()
root.title("Registration Form")
root.iconbitmap("C:\\Users\pranjal lotankar\PycharmProjects\pythonproject\gui\login.ico")
root.geometry("800x500")
root['bg']="LightBlue4"
global e1
global e2
global e3
global e4

tkinter.Label(root, text="Student Registration",bg="blanched almond", fg= "gold4", font=("Times", "24", "bold italic underline")).place(x=400, y=5)

tkinter.Label(root, text="Student ID", bg="light cyan").place(x=10, y=10)
tkinter.Label(root, text="Student Name", bg="light cyan").place(x=10, y=40)
tkinter.Label(root, text="Course", bg="light cyan").place(x=10, y=70)
tkinter.Label(root, text="Form Number", bg="light cyan").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Add", command= Add, height=3, bg="cyan", width=13).place(x=30, y=130)
Button(root, text="Update", command=Update, height=3, bg="green yellow", width=13).place(x=140, y=130)
Button(root, text="Delete", command=Delete, height=3, bg="sienna2", width=13).place(x=250, y=130)

cols = ('ID', 'Student Name', 'Course', 'Form Number')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
  listBox.heading(col, text=col)
  listBox.grid(row=1, column=0, columnspan= 2)
  listBox.place(x=10, y=200)


Show()
listBox.bind('<Double-Button-1>', GetValue)
root.mainloop()

