from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime




def give_bk():
    global bk_entry
    global to_entry
    global root

    bok=bk_entry.get()
    student=to_entry.get()


    if bok=="" or student=="":
        messagebox.showerror(title='error',message='field cannot be empty')
    else:
  

        conn=sqlite3.connect('library.db')
        cur=conn.cursor()
        
  
        check_availability="SELECT * FROM  books WHERE available='YES'"
        cur.execute(check_availability)
        conn.commit()


            
        if cur.fetchone():
            
            
            cur.execute( "UPDATE books set available='NO' WHERE available=?")
            conn.commit()

            
            sqlquery="""INSERT INTO issued_books(book_id,issued_to) VALUES(?,?)"""
            lend=(bok,student)
            cur.execute(sqlquery,lend)
            conn.commit()


            messagebox.showinfo(message='book issued succesfully')
        else:
            messagebox.showerror(message='required book is not available')
        
    
##################function for craeting window for issuing books#########################
def issue():

    global bk_entry
    global to_entry
    global root

    root=Tk()
    root.title('LIBRARY MANAGMENY SYSTEM')
    root.geometry('400x400')

    #craete frames
    main_frame=Frame(root,height=80,relief='solid',borderwidth=3,bg='#B8B886')
    main_frame.pack(fill='x')
    body_frame=Frame(root,height=320,relief='raised',borderwidth=3)
    body_frame.pack(fill='x')


    #create entries and labels
    title=Label(main_frame,text='ISSUE BOOK',font='arial 20 bold')
    title.place(x=100,y=20)
    issued_bk=Label(body_frame,text='BOOK ID:',font='arial 12 bold')
    issued_bk.place(x=30,y=40)
    bk_entry=Entry(body_frame)
    bk_entry.place(x=140,y=40,width=100,height=26)
    issued_to=Label(body_frame,text='ISSUED TO:',font='arial 12 bold')
    issued_to.place(x=30,y=80)
    to_entry=Entry(body_frame)
    to_entry.place(x=140,y=80,width=100,height=26)
    submit_bt=Button(body_frame,text='SUBMIT',command=give_bk)
    submit_bt.place(x=90,y=150,width=80,height=40)
    quit_bt=Button(body_frame,text='QUIT',command=root.destroy)
    quit_bt.place(x=200,y='150',width=80,height=40)
    
    pass






























