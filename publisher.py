from  tkinter import *
import sqlite3
from tkinter import messagebox


def publish():
    global pub_entry
    global id_entry
    global root


    company=pub_entry.get()
    pub_id=id_entry.get()
    
    if (company and pub_id  !=""):
        try:
            conn=sqlite3.connect('library.db')
            cur=conn.cursor()
            print('successfuly connected')

            query="""INSERT INTO publisher( publisher_name,publisher_id) VALUES (?,?)"""
            data=(company,pub_id)
            cur.execute(query,data)
            conn.commit()
            messagebox.showinfo(title='success',message='publisher added sucessfully')
            
        except:
            messagebox.showerror(message='cannot add publisher to database')
    
    else:
        messagebox.showerror(message='field cannot be empty')
    root.destroy()
 



#----------------------FUNCTION FOR CREATING MAIN WINDOW-----------------------#
def Add_publisher():
    
    global pub_entry
    global id_entry
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
    title=Label(main_frame,text='ADD PUBLISHER',font='Courier 30 bold')
    title.place(x=150,y=30)
    pub_name=Label(other_frame,text='PUBLISHER NAME:',font='Courier 15 bold')
    pub_name.place(x=50,y=20)
    pub_entry=Entry(other_frame,relief='sunken')
    pub_entry.place(x=270,y=20,height=30,width=200)
    id=Label(other_frame,text='PUBLISHER ID:',font='Courier 15 bold')
    id.place(x=50,y=60)
    id_entry=Entry(other_frame,relief='sunken')
    id_entry.place(x=270,y=60,height=30,width=200)
    submit_bt=Button(other_frame,text='SUBMIT',command=publish)
    submit_bt.place(x=90,y=130,width=80,height=40)
    quit_bt=Button(other_frame,text='QUIT',command=root.destroy)
    quit_bt.place(x=250,y=130,width=80,height=40)
    root.mainloop()


Add_publisher()



    
    









































# check_bk="""SELECT * FROM books where available='yes';"""
          
#             give=cur.execute(check_bk)
            

#             flag=0
#             for i in give:
#                 if(i[0]==bok):
#                     flag=1
#                 break;
                    
            
#             if flag==1:
#                 update_db="""UPDATE books set available='NO' where bok='"+bok+"';"""
#                 print(update_db)
#                 cur.execute(update_db)


#                 query="""INSERT into issue_book  VALUES('"+bok+"','"+student+"');"""
                
#                 cur.execute(query)
#                 conn.commit()

#                 messagebox.showinfo(title='SUCCESS',message='book sucessfully issued')
#         except:
#             messagebox.showerror(message='book not available')
#     else:
#         messagebox.showerror(message='cannot issue given book')
#     root.destroy()