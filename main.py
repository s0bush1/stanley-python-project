import tkinter as tk
import sqlite3
from tkinter import messagebox
import addbook
import add_students
import delete_book
import delete_patron
import issue_book
import return_book
# import publisher


conn=sqlite3.connect('library.db')
cur=conn.cursor()


def add():
  
    book=addbook.addbooks()

def students():
    user=add_students.addpatrons()

def del_book():
    terminate=delete_book.delete()

def del_pt():
    remove=delete_patron.delete_user()

def give():
    lend=issue_book.issue()

def give_back():
    ret=return_book.return_bk()

# def company():
#     com=publisher.Add_publisher()


    





   
# #SEACH BUTTON FUNCTION
def searchbooks():
    global search_entry
    global ilist


    value=search_entry.get()
    search=cur.execute("SELECT * FROM books WHERE book_name LIKE ?",('%'+value+'%',)).fetchall()
    print(search)
    ilist.delete(0,tk.END)
    count=0
    for book in search:
        ilist.insert(count,str(book[0])+"-"+book[1])
        count +=1




#creating main window
def dashboard():

    global search_entry
    global ilist

    root=tk.Tk()
    root.geometry('700x800')
    root.title("LIBRARAY MANAGMENT SYSTEM")
    root.iconbitmap('icon.ico.ico')
    root.minsize(0,0)





        #creating frame

    top_frame=tk.Frame(root,width=700,height=80, relief='ridge',borderwidth=2,)
    top_frame.pack(side='top',fill='x')
    centre_frame=tk.Frame(root,width=700,height=120,relief='sunken',borderwidth=4)
    centre_frame.pack(fill='x',side='top')
    left_frame=tk.Frame(root,relief='sunken',borderwidth=2)
    left_frame.place(x=0,y=120,relheight=0.5,relwidth=0.6)
    right_frame=tk.Frame(root,relief='sunken',borderwidth=2,bg='#CDCDC1')
    right_frame.place(relx=0.5,y=120,relwidth=0.5,relheight=0.5)


        #welcome bar
    welcome=tk.Label(top_frame,text='WELCOME TO STANLEYS\n NATIONAL LIBRARY',bg='#B8B886',font="arial 15 bold")
    welcome.pack(fill='x')

        #craete buttons for addbook,addpatron,deletebook
    addbook_bt=tk.Button(centre_frame,text='ADD BOOK',command=add,font='arial 15 bold',borderwidth=15,bg='#DADAA5') 
    addbook_bt.grid(row=0,column=0) 
    adduser_bt=tk.Button(centre_frame,text='ADD PATRON',command=students,font='arial 15 bold',borderwidth=15,bg='#DADAA5')
    adduser_bt.grid(row=0,column=1) 
    deletebk_bt=tk.Button(centre_frame,text='DELETE BOOK',command=del_book,font='arial 15 bold',borderwidth=15,bg='#DADAA5')
    deletebk_bt.grid(row=0,column=2)
    issuedbk_bt=tk.Button(centre_frame,text='ISSSUE BOOKS',command=give,font='arial 15 bold',borderwidth=15,bg='#DADAA5')
    issuedbk_bt.grid(row=0,column=3)
    patron=tk.Button(centre_frame,text='DELETE PATRON',command=del_pt,font='arial 15 bold',borderwidth=15,bg='#DADAA5')
    patron.grid(row=0,column=4)
    return_b=tk.Button(centre_frame,text='RETURN BOOK',command=give_back,font='arial 15 bold',borderwidth=15,bg='#DADAA5')
    return_b.grid(row=0,column=5)
    publisher_bt=tk.Button(centre_frame,text='PUBLISHER',font='arial 15 bold',borderwidth=15,bg='#DADAA5')
    publisher_bt.grid(row=0,column=6)



            




    #create a search bar and books
    search_lf=tk.LabelFrame(right_frame,text='SEARCH FOR BOOKS',padx=150,pady=200)
    search_lf.place(relheight=0.5,relwidth=1.0)
    search_bk=tk.Label(right_frame,text='ENTER NAME:',font='arial 10 bold')
    search_bk.place(x=10,y=25)
    search_entry=tk.Entry(right_frame)
    search_entry.place(x=120,y=25)
    search_bt=tk.Button(right_frame,text='SEARCH',command=searchbooks,font='arialL 10 bold',padx=10,pady=10)
    search_bt.place(x=100,y=50)


    #CRAETING RADIO BUTTONS FOR GENERATING REPORTS 
    generate=tk.LabelFrame(right_frame,text="GENERATE REPORTS",padx=150,pady=200)
    generate.place(relwidth=1.0,relheight=0.5,x=0,y=177)
    r1=tk.Radiobutton(right_frame,text=' ISSUED BOOKS',bg='#8B8B83')
    r1.place(x=0,y=200)
    r2=tk.Radiobutton(right_frame,text='RETURNED BOOKS',bg='#8B8B83')
    r2.place(x=0,y=250)
    r3=tk.Radiobutton(right_frame,text='LIST OF PATRONS',bg='#8B8B83')
    r3.place(x=0,y=300)








    #create a frame to display list of books

    ilist=tk.Listbox(left_frame,width=150,height=400,bg='#EEEEE0')
    ilist.pack(fill='both')

    scroll_v=tk.Scrollbar(left_frame,command=ilist.yview)
    ilist.config(yscrollcommand=scroll_v.set)

    scroll_v.pack(side='right',fill='y')

    pass













 











    
    






    









