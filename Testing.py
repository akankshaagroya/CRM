#importing the modules
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import tkinter.messagebox as messagebox
import mysql.connector


#Setting MYSQL and Python Connectivity
mydb = mysql.connector.connect( host = 'localhost',user='root',password='Dhvani#40129')
mycursor = mydb.cursor()

mycursor.execute('USE CRM')



#==============================================================FUNCTIONS==================================================================
#function used to clear all the existing entries from the entry box

def showtable():
    mycursor.execute('SELECT * FROM DETAILS')
    ID= []
    for i in mycursor:
        if i not in  ID:
            ID.append(i)
            tree.insert('','end',values=(i))
            


def cleartable():
       for i in tree.get_children():
        tree.delete(i)
        showtable()


def searchID():
    for i in tree.get_children():
        tree.delete(i)  

    entryid = searchentry.get()
     

    mycursor.execute('SELECT * FROM DETAILS WHERE CASEID = %s',(entryid,))
    ID= []
    for i in mycursor:
            if i not in  ID:
                ID.append(i)
                tree.insert('','end',values=(i))
    searchentry.delete(0,END)


def clearentry():
    identry.delete(0,END)
    complaineeentry.delete(0,END)
    dateentry.delete(0,END)
    cityentry.delete(0,END)
    stateentry.delete(0,END)
    phoneentry.delete(0,END)
    extraentry.delete(0,END)


#function used to exit the window/destroy the window
def exitcommand():
    tk.destroy()


#function used to update the existing record which is also selected
def edit():
    try:
        idcase = caseid_var.get()
    except:
        messagebox.showinfo('ERROR','Check Case ID')
    try:
        namecase = name_var.get()
    except:
        messagebox.showinfo('ERROR','Check Name')
    try:
        datecase = date_var.get()
    except:
        messagebox.showinfo('ERROR','Check Date')
    try:
        citycase = city_var.get()
    except:
        messagebox.showinfo('ERROR','Check City')
    try:
        statecase = state_var.get()
    except:
        messagebox.showinfo('ERROR','Check State')
    try:
        contactcase = contact_var.get()
    except:
        messagebox.showinfo('ERROR','Check Contact')
    try:
        detailscase = extra_var.get()
    except:
        messagebox.showinfo('ERROR','Check Details')
    

    f = open('details.txt','w')
    f.write(str(idcase)+','+str(namecase)+','+str(datecase)+','+str(citycase)+','+str(statecase)+','+str(contactcase)+','+str(detailscase))
    f.close()
    f = open('details.txt','r')
    data = f.read()
    data = data.split(',')
    valuetree = data[0],data[1],data[2],data[3],data[4],data[5],data[6]
    selected_item = tree.selection()[0]
    tree.item(selected_item, values=(valuetree))
    Update="Update DETAILS set  NAME='%s', DATE='%s', City='%s', State='%s', Contact='%s',Extra='%s' where CASEID='%s'" %(namecase,datecase,citycase,statecase,contactcase,detailscase,idcase)
    mycursor.execute(Update)
    mydb.commit()
    clearentry()


#function used to delete an existing record which is selected
def deletee():
    selected_item = tree.focus()
    item_details = tree.item(selected_item)
    data=item_details.get("values")
    mycursor.execute("DELETE FROM DETAILS WHERE CASEID=%s",(data[0],))
    mydb.commit()

    selected_item = tree.selection()[0]
    tree.delete(selected_item)


