from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from  main import dashboard















def login():

    global user_entry
    global pass_entry
    global root


    user=user_entry.get() 
    passw=pass_entry.get()

    if user=="" or passw=="":
        messagebox.showerror(title='error',message='field cannot be empty')
    else:
    
        conn=sqlite3.connect('library.db')
        cur=conn.cursor()

        roe= cur.execute("SELECT * FROM patrons where patron_id='%s' and password='%s'" % (user,passw))
           

        if roe.fetchone():
               
            messagebox.showinfo(message='welcome')
            dashboard()
            exit
            

        else:
            messagebox.showerror(title='login failed',message='invalid user_id or password')

           
                
        
        










def tim():

    global user_entry
    global pass_entry
    global root

    root=Tk()
    root.title('LIBRARY MANAGMENT SYSTEM')
    root.geometry('600x500')
    root.iconbitmap('book.ico.ico')



    #-------------CREATING FRAMES---------------------#
    title_frame=Frame(root,height=80,relief='solid',borderwidth=3,bg='#B8B886')
    title_frame.pack(fill='x')
    body_frame=Frame(root,height=420,borderwidth=3,relief='raised')
    body_frame.pack(fill='x')

    #------------------TITLE FRAME-------------------#
    title=Label(title_frame,text='USER LOGIN TAB',font='Courier 30 bold')
    title.place(x=150,y=30)


    #------------------LOGIN DETAILS-------------------------------#
    user_id=Label(body_frame,text='USER ID:',font='Courier 15 bold')
    user_id.place(x=50,y=20)
    user_entry=Entry(body_frame,relief='sunken')
    user_entry.place(x=270,y=20,height=30,width=200)
    pass_name=Label(body_frame,text="PASSWORD:",font='Courier 15 bold')
    pass_name.place(x=50,y=70)
    pass_entry=Entry(body_frame,relief='sunken',show="*")
    pass_entry.place(x=270,y=70,width=200,height=30)


    submit_bt=Button(body_frame,text='LOGIN',command=login)
    submit_bt.place(x=90,y=110,width=80,height=40)
    root.mainloop()

tim()






