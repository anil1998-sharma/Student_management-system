import tkinter as tk
from tkinter.ttk import Combobox,Treeview
from tkinter import messagebox
import  psycopg2
from tkinter import *
root=Tk()
root.geometry('700x500')
root.title('Student Management system')
class Student:

    def __init__(self,root):
        self.root=root
        self.head=Label(self.root,text='Student Management System',bg='cyan',bd=10,relief=GROOVE,font=("time new roman",40,"bold"))
        self.head.pack(side=TOP,fill=X)
        self.roll=StringVar()
        self.name=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contect=StringVar()
        self.dob=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        Manage_fram=Frame(self.root,bd=4,relief=RIDGE,bg='cyan')
        Manage_fram.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_fram,text="Manage Student",bg='cyan',fg='black',font=("time new roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lbl_roll=Label(Manage_fram,text='Roll No.',bg='cyan',fg='white',font=("time new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky='w')

        txt_roll=Entry(Manage_fram,textvariable=self.roll,font=("time new roman",15,"bold"))
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')

        lbl_name = Label(Manage_fram, text='Name', bg='cyan', fg='white', font=("time new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        txt_name = Entry(Manage_fram, textvariable=self.name, font=("time new roman", 15, "bold"))
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        lbl_email = Label(Manage_fram, text='Email', bg='cyan', fg='white', font=("time new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        txt_email = Entry(Manage_fram, textvariable=self.email, font=("time new roman", 15, "bold"))
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        lbl_gender = Label(Manage_fram, text='Gender', bg='cyan', fg='white', font=("time new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky='w')

        combo_gender = Combobox(Manage_fram, textvariable=self.gender, font=("time new roman", 15, "bold"),state='readoly')
        combo_gender['values']=("male","female",'other')
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky='w')

        lbl_contect = Label(Manage_fram, text='Contect', bg='cyan', fg='white', font=("time new roman", 20, "bold"))
        lbl_contect.grid(row=5, column=0, pady=10, padx=20, sticky='w')

        txt_contect = Entry(Manage_fram, textvariable=self.contect, font=("time new roman", 15, "bold"))
        txt_contect.grid(row=5, column=1, pady=10, padx=20, sticky='w')


        lbl_dob = Label(Manage_fram, text='D.O.B', bg='cyan', fg='white', font=("time new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky='w')

        txt_roll = Entry(Manage_fram, textvariable=self.dob, font=("time new roman", 15, "bold"))
        txt_roll.grid(row=6, column=1, pady=10, padx=20, sticky='w')
#-----------------------------------------btn frame----------------------------------------------------------------------------------------
        btn_frame=Frame(Manage_fram,bd=4,bg='white',relief=RIDGE)
        btn_frame.place(x=15,y=500,width=420)
        addbtn=Button(btn_frame,text='Add',width=10,bg='cyan',command=self.add_stus).grid(row=1,column=0,padx=10,pady=10)
        updatebtn = Button(btn_frame, text='Update', width=10, bg='cyan',command=self.Update_data).grid(row=1, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text='Delete', width=10, bg='cyan',command=self.delete_data).grid(row=1, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame, text='Clear', width=10, bg='cyan',command=self.clear).grid(row=1, column=3, padx=10, pady=10)

        #detail frame
        detail_freme=Frame(self.root,bd=4,relief=RIDGE,bg='cyan')
        detail_freme.place(x=500,y=100,width=800,height=580)

        lbl_search=Label(detail_freme,text='Search By',bg='cyan',fg='white',font=('time new roman',20,'bold'))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky='w')

        combo_search=Combobox(detail_freme,textvariable=self.search_by,width=10,font=('time new roman',15,'bold'))
        combo_search['values']=('roll_no','name','contect')
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search=Entry(detail_freme,textvariable=self.search_txt,font=('time new roaman',15,'bold'))
        txt_search.grid(row=0,column=2,pady=10,padx=20)

        search_btn=Button(detail_freme,text='Search',width=10,pady=5,command=self.search_data).grid(row=0,column=3,pady=5,padx=5)
        showall_btn = Button(detail_freme, text='Show All', width=10,pady=5,command=self.fetch_data).grid(row=0, column=4, pady=10, padx=5)


#------------------------------------------detaile-table-----------------------------------------------------------------------

        Table_Frame=Frame(detail_freme,bd=4,relief=RIDGE,bg='white')
        Table_Frame.place(x=10,y=70,height=500)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Stud_table=Treeview(Table_Frame,column=('Studentroll','Studentname','Studentgender','Studentemail','Studentcontect','Studentdob'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=Y)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Stud_table.xview)
        scroll_y.config(command=self.Stud_table.yview)
        self.Stud_table.heading('Studentroll',text="Roll No.")
        self.Stud_table.heading('Studentname', text="Name")
        self.Stud_table.heading('Studentgender', text="Gender")
        self.Stud_table.heading('Studentemail', text="Email")
        self.Stud_table.heading('Studentcontect', text="Contect")
        self.Stud_table.heading('Studentdob', text="D.O.B")
        self.Stud_table['show']='headings'
        self.Stud_table.column('Studentroll',width=100)
        self.Stud_table.column('Studentname', width=100)
        self.Stud_table.column('Studentemail', width=100)
        self.Stud_table.column('Studentcontect', width=100)
        self.Stud_table.column('Studentdob', width=100)
        self.Stud_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        #to bind the cursor with textfeild
        self.Stud_table.bind("<ButtonRelease-1>",self.get_cursor)


        #call function to fatch data


#--------------------------------Funtion defination------------------------------------------------------------------------------
    #To clear textbox
    def clear(self):
        self.roll.set('')
        self.name.set('')
        self.email.set('')
        self.gender.set('')
        self.dob.set('')
        self.contect.set('')
    def add_stus(self):

        con = psycopg2.connect(host='localhost',
                               database='StudentDB',
                               user='postgres',
                               password='4anil1998')
        print('get connection')
        cur = con.cursor()
        query = "insert into student values ('{}' ,'{}' ,'{}', '{}', '{}','{}' )".format(self.roll.get(),
                                                                                         self.name.get(),
                                                                                         self.email.get(),
                                                                                         self.gender.get(),
                                                                                         self.contect.get(),
                                                                                         self.dob.get())
        print(query)
        cur.execute(query)
        con.commit()
        '''
        cur.execute("select * from  student;")
        row=cur.fetchall()
        for r in row:
            print(r)'''
        cur.close()
        con.close()
        print('close contection')

        messagebox.showinfo('Data Summitted','Successfully! data stored in database.')
        self.clear()
        self.fetch_data()
    def Update_data(self):
        con = psycopg2.connect(host='localhost',
                               database='StudentDB',
                               user='postgres',
                               password='4anil1998')
        print('get connection')
        cur = con.cursor()
        query="Update student set name= '{}' ,email='{}',gender='{}',contect='{}',dob='{}' where roll_no='{}' ".format(self.name.get(),
                                                                                         self.email.get(),
                                                                                         self.gender.get(),
                                                                                         self.contect.get(),
                                                                                         self.dob.get(),self.roll.get())
        print(query)
        cur.execute(query)
        con.commit()
        con.close
        messagebox.showinfo('Update', 'Successfully! data updated in database.')
    def fetch_data(self):
        con = psycopg2.connect(host='localhost',
                               database='StudentDB',
                               user='postgres',
                               password='4anil1998')
        print('get connection')
        cur = con.cursor()
        cur.execute('select * from student ORDER BY  roll_no ASC')
        row=cur.fetchall()
        if row!=0:
            self.Stud_table.delete(*self.Stud_table.get_children()) # to delete the remaining record if show btn press again anf again
            for r in row:
                self.Stud_table.insert('',END,values=r)
        con.commit()
        con.close()
    def get_cursor(self,ev):
        curosor_row=self.Stud_table.focus()
        contents=self.Stud_table.item(curosor_row)
        row=contents['values']

        self.roll.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.contect.set(row[4])
        self.dob.set(row[5])

    def search_data(self):
        con = psycopg2.connect(host='localhost',
                               database='StudentDB',
                               user='postgres',
                               password='4anil1998')
        print('get connection')
        cur = con.cursor()
        query="select * from student where {}='{}'".format(self.search_by.get(),self.search_txt.get())
        print(query)

        cur.execute(query)
        row=cur.fetchall()
        if row!=0:
            self.Stud_table.delete(*self.Stud_table.get_children())
            for r in row:
                self.Stud_table.insert('',END,values=r)
        con.commit()
        con.close()
    def delete_data(self):
        con = psycopg2.connect(host='localhost',
                               database='StudentDB',
                               user='postgres',
                               password='4anil1998')
        print('get connection')
        cur = con.cursor()
        m=messagebox.askyesnocancel('Delete','Are you sure to delete this record')
        query="Delete from student where  roll_no='{}'".format(self.roll.get())
        print(m, query)
        if m:
            cur.execute(query)
            messagebox.showinfo('Delete', "Record is succussfully delete.")
        cur.close
        con.commit()
        con.close()

















obj=Student(root)
root.mainloop()