#function used to enter a new record from the data given in the entry box
def insert():
    try:
        idcase = caseid_var.get()
    except:
        messagebox.showinfo('ERROR','Check Case ID')
    try:
        namecase = name_var.get()
    except:
        messagebox.showinfo('ERROR','Check Name')
    try:
        datecase = date_var.get()
    except:
        messagebox.showinfo('ERROR','Check Date')
    try:
        citycase = city_var.get()
    except:
        messagebox.showinfo('ERROR','Check City')
    try:
        statecase = state_var.get()
    except:
        messagebox.showinfo('ERROR','Check State')
    try:
        contactcase = contact_var.get()
    except:
        messagebox.showinfo('ERROR','Check Contact')
    try:
        detailscase = extra_var.get()
    except:
        messagebox.showinfo('ERROR','Check Details')
    else:
        if idcase == "":
            messagebox.showinfo('ERROR','Missing ID')
        elif namecase == '':
            messagebox.showinfo('ERROR','Missing Name')
        elif datecase == '':
            messagebox.showinfo('ERROR','Missing date')
        elif citycase == '':
            messagebox.showinfo('ERROR','Missing City')
        elif statecase == '':
            messagebox.showinfo('ERROR','Missing state')
        elif contactcase == '':
            messagebox.showinfo('ERROR','Missing contact')
        elif detailscase == '':
            messagebox.showinfo('ERROR','Missing details')
        else:
            f = open('details.txt','w')
            f.write(str(idcase)+','+str(namecase)+','+str(datecase)+','+str(citycase)+','+str(statecase)+','+str(contactcase)+','+str(detailscase))
            f.close()
            f = open('details.txt','r')
            data = f.read()
            data = data.split(',')
            sql = 'INSERT INTO DETAILS VALUES (%s,%s,%s,%s,%s,%s,%s)'
            values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
            try:
             mycursor.execute(sql,values)
             mydb.commit()
             tree.insert('','end',values=values)
             clearentry()
            except:
                messagebox.showinfo('ERROR','Please recheck the entered data')
            
            f.close()
            
            


#=========================================================MAINCODE========================================================================

#CREATING TKINTER WINDOW
tk = Tk()
#giving the tkinter window a title
tk.title('Crime Records Management')
#giving the dimensions of the tkinter window
tk.geometry('1350x700+0+0')

#=============ADDING INTRO LABEL================
#adding a heading to the tkinter window
intro = Label(tk,text='Crime Records Management',bd=5,relief=GROOVE,font=('Georgia',50,'bold'),bg='#1b1463',fg='White')

#packing the heading assigning it a side and filling it along the x-axis
intro.pack(side=TOP,fill=X)

#==============EXTRA FRAMES===========================
#creating the workframe where the new data will be inputted
work_frame=Frame(tk,bd=4,relief=RIDGE,bg='#1b1463')
work_frame.place(x=10,y=90,width=430,height=540)

#creating the search frame where the option to search will be placed
search_frame = Frame(tk,bd=4,relief=RIDGE,bg='#1b1463',width=810,height=60)
search_frame.place(x=450,y=90)

#creating the display frame where the database will be shown
table_frame=Frame(tk,bd=4,relief=RIDGE,bg='#1b1463')
table_frame.place(x=450,y=150,width=810,height=480)


#creating heading for the workframe
work_title=Label(work_frame,text='Manage Data',font=('Georgia',20),bg='#1b1463',fg='White')
work_title.place(x=130,y=0) #assigning coordinates to the text

#creating heading for the display frame
table_title=Label(table_frame,text='Crime Records',font=('Georgia',20),bg='#1b1463',fg='White')
table_title.place(x=300,y=0) #assigning coordinates to the text

#=====================VARIABLES=======================
#Variables for the table
caseid_var= StringVar()

name_var= StringVar()

date_var= StringVar()

city_var=StringVar()

state_var=StringVar()

contact_var=StringVar()

extra_var=StringVar()

search_var = StringVar()

#=========================LABELS==========================
idnumber = Label(work_frame,text='Case ID',font=('Georgia',15),bg='#1b1463',fg='white')

complainee = Label(work_frame,text='Name',font=('Georgia',15),bg='#1b1463',fg='white')

date = Label(work_frame,text='Date',font=('Georgia',15),bg='#1b1463',fg='white')

city = Label(work_frame,text='City',font=('Georgia',15),bg='#1b1463',fg='white')

state = Label(work_frame,text='State',font=('Georgia',15),bg='#1b1463',fg='white')

