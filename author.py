from  tkinter import *
import sqlite3
from tkinter import messagebox


def writer():
    global author_entry
   
    global root


    name=author_entry.get()
  
    
    if (name !=""):
        try:
            conn=sqlite3.connect('library.db')
            cur=conn.cursor()
           
            query="INSERT INTO authors(author_name) VALUES (?)"
            data=(name)
            cur.execute(query,data)
            conn.commit()
            messagebox.showinfo(title='success',message='author added sucessfully')
            
        except:
            messagebox.showerror(message='cannot add author to database')
    
    else:
        messagebox.showerror(message='field cannot be empty')
  
 



#----------------------FUNCTION FOR CREATING MAIN WINDOW-----------------------#
def Add_author():
    
    global author_entry
   
    global root    

    root=Tk()
    root.title('LIBRARY MANAGMENT SYSTEM')
    root.geometry('700x400')
    root.iconbitmap('book.ico.ico')

#creating frames
    main_frame=Frame(root,width=700,height=80, relief='ridge',borderwidth=2,bg='#B8B886')
    main_frame.pack()
    other_frame=Frame(root,width=700,height=520,relief='groove',borderwidth=2,bg='#8B8B47')
    other_frame.pack()
  

#creating labels and entries
    title=Label(main_frame,text='AUTHOR',font='Courier 30 bold')
    title.place(x=150,y=30)
    author_name=Label(other_frame,text='AUTHOER NAME:',font='Courier 15 bold')
    author_name.place(x=50,y=20)
    author_entry=Entry(other_frame,relief='sunken')
    author_entry.place(x=220,y=20,height=30,width=200)
  
    submit_bt=Button(other_frame,text='SUBMIT',command=writer)
    submit_bt.place(x=90,y=80,width=80,height=40)
    quit_bt=Button(other_frame,text='QUIT',command=root.destroy)
    quit_bt.place(x=250,y=80,width=80,height=40)
    root.mainloop()

Add_author()