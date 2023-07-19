from tkinter import *
import sqlite3
from tkinter import messagebox

def Add_bk():
    global bk_entry 
    global book_entry
    global cat_entry
    global isbn_entry 
    global id_entry
    global root
   
    
    identification=bk_entry.get()
    
    name=book_entry.get()
    isbn=isbn_entry.get()
    genre=cat_entry.get()
    author=id_entry.get()
    
   
  
    

    if (identification and name and isbn and genre and author !=""):

        try:
            conn=sqlite3.connect('library.db')
            cur=conn.cursor()

            query="""INSERT INTO books(book_id,book_name,isbn_no,category,author_id) VALUES (?,?,?,?,?)"""
            data=(identification,name,isbn,genre,author)
            cur.execute(query,data)
            conn.commit()
            messagebox.showinfo(title='success',message='book added sucessfully')
            
        except:
            messagebox.showerror(message='cannot add booK to database')
    
        
    else:
        messagebox.showerror(message='field cannot be empty')

    root.destroy()
        





 ##################function for craeting window for adding books#########################   
def addbooks():
    global bk_entry 
    global book_entry
    global cat_entry
    global isbn_entry 
    global id_entry
    global root
   


    root=Tk()
    root.title('LIBRARY MANAGMENT SYSTEM')
    root.geometry('700x400')
    root.iconbitmap('book.ico.ico')

#creating frames
    main_frame=Frame(root,width=700,height=80, relief='ridge',borderwidth=2,bg='#B8B886')
    main_frame.pack()
    other_frame=Frame(root,width=700,height=520,relief='groove',borderwidth=2)
    other_frame.pack()

#craeting labels and entries
    title=Label(main_frame,text='ADD BOOK DETAILS',font='Courier 30 bold')
    title.place(x=150,y=30)

    #BOOK ID AND NAME--------------------------------------#
    bk_id=Label(other_frame,text='ENTER BOOK ID:',font='Courier 15 bold')
    bk_id.place(x=50,y=40)
    bk_entry=Entry(other_frame,relief='sunken')
    bk_entry.place(x=270,y=40,height=30,width=200)
    bk_name=Label(other_frame,text='BOOK NAME:',font='Courier 15 bold')
    bk_name.place(x=50,y=80)
    book_entry=Entry(other_frame,relief='groove')
    book_entry.place(x=270,y=80,height=30,width=200)

    #ISBN NUMBER ABD CATEGORY------------------------------#
    isbn=Label(other_frame,text='ISBN_NO:',font='Courier 15 bold')
    isbn.place(x=50,y=120)
    isbn_entry=Entry(other_frame,relief='raised')
    isbn_entry.place(x=270,y=120,height=30,width=200)
    cat=Label(other_frame,text='CATEGORY:',font='Courier 15 bold')
    cat.place(x=50,y=160)
    cat_entry=Entry(other_frame,relief='raised')
    cat_entry.place(x=270,y=160,height=30,width=200)

    #AUTHOR ID----------------------------------# 
    author_id=Label(other_frame,text='AUTHOR ID',font='Courier 15 bold')
    author_id.place(x=50,y=200)
    id_entry=Entry(other_frame,relief='sunken')
    id_entry.place(x=270,y=200,height=30,width=200)

    #SUBMIT AND QUIT BUTTON-----------------------------#
    submit_bt=Button(other_frame,text='SUBMIT',command=Add_bk)
    submit_bt.place(x=90,y=240,width=80,height=40)
    quit_bt=Button(other_frame,text='QUIT',command=root.destroy)
    quit_bt.place(x=200,y=240,width=80,height=40)
    
    pass
   
  
  
  
 






    
  
    