phone = Label(work_frame,text='Contact',font=('Georgia',15),bg='#1b1463',fg='white')

extra = Label(work_frame,text='Details',font=('Georgia',15),bg='#1b1463',fg='white')



#====================PLACING LABELS========================
idnumber.place(x=20,y=55)

complainee.place(x=20,y=100)

date.place(x=20,y=150)

city.place(x=20,y=200)

state.place(x=20,y=250)

phone.place(x=20,y=300)

extra.place(x=20,y=350)


#=================================================================MAKING ENTRIES==========================================================
identry = Entry(work_frame,textvariable =caseid_var,font=('Georgia',15))

complaineeentry= Entry(work_frame,textvariable=name_var,font=('Georgia',15))

#date entry has a special entry, a dropdown calendar 
dateentry= DateEntry(work_frame,textvariable=date_var,font=('Georgia',15)) 

cityentry= Entry(work_frame,textvariable=city_var,font=('Georgia',15))

#states have a special dropdown combobox for entry
#creating a list of states for the combo box options
states = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra/NagarHaveli","Daman/Diu","Lakshadweep","Delhi","Puducherry"]

stateentry= ttk.Combobox(work_frame,value=states,textvariable=state_var,font=('Georgia',15))

phoneentry= Entry(work_frame,textvariable=contact_var,font=('Georgia',15))

extraentry= Entry(work_frame,textvariable=extra_var,font=('Georgia',15),width=20)

searchentry = Entry(search_frame,textvariable=search_var,font=('Georgia',15),width=20)


#=============================PLACING ENTRIES===========================================================
identry.place(x=150,y=55)

complaineeentry.place(x=150,y=100)

dateentry.place(x=150,y=150)

cityentry.place(x=150,y=200)

stateentry.place(x=150,y=250)

phoneentry.place(x=150,y=300)

extraentry.place(x=150,y=350)

searchentry.place(x=20,y=10)
#======================================================BUTTONS=================================================

#CREATING BUTTONS
inputbutton= Button(work_frame,text='Input',width=10,command=insert)

updatebutton = Button(work_frame,text='Update',width=10,command=edit)

deletebutton = Button(work_frame,text='Delete',width=10,command=deletee)

exitbutton = Button(work_frame,text='Exit',width=10,command=exitcommand)

searchbutton = Button(search_frame,text='Search',width =10,command=searchID)

clearbutton = Button(search_frame,text='Clear',width=10,command=cleartable)

#PLACING BUTTONS
inputbutton.place(x=25,y=450)

updatebutton.place(x=125,y=450)

deletebutton.place(x=225,y=450)

exitbutton.place(x=325,y=450)

searchbutton.place(x=280,y=11)

clearbutton.place(x=370,y=11)
#===================================================TREEVIEW==============================================================================
#creating scrollbars
xscroll= Scrollbar(table_frame,orient=HORIZONTAL)

yscroll = Scrollbar(table_frame,orient=VERTICAL)

tree = ttk.Treeview(table_frame,columns=('Case ID','Name','Date','City','State','Contact','Extra Info'),xscrollcommand=xscroll,
yscrollcommand=yscroll)

xscroll.pack(side=BOTTOM,fill=X)

yscroll.pack(side=RIGHT,fill=Y)

xscroll.config()

yscroll.config()

#defining treeview headings
tree.heading('Case ID',text='Case ID')

tree.heading('Name',text='Name')

tree.heading('Date',text='Date')

tree.heading('City',text='City')

tree.heading('State',text='State')

tree.heading('Contact',text='Contact')

tree.heading('Extra Info',text='Details')

tree['show'] = 'headings'

tree.column('Case ID',width=100)

tree.column('Name',width=100)

tree.column('Date',width=100)

tree.column('City',width=100)

tree.column('State',width=100)

tree.column('Contact',width=100)

tree.column('Extra Info',width=150)

tree.pack(fill=BOTH,expand=1)

showtable()


tk.mainloop()

