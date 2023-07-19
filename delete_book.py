from tkinter import  *
from tkinter import messagebox
import sqlite3

def delete_db():
    global delete_entry
    global root

    bk_id=delete_entry.get()

    if (bk_id !=""):
        try:
                    conn=sqlite3.connect('library.db')
                    cur=conn.cursor()

                    query="""DELETE FROM books where isbn_no=?""" 
                    data=(bk_id)
                    cur.execute(query,data)
                    conn.commit()
                    messagebox.showinfo(title='success',message='book sucessfully deleted')
                
        except:
                    messagebox.showerror(message='please check book id')
            
        root.destroy()
    else:
        messagebox.showerror(message='field cannot be empty')

##################function for craeting window for deleteing books#########################
def delete():
    global delete_entry
    global root

    root=Tk()
    root.title('LIBRARY MANAGMENT SYSTEM')
    root.geometry('400x280')

    #create frames
    title_frame=Frame(root,height=80,relief='solid',borderwidth=3,bg='#B8B886')
    title_frame.pack(fill='x')
    body_frame=Frame(root,height=200,borderwidth=3,relief='raised')
    body_frame.pack(fill='x')

    #create the label,entry  and button
    title=Label(title_frame,text='DELETE BOOK',font='arial 15 bold',fg='#8B8B47')
    title.place(x=130,y=20)
    delete_lbl=Label(body_frame,text='ENTER BOOK ID:',font='arial 12 bold')
    delete_lbl.place(x=30,y=30)
    delete_entry=Entry(body_frame)
    delete_entry.place(x=180,y=33,height=20,width=100)
    del_button=Button(body_frame,text='DELETE',command=delete_db,relief='ridge',borderwidth=3)
    del_button.place(x=150,y=60)
    quit_bt=Button(body_frame,text='QUIT',relief='ridge',command=root.destroy,borderwidth=3)
    quit_bt.place(x=250,y=60)

    
  
    pass

































