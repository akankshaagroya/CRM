#=====================IMPORTING MODULES================================
from tkinter import * #graphical user interface 
import mysql.connector

#==========FUNCTIONS==============

#submit button to submit the details
def submit():
    email_get = email_entry.get()
    password_get = password_entry.get()
    f = open("myfile.txt", "w")
    f.write(email_get+',')
    f.write(password_get)
    f.close()
    tk.destroy()

#==============MYSQL-CONNECTION=====================
mydb = mysql.connector.connect( host = 'localhost',user='root',password='pass@123')
mycursor = mydb.cursor()
mycursor.execute('DROP DATABASE IF EXISTS login_info;')
mycursor.execute('CREATE DATABASE login_info;')
mycursor.execute('USE login_info;')
mycursor.execute('CREATE TABLE info(EMAIL varchar(60),PASSWORD varchar(10));')

#===============ADDING-SAMPLE-INFO====================
sql = 'INSERT INTO info(EMAIL,PASSWORD) VALUES(%s,%s)'
val = 'dhvani@hello.com','40129'
mycursor.execute(sql,val)  
sql = 'INSERT INTO info(EMAIL,PASSWORD) VALUES(%s,%s)'
val = 'adhyant@hello.com','aimbot'
mycursor.execute(sql,val)  

#==============================================TKINTER================================================================
tk = Tk()

tk.geometry('1000x380+0+0')

tk.title('CRM Login')

intro = Label(tk,text='Crime Records Management',bd=5,relief=GROOVE,font=('Georgia',50,'bold'),bg='#1b1463',fg='White')

intro.pack(side=TOP,fill=X)

work_frame=Frame(tk,bd=4,relief=RIDGE,bg='#1b1463')

work_frame.place(x=200,y=100,width=600,height=250)

#=======Creating Variables========
emailvar = StringVar()

passwordvar = StringVar()


#======EMAIL=========
email = Label(work_frame,text='Email',font=('Georgia',20),bg='#1b1463',fg='White')

email.place(x=10,y=20)

email_entry= Entry(work_frame,font=('Georgia',20),bg='White',fg='Black',textvariable=emailvar)

email_entry.place(x=150,y=35,anchor=W)

#========PASSWORD========
password = Label(work_frame,text='Password',font=('Georgia',20),bg='#1b1463',fg='White')

password.place(x=10,y=90)

password_entry= Entry(work_frame,font=('Georgia',20),bg='White',fg='Black',textvariable = passwordvar,  show = '*')

password_entry.place(x=150,y=110,anchor=W)

#===========BUTTON============
submitbutton = Button(work_frame,command=submit,text='SUBMIT',width=75,bg='White',fg='#1b1463')

submitbutton.place(x=20,y=200,anchor=W)

tk.mainloop()

#=============CHECKING USER DETAILS====================o
f  = open("myfile.txt", "r")
data = f.read()
details = data.split(',')
mycursor.execute('SELECT * FROM info;')
count=0
detail=0
for j in mycursor:
    for i in range(len(j)):
        if j[i] in details:
            detail+=1
         
        else:
            count +=1
    if detail==2:
        import Testing as code
        code
    if count>len(j):
            tk = Tk()
            tk.geometry('400x150+0+0')
            tk.title('ERROR')
            error_frame = Frame(tk,bd=4,relief=RIDGE,bg='#1b1463')
            error_frame.place(x=10,y=10,width=380,height=120)
            error = Label(error_frame,text = 'USER NOT FOUND' ,font=('Georgia',25),bg='MAROON',fg='WHITE')
            error.place(x=40,y=25)
            tk.mainloop()
            break
        



         
            