column=('book_id','book_name','publisher_name','category','status')
    tree=ttk.Treeview(left_frame,height=400,columns=column,show='headings')
    tree.pack(fill='both')

    #setup column attributes
    for col in column:
        tree.heading(col,text=col)
        tree.column(col,anchor=tk.CENTER)

    #fetch data
    conn=sqlite3.connect('library.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM books')

    for rec in c:
        tree.insert('','end',values=rec)