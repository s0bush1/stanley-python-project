from  tkinter import *
import sqlite3
from tkinter import messagebox








def Add_pt():
    global first_entry
    global  second_entry
    global  surname_entry
    global phone_entry
    global email_entry
    global password_entry

    name1=first_entry.get()
    name2=second_entry.get()
    name3=surname_entry.get()
    phone=phone_entry.get()
    address=email_entry.get()
    pin=password_entry.get()

    if (name1 and name2 and name3 and phone and address and pin !=""):
        try:
            conn=sqlite3.connect('library.db')
            cur=conn.cursor()

            query="""INSERT INTO patrons(first_name,second_name,surname,phone_no,email,password) VALUES (?,?,?,?,?,?)"""
            data=(name1,name2,name3,phone,address,pin)
            cur.execute(query,data)
            conn.commit()
            messagebox.showinfo(title='success',message='patron added sucessfully')
           
        except:
            messagebox.showerror(message='cannot add patron to database')
    
        root.destroy()
    else:
        messagebox.showerror(message='field cannot be empty')
        
##################function for craeting window for adding students#########################
def addpatrons():
    global first_entry 
    global second_entry
    global surname_entry
    global phone_entry
    global email_entry
    global password_entry
    global root


    root=Tk()
    root.title('LIBRARY MANAGMENT SYSTEM')
    root.geometry('600x500')
    root.iconbitmap('book.ico.ico')

    #creating frames 
    title_frame=Frame(root,height=80,relief='solid',borderwidth=3,bg='#B8B886')
    title_frame.pack(fill='x')
    body_frame=Frame(root,height=420,borderwidth=3,relief='raised')
    body_frame.pack(fill='x')

    #craeting enties and labels
    title=Label(title_frame,text='ADD PATRON DETAILS',font='Courier 30 bold')
    title.place(x=150,y=30)
    #----------------names-----------------------#
    first_name=Label(body_frame,text='FIRST NAME:',font='Courier 15 bold')
    first_name.place(x=50,y=20)
    first_entry=Entry(body_frame,relief='sunken')
    first_entry.place(x=270,y=20,height=30,width=200)
    second_name=Label(body_frame,text='SECOND NAME:',font='Courier 15 bold')
    second_name.place(x=50,y=70)
    second_entry=Entry(body_frame,relief='sunken')
    second_entry.place(x=270,y=70,width=200,height=30)
    surname=Label(body_frame,text='SURNAME:',font='Courier 15 bold')
    surname.place(x=50,y=120)
    surname_entry=Entry(body_frame,relief='raised')
    surname_entry.place(x=270,y=120,height=30,width=200)
    #------------------phone no and email address-----------------#
    email=Label(body_frame,text='EMAIL ADDRESS:',font='Courier 15 bold')
    email.place(x=50,y=220)
    email_entry=Entry(body_frame,relief='raised')
    email_entry.place(x=270,y=220,height=30,width=200)
    phone_no=Label(body_frame,text='PHONE NO:',font='Courier 15 bold')
    phone_no.place(x=50,y=170)
    phone_entry=Entry(body_frame,relief='raised')
    phone_entry.place(x=270,y=170,width=200,height=30)
    #--------------------PASSWORD-----------------#
    password=Label(body_frame,text='PASSWORD:',font='Courier 15 bold')
    password.place(x=50,y=270)
    password_entry=Entry(body_frame,show='*')
    password_entry.place(x=270,y=270,height=30,width=200)
    
    submit_bt=Button(body_frame,text='SUBMIT',command=Add_pt)
    submit_bt.place(x=90,y=350,width=80,height=40)
    quit_bt=Button(body_frame,text='QUIT',command=root.destroy)
    quit_bt.place(x=200,y=350,width=80,height=40)

    root.mainloop()

   
    pass








    



  
