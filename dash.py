from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox
#from tkMessageBox import *
#import cmsg #custom message file 

#global con,cur
#con = sqlite3.connect('DB.db')
#cur = con.cursor()

def create():  
    
    con = sqlite3.connect('DB.db')
    cur = con.cursor()      
    cur.execute("create table if not exists login(username varchar(20) PRIMARY KEY, password varchar(20), name varchar(50))")
    con.commit()
    con.close()
    
def create_admin():
    global flag
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    cur.execute("select * from login where username='admin'")
    status = cur.fetchall()
    if (len(status))==0:
        cur.execute("insert into login values ('admin', 'admin', 'Administrator')")
    else:
        flag=0
    con.commit()
    con.close()

def sign_in(index_ui,username, password):
    global showerror

    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    try:
        cur.execute("select count(*) from login where username=? and password=?", (username, password))
    except:
        messagebox.showerror('ERROR', 'SIGNIN FAILED')
        
        
    status = cur.fetchall()
    if status[0][0]==1:
        index_ui.destroy()
        dashboard(username)
    else:
        messagebox.showerror('ERROR', 'SIGNING FAILED')
    
    con.commit()
    con.close()


def details_ui(option):
    global lb1,lb2,lb3,lb4,lb5,lb6,lb7,lb8,lb9,lb10,lb11,lb12,lb13,lb14,lb15,lb98,lb99
    global criminal_id,lockup_id,fname,lname,blood_group,father_name,gender,age,status,crime,state,city,street_no,house_no,doc,off_name
    details_ui = tk.Toplevel()
    details_ui.geometry("1280x720")
#    details_ui.resizable(0,0)
    bg = tk.PhotoImage(file="images/windows_bg.gif")
    lb1=tk.Label(details_ui, image=bg).place(x=0,y=0)

    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    
    cur.execute("create table if not exists criminals (criminal_id varchar(10) PRIMARY KEY, lockup_id varchar(10), fname varchar(15), lname varchar(15),blood_group varchar(3), father_name varchar(30), gender varchar(6), age number(3), status varchar(15), crime varchar(15), state text,city varchar(10), street_no varchar(10), house_no varchar(10), Date_of_Crime text, Officers_Name varchar(15))") 

    lb2=tk.Label(details_ui, text='Criminal ID: ', font='Helvetica 11 bold',bg='#34383C',fg='white', borderwidth=0).place(x=320, y=50)
    criminal_id = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    criminal_id.place(x=700, y=50)


    lb3=tk.Label(details_ui, text="Lockup ID, Place: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=80)
    lockup_id = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    lockup_id.place(x=700, y=80)

    lb4=tk.Label(details_ui, text="First Name: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=110)
    fname = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    fname.place(x=700, y=110)
    
    lb5=tk.Label(details_ui, text="Last Name: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=140)
    lname = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    lname.place(x=700, y=140)

    lb6=tk.Label(details_ui, text="Blood Group: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=170)
    blood_group = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    blood_group.place(x=700, y=170)
    
    lb7=tk.Label(details_ui, text="Father's Name: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=200)
    father_name = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    father_name.place(x=700, y=200)

    lb8=tk.Label(details_ui, text="Gender: ", font='Helvetica 11 bold',bg='#34383C',fg='white')
    lb8.place(x=320, y=230)
    gender = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    gender.place(x=700, y=230)
     
    lb9=tk.Label(details_ui, text="Age: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=260)
    age = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    age.place(x=700, y=260)

    lb10=tk.Label(details_ui, text="Status: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=290)
    status = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    status.place(x=700, y=290)

    lb11=tk.Label(details_ui, text="Crime: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=320)
    crime = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    crime.place(x=700, y=320)

    lb12=tk.Label(details_ui, text="State: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=350)
    state = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    state.place(x=700, y=350)

    lb13=tk.Label(details_ui, text="City: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=380)
    city = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    city.place(x=700, y=380)

    lb14=tk.Label(details_ui, text="Street No: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=410)
    street_no = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    street_no.place(x=700, y=410)

    lb15=tk.Label(details_ui, text="House No: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=440)
    house_no = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    house_no.place(x=700, y=440)
    
    lb98=tk.Label(details_ui, text="Date of Crime: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=470)
    doc = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    doc.place(x=700, y=470)
    
    lb99=tk.Label(details_ui, text="Officer's Name: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=320, y=500)
    off_name = tk.Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    off_name.place(x=700, y=500)
    
    con.commit()
    con.close()
    
    def insert_sql():
#        global con,cur
#        con = sqlite3.connect('DB.db')
#        cur = con.cursor()
        try:
              global criminal_id,lockup_id,fname,lname,blood_group,father_name,gender,age,status,crime,state,city,street_no,house_no
              conn = sqlite3.connect("DB.db")
              cur = conn.cursor()
#    cur.execute("INSERT INTO user VALUES(?,?,?,?)",
#                (fn,ln,un,pw))
              cur.execute("""INSERT INTO criminals VALUES(:criminal_id,:lockup_id,:fname,:lname,
                                           :blood_group,:father_name,:gender,:age,
                                           :status,:crime,:state,:city,
                                           :street_no,:house_no,:Date_of_Crime,:Officers_Name)""", 
    
                {'criminal_id':criminal_id.get(),
                 
                 'lockup_id':lockup_id.get(),
                 'fname':fname.get(),
                 'lname':lname.get(),
                 'blood_group':blood_group.get(),
                 'father_name':father_name.get(),
                 'gender':gender.get(),
                 'age':age.get(),
                 'status':status.get(),
                 'crime':crime.get(),
                 'state':state.get(),
                 'city':city.get(),
                 'street_no':street_no.get(),
                 'house_no':house_no.get(),
                 'Date_of_Crime':doc.get(),
                 'Officers_Name':off_name.get()
                 
                }
                )
              messagebox.showinfo('Inserted', 'Values are inserted')
              conn.commit()
              conn.close()
#            cur.execute("insert into criminals values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (criminal_id.get(), lockup_id.get(), fname.get(), lname.get(), blood_group.get(), father_name.get(), gender.get(), age.get(), status.get(), crime.get(), state.get(), city.get(), street_no.get(), house_no.get()))
#            messagebox.showinfo('Inserted', 'Values are inserted')
        except:
            messagebox.showerror('ERROR', 'Insertion failed')

    if(option=='insert'):
        global lb16,b1
        lb16=tk.Label(details_ui, text='ENTER THE DETAILS ', borderwidth=0, bg='white',font='Helvetica 18 bold').place(x=640, y=10)
        b1=tk.Button(details_ui, text='INSERT', font='Helvetica 14 bold',bg='#373E44',fg='white',borderwidth=10, command=insert_sql).place(x=750, y=580)
    
    def update():
        
        conn=sqlite3.connect('DB.db')
         #Create Cursor
        c=conn.cursor()
        try:
            global que,val,lb54,b22
            c.execute("UPDATE criminals set lockup_id=?, fname=?, lname=?, blood_group=?, father_name=?, gender=?, age=?, status=?,crime=?,state=?, city=?, street_no=?, house_no=? where criminal_id=?",(lockup_id.get(), fname.get(), lname.get(), blood_group.get(), father_name.get(), gender.get(), age.get(), status.get(), crime.get(), state.get(), city.get(), street_no.get(), house_no.get(),criminal_id.get()))
#            details_ui.destroy()
            messagebox.showinfo('UPDATED', 'DATA UPDATED')
            conn.commit()
            conn.close()
        except:
            messagebox.showerror('ERROR', 'Failed to Update')
            
                     
    if(option=='update'):
        lb54=tk.Label(details_ui, text='VIEW AND UPDATE', borderwidth=0, bg='white', font='Helvetica 18 bold').place(x=640, y=10)
        lb54=tk.Label(details_ui, text='Enter criminal id click VIEW and then UPDATE attributes you want', borderwidth=0, bg='white', font='Helvetica 12 bold').place(x=9, y=10)
        tk.Button(details_ui, text='VIEW', font='Helvetica 14 bold',bg='#373E44',fg='white',borderwidth=10, command=lambda:view_sql(criminal_id.get())).place(x=750 , y=570)
        b22=tk.Button(details_ui, text='UPDATE', font='Helvetica 14 bold',bg='#373E44',fg='white',borderwidth=10, command=update).place(x=850, y=570)
                     
    
    def view_sql(criminal_id):
#        global criminal_id,lockup_id,fname,lname,blood_group,father_name,gender,age,status,crime,state,city,street_no,house_no,doc,off_name
        global lb18
        
        try:
            
         #Create Cursor
            conne=sqlite3.connect('DB.db')
            c=conne.cursor()
            c.execute("select * from criminals where criminal_id=?", [criminal_id])
            details = c.fetchall()[0]

            if(len(lockup_id.get())!=0):
               lockup_id.delete(0,'END')
            lockup_id.insert(0, details[1])
            if(len(fname.get())!=0):
                fname.delete(0,'END')
            fname.insert(0,details[2])
            if(len(lname.get())!=0):
                lname.delete(0,'END')
            lname.insert(0,details[3])
            if(len(blood_group.get())!=0):
                blood_group.delete(0,'END')
            blood_group.insert(0,details[4])
            if(len(father_name.get())!=0):
                father_name.delete(0,'END')
            father_name.insert(0,details[5])
            if(len(gender.get())!=0):
                gender.delete(0,'END')
            gender.insert(0,details[6])
            if(len(age.get())!=0):
                age.delete(0,'END')
            age.insert(0,details[7])
            if(len(status.get())!=0):
                status.delete(0,'END')
            status.insert(0,details[8])
            if(len(crime.get())!=0):
                crime.delete(0,'END')
            crime.insert(0,details[9])
            if(len(state.get())!=0):
                state.delete(0,'END')
            state.insert(0,details[10])
            if(len(city.get())!=0):
                city.delete(0,'END')
            city.insert(0,details[11])
            if(len(street_no.get())!=0):
                street_no.delete(0,'END')
            street_no.insert(0,details[12])
            if(len(house_no.get())!=0):
                house_no.delete(0,'END')
            house_no.insert(0,details[13])
            if(len(doc.get())!=0):
                doc.delete(0,'END')
            doc.insert(0,details[14])
            if(len(off_name.get())!=0):
                off_name.delete(0,'END')
            off_name.insert(0,details[15])
            conne.commit()
            conne.close()  
        except:
            messagebox.showerror('ERROR', 'Criminal record is not available for this ID')
              
#    if (option=='view'):
#        tk.Button(details_ui, text='VIEW', font='Helvetica 11 bold',bg='#373E44',fg='white',borderwidth=0, command=lambda:view_sql(criminal_id.get())).place(x=460 , y=520)
#        lb18=tk.Label(details_ui, text='Enter Criminal id only', borderwidth=0, bg='white',font=(12)).place(x=360, y=10)
#        
    
    details_ui.mainloop()

def create_acc():
    global lb19,lb20,lb21,lb22,lb23
    create_win = tk.Toplevel()
    create_win.geometry("1280x720")
#    create_win.resizable(0,0)
    
    new_user_bg = tk.PhotoImage(file="images/other_bg.gif")
    lb19=tk.Label(create_win, image=new_user_bg).place(x=0, y=0)
    lb20=tk.Label(create_win, text="CREATE AN ACCOUNT", font="Helvetica 15 bold", fg='white', bg='#34383C').place(x=331, y=60)

    username = tk.Entry(create_win, font=(13))
    lb21=tk.Label(create_win, text='Username', fg = '#34383C', bg='white', font='Helvetica 11 bold').place(x=300, y=160)
        
    password = tk.Entry(create_win, font=(13))
    lb22=tk.Label(create_win, text='Password', fg = '#34383C', bg='white',font='Helvetica 11 bold').place(x=300, y=260)
        
    name = tk.Entry(create_win, font=(13))
    lb23=tk.Label(create_win, text='Name', fg = '#34383C', bg='white', font='Helvetica 11 bold').place(x=300, y=360)

        
    username.place(x=300, y=200)
    password.place(x=300, y=300)
    name.place(x=300, y=400)
  

    tk.Button(create_win, text=' '*20+' SUBMIT'+' '*22, bg='#00BC90', fg='#34383C',font='Helvetica 15' ,borderwidth=0, command=lambda:submit()).place(x=270, y=490)
    def submit():
        conn=sqlite3.connect('DB.db')
         #Create Cursor
        cur=conn.cursor()
        try:
            cur.execute("insert into login values(?,?,?)", (username.get(), password.get(), name.get()))
            messagebox.showinfo("CREATED", "ACCOUNT CREATED, NOW YOU CAN LOG IN TO THE APPLICATION")
            
        except:
            messagebox.showerror("ERROR", "YOUR ACCOUNT IS PROBABLY ALREADY REGISTERED , TRY LOGGING IN AND IF THE PROBLEM PERSISTS SEE HELP MENU")
        conn.commit()
        conn.close()
            
    create_win.mainloop()

def search():
    
    def populateView():
        tree.delete(*tree.get_children())
        global que,val
        conn=sqlite3.connect('DB.db')
         #Create Cursor
        c=conn.cursor()
        
        c.execute("SELECT * FROM criminals WHERE crime=? OR Date_of_Crime=? OR Officers_Name=? ",(txt.get(),txt1.get(),txt2.get(),))
        fetch = c.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15]))
#            data[18]))
        c.close()
        conn.close()
##        global criminal_id,lockup_id,fname,lname,blood_group,father_name,gender,age,status,crime,state,city,street_no,house_no
    search_ui = tk.Toplevel() 
    search_ui.title("SEARCH FOR RECORDS")
    search_ui.geometry("400x400")
    search_ui.configure(background = "white")
    message =tk.Label(search_ui, text="SEARCH CRIMINAL RECORDS" ,fg="black",bg="white" ,width=55 ,height=1,font=('times', 29, ' bold '))
    message.place(x=10, y=10)
    frame3 = tk.Frame(search_ui, bg="#FFC8FB")
#    frame3.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)
    frame3.place(relx=0.11, rely=0.09, relwidth=0.39, relheight=1.00)
    l14 = tk.Label(frame3, text="ENTER ANY INFORMATION OF THE FOLLOWING",width=50 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 12, ' bold ') )
    l14.place(x=0, y=40)
    
    l7 = tk.Label(frame3, text="CRIME NAME ",width=15 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 15, ' bold ') )
    l7.place(x=0, y=80)
    global txt
    txt=tk.StringVar()
    txt = tk.Entry(frame3,textvariable=txt,width=27 ,fg="black",font=('times', 15, ' bold '))
    txt.place(x=200, y=80)   
    
    l12 = tk.Label(frame3, text="OR ",width=15 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 15, ' bold ') )
    l12.place(x=150, y=130)
    
    l10 = tk.Label(frame3, text="DATE OF CRIME",width=15 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 15, ' bold ') )
    l10.place(x=0, y=180)
    global txt1
    txt1=tk.StringVar()
    txt1 = tk.Entry(frame3,textvariable=txt1,width=27 ,fg="black",font=('times', 15, ' bold '))
    txt1.place(x=200, y=180) 
    
    l13 = tk.Label(frame3, text="OR ",width=15 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 15, ' bold ') )
    l13.place(x=150, y=230)
#    ,command=pgrade
    l21 = tk.Label(frame3, text="OFFICER'S NAME",width=15 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 15, ' bold ') )
    l21.place(x=0, y=280)
    global txt2
    txt2=tk.StringVar()
    txt2 = tk.Entry(frame3,textvariable=txt2,width=27 ,fg="black",font=('times', 15, ' bold '))
    txt2.place(x=200, y=280)
    clearButton9=tk.Button(frame3, text="SEARCH",fg="white"  ,bg="black"  ,command=populateView,width=20,activebackground = "white" ,font=('times', 14, ' bold '))
    clearButton9.place(x=150, y=360) 
    
   
    
    frame4 =tk.Frame(search_ui, bg="#FFC8FB")
##    frame4.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)
    frame4.place(relx=0.51, rely=0.09, relwidth=0.45, relheight=0.90)
#    
#    head5 = tk.Label(frame4, text="                       DETAILS                    ", fg="black",bg="#FFC8FB" ,font=('times', 17, ' bold ') )
#    head5.place(x=0,y=0)
    
    scrollbary =tk.Scrollbar(frame4, orient=tk.VERTICAL)
    scrollbarx =tk.Scrollbar(frame4, orient=tk.HORIZONTAL)

    tree = ttk.Treeview(frame4, columns=("criminal_id", "lockup_id", "fname", "lname", "blood_group",
                                         "father_name","gender","age","status","crime",
                                         "state","city","street_no","house_no","Date_of_Crime","Officers_Name"), 
    selectmode="extended",height=200, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
    
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
    
    tree.heading('criminal_id', text="Criminal Id", anchor=tk.W)
    tree.heading('lockup_id', text="Lockup Id", anchor=tk.W)
    tree.heading('fname', text="First Name", anchor=tk.W)
    tree.heading('lname', text="Last Name", anchor=tk.W)
    tree.heading('blood_group', text="Blood Group", anchor=tk.W)
    tree.heading('father_name', text="Father Name", anchor=tk.W)
    tree.heading('gender', text="Gender", anchor=tk.W)
    tree.heading('age', text="Age", anchor=tk.W)
    tree.heading('status', text="Status", anchor=tk.W)
    tree.heading('crime', text="Crime", anchor=tk.W)
    tree.heading('state', text="State", anchor=tk.W)
    tree.heading('city', text="City", anchor=tk.W)
    tree.heading('street_no', text="Street Number", anchor=tk.W)
    tree.heading('house_no', text="House Number", anchor=tk.W)
    tree.heading('Date_of_Crime', text="Date of Crime", anchor=tk.W)
    tree.heading('Officers_Name', text="Officer's Name", anchor=tk.W)

    
    tree.column('#0', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#1', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#2', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#3', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#4', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#5', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#6', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#7', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#8', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#9', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#10', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#11', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#12', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#13', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#14', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#15', stretch=tk.NO, minwidth=0, width=50)
    tree.column('#16', stretch=tk.NO, minwidth=0, width=50)
#    tree.column('#17', stretch=tk.NO, minwidth=0, width=50)

    tree.pack()
    
    search_ui.mainloop()
    
def analyse():
    def  maxmin():
        conne=sqlite3.connect('DB.db')
        c=conne.cursor()
#        , COUNT(crime)
        c.execute("SELECT DISTINCT(crime) FROM criminals  GROUP BY crime HAVING COUNT (crime)=( SELECT MAX(crime_count) FROM ( SELECT crime, COUNT(crime) as crime_count FROM criminals GROUP BY crime))")
        details=[]
        details = c.fetchall()
        print(details)
        if(len(tt2.get())!=0):
            tt2.delete(0,'END')
        tt2.insert(0,details)
        conne.commit()
        conne.close()
        
    def  minmax():
        conne=sqlite3.connect('DB.db')
        c=conne.cursor()
#        , COUNT(crime)
        c.execute("SELECT DISTINCT(crime) FROM criminals  GROUP BY crime HAVING COUNT (crime)=( SELECT MIN(crime_count) FROM ( SELECT crime, COUNT(crime) as crime_count FROM criminals GROUP BY crime))")
        details=[]
        details = c.fetchall()
        print(details)
        if(len(tt1.get())!=0):
            tt1.delete(0,'END')
        tt1.insert(0,details)
        conne.commit()
        conne.close()
    def statemax():
        tree.delete(*tree.get_children())
        global qu,va
        conne=sqlite3.connect('DB.db')
        c=conne.cursor()
#        , COUNT(crime)
        print(tkvar.get()) 
#        ,MAX(crime_count)
#        c.execute("select crime,MAX(crime_count) from(select crime,count(crime) as crime_count from criminals where state=? group by crime)",(tkvar.get(),))
#        c.execute("select DISTINCT(crime) from criminals group by crime,state having count(crime)=(select MAX(crime_count) from(select crime,count(crime) as crime_count from criminals where state=? group by crime))",(tkvar.get(),))
        c.execute("SELECT DISTINCT(crime),count(crime),state from criminals where state=? group by crime,state ORDER BY count(crime) DESC ",(tkvar.get(),))
#        details=[]
#        details = c.fetchall()
#        print(details)
###        T.insert(tk.END, details)
##        details = c.fetchall()[0]
#        if(len(xt1.get())!=0):
#            xt1.delete(0,'END')
#        xt1.insert(0,details)
        fetch = c.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0],data[1]))
#            data[18]))
      
        
        conne.commit()
        conne.close()
        
    def statemin():
        conne=sqlite3.connect('DB.db')
        c=conne.cursor()
#        , COUNT(crime)
        c.execute("select DISTINCT(crime) from criminals group by crime,state having count(crime)=(select MIN(crime_count) from(select crime,count(crime) as crime_count from criminals where state=? group by crime))",(tkvar.get(),))
#        c.execute("SELECT * FROM criminals WHERE crime=? OR Date_of_Crime=? OR Officers_Name=? ",(txt.get(),txt1.get(),txt2.get(),))
        details=[]
        details = c.fetchall()
        print(details)
        if(len(xt2.get())!=0):
            xt2.delete(0,'END')
        xt2.insert(0,details)
        conne.commit()
        conne.close()

        
    ana_ui=tk.Toplevel()
    ana_ui.geometry("1280x720")
    ana_ui.title("ANALYSE CRIME RECORDS")
    ana_ui.configure(background = "white")
    message =tk.Label(ana_ui, text="ANALYSE CRIMINAL RECORDS" ,fg="black",bg="white" ,width=55 ,height=1,font=('times', 29, ' bold '))
    message.place(x=10, y=10)
    frame3 = tk.Frame(ana_ui, bg="#FFC8FB")
#    frame3.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)
    frame3.place(relx=0.00, rely=0.09, relwidth=0.50, relheight=1.00)
#    frame3 = tk.Frame(ana_ui, bg="#FFC8FB")
##    frame3.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)
#    frame3.place(relx=0, rely=0.09, relwidth=1.00, relheight=1.00)
#    CHECK THE CRIME COMMITTED CLICKING THE BUTTONS BELOW IRRESPECTIVE OF STATES
    l14 = tk.Label(frame3, text="COUNTRY WIDE",width=50 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 12, ' bold ') )
    l14.place(x=10, y=40)

    cbtn1=tk.Button(frame3, text="MAXIMUM",fg="white"  ,bg="black" ,command=maxmin  ,width=20,activebackground = "white" ,font=('times', 14, ' bold '))
    cbtn1.place(x=10, y=80)
    
    global tt2
    tt2=tk.StringVar()
    tt2 = tk.Entry(frame3,textvariable=tt2,width=27 ,fg="black",font=('times', 15, ' bold '))
    tt2.place(x=250, y=80)
    
   
    cbtn2=tk.Button(frame3, text="MINIMUM",fg="white",command=minmax,bg="black"  ,width=20,activebackground = "white" ,font=('times', 14, ' bold '))
    cbtn2.place(x=10, y=180)
    
    global tt1
    tt1=tk.StringVar()
    tt1 = tk.Entry(frame3,textvariable=tt1,width=27 ,fg="black",font=('times', 15, ' bold '))
    tt1.place(x=250, y=180)
    
    
    l15 = tk.Label(frame3, text="STATE WISE",width=50 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 12, ' bold ') )
    l15.place(x=10, y=270)

    global tkvar
    tkvar = tk.StringVar(ana_ui)

# Dictionary with options
    choices = [ "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Nagpur","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","Dehradun","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Jammu and Kashmir","Ladakh","Kargil","Lakshadweep","Puducherry"]
    tkvar.set('SELECT') # set the default option
    popupMenu =tk.OptionMenu(frame3, tkvar, *choices)
    popupMenu.config(width=15, font=('times', 12))
    popupMenu.place(x=10,y=360)
#     w = apply(tk.OptionMenu, (ana_ui, tkvar) + tuple(choices))
#    w.config(width=15, font=('times', 12))
#    w.place(x=20,y=350)
#    w.pack()
    def change_dropdown(*args):
        print( tkvar.get() )

# link function to change dropdown
    tkvar.trace('w', change_dropdown)
    



    
    cbt1=tk.Button(frame3, text="MAXIMUM",command=statemax,fg="white"  ,bg="black"  ,width=20,activebackground = "white" ,font=('times', 14, ' bold '))
    cbt1.place(x=10, y=420)
    
    
    global xt1
    xt1=tk.StringVar()
    xt1 = tk.Entry(frame3,textvariable=xt1,width=27 ,fg="black",font=('times', 15, ' bold '))
    xt1.place(x=250, y=420)
  

#    T = tk.Text(ana_ui, height=4, width=70)
##    S = tk.Scrollbar(ana_ui)
#    scrollbary =tk.Scrollbar(ana_ui, orient=tk.VERTICAL)
#    scrollbarx =tk.Scrollbar(ana_ui, orient=tk.HORIZONTAL)
##    S.pack(side=tk.RIGHT, fill=tk.Y)
##    T.pack(side=tk.LEFT, fill=tk.Y)
#    T.place(x=250,y=400)
##    S.config(command=T.yview)
#    scrollbary.config(command=T.yview)
#    scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
#    
#    scrollbarx.config(command=T.xview)
#    scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
#    T.config(yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
    
    cbt2=tk.Button(frame3, text="MINIMUM",command=statemin,fg="white",bg="black"  ,width=20,activebackground = "white" ,font=('times', 14, ' bold '))
    cbt2.place(x=10, y=500) 
        
    global xt2
    xt2=tk.StringVar()
    xt2 = tk.Entry(frame3,textvariable=xt2,width=27 ,fg="black",font=('times', 15, ' bold '))
    xt2.place(x=250, y=500)
    
#    l20 = tk.Label(frame3, text="Following is the crime name committed maximum number of times in the chosen state",width=100 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 12, ' bold ') )
#    l20.place(x=10, y=390)
#    l19 = tk.Label(frame3, text="Following is the crime name committed maximum number of times in the chosen state",width=100 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 12, ' bold ') )
#    l19.place(x=10, y=430)
    frame4 =tk.Frame(ana_ui, bg="#FFC8FB")
##    frame4.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)
    frame4.place(relx=0.51, rely=0.09, relwidth=0.47, relheight=0.90)
    scrollbary =tk.Scrollbar(frame4, orient=tk.VERTICAL)
    scrollbarx =tk.Scrollbar(frame4, orient=tk.HORIZONTAL)

    tree = ttk.Treeview(frame4, columns=("crime", "crime_count"), 
    selectmode="extended",height=200,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
    
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
    
    tree.heading('crime', text="CRIME", anchor=tk.W)
    tree.heading('crime_count', text="CRIME_COUNT", anchor=tk.W)
    
    tree.column('#0', stretch=tk.NO, minwidth=0, width=100)
    tree.column('#1', stretch=tk.NO, minwidth=0, width=100)
    tree.column('#2', stretch=tk.NO, minwidth=0, width=100)
    
    tree.pack()
    
    


    ana_ui.mainloop()
    
    
    
            
    
  
    
#l7 = tk.Label(frame3, text="CRIME NAME ",width=15 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 15, ' bold ') )
#l7.place(x=0, y=80)
#    
#    
#l12 = tk.Label(frame3, text="OR ",width=15 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 15, ' bold ') )
#l12.place(x=150, y=130)
#    
#l10 = tk.Label(frame3, text="DATE OF CRIME",width=15 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 15, ' bold ') )
#l10.place(x=0, y=180)
#     
#    
#l13 = tk.Label(frame3, text="OR ",width=15 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 15, ' bold ') )
#l13.place(x=150, y=230)
##    ,command=pgrade
#    l21 = tk.Label(frame3, text="OFFICER'S NAME",width=15 ,fg="black"  ,bg="#FFC8FB" ,font=('times', 15, ' bold ') )
#    l21.place(x=0, y=280)
#    global txt2
#    txt2=tk.StringVar()
#    txt2 = tk.Entry(frame3,textvariable=txt2,width=27 ,fg="black",font=('times', 15, ' bold '))
#    txt2.place(x=200, y=280)
#    clearButton9=tk.Button(frame3, text="SEARCH",fg="white"  ,bg="black"  ,command=populateView,width=20,activebackground = "white" ,font=('times', 14, ' bold '))
#    clearButton9.place(x=150, y=360) 

    
def remove():
    global lb24,lb25,lb26,lb59
    remove_ui = tk.Toplevel()
    remove_ui.geometry("1280x720")
#    remove_ui.resizable(0,0)
    bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/other_bg.gif")
    lb24=tk.Label(remove_ui, image=bg).place(x=0,y=0)

    lb25=tk.Label(remove_ui, text='DELETE A CRIMINAL RECORD',font="times 30 bold", fg='white', bg='#34383C').place(x=340, y=60)
    lb26=tk.Label(remove_ui, text='ENTER CRIMINAL ID', fg = '#34383C', bg='white', font='Helvetica 18 bold').place(x=500, y=280)
    to_remove = tk.Entry(remove_ui, font=(13))
    to_remove.place(x=500, y=330)
    def execute_remove(to_remove):
       
        co=sqlite3.connect('DB.db')
         #Create Cursor
        cr=co.cursor()
        cr.execute("DELETE from criminals where criminal_id = ?",[to_remove.get()])
        messagebox.showinfo('Deleted', 'Values are deleted')
        co.commit()
        co.close()
    tk.Button(remove_ui, text=' '*20 + 'DELETE' + ' '*20,bg='#F85661', fg='#34383C',borderwidth=10, font='Helvetica 15 bold',command=lambda:execute_remove(to_remove)).place(x=440, y=490)
#    con.commit()
    remove_ui.mainloop()
    
def dashboard(username):
    global lb27,lb28,lb29,lb30,lb31,lb32,lb33,lb34,lb35,lb53,l101,l102
    dash_ui =tk.Tk()
    dash_ui.geometry("1280x720")
#    dash_ui.resizable(0,0)
    bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/dashboard_bg.gif")
    lb27=tk.Label(dash_ui, relief="flat",image=bg).grid(row=0, column=0, rowspan=20, columnspan=20)

    #user_bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/user.gif")
    #lb28=tk.Label(dash_ui, image=user_bg,borderwidth=0).place(x=800 , y=6.5)
    
    logout = tk.Button(dash_ui,bg='#16202C', borderwidth=0, command=lambda:dash_ui.destroy())
    logout_bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/logout.gif")
    logout.config(image=logout_bg)
    logout.place(x=1200, y=10)
    lb29=tk.Label(dash_ui, text='DASHBOARD',fg='white',bg='#34383C', font='Helvetica 18 bold').place(x=45, y=50)
    lb30=tk.Label(dash_ui, text='WELCOME '+username.upper() , bg='#34383C', fg='#ffffff', font = 'Helvetica 30 bold').place(x=540, y=10)
    
    add_bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/plus.gif")
    lb31=tk.Label(dash_ui, bg='#16202C', borderwidth=0, image=add_bg).place(x=10, y=105)
    tk.Button(dash_ui, text='INSERT', bg='#34383C', fg='#ffffff', font='4', borderwidth=0, command=lambda:details_ui('insert')).place(x=84, y=105)

    minus_bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/minus.gif")
    lb32=tk.Label(dash_ui, bg='#16202C', borderwidth=0,image=minus_bg).place(x=8.4,y=155)
    tk.Button(dash_ui, text='DELETE', bg='#34383C', fg='#ffffff', font='4', borderwidth=0, command=lambda:remove()).place(x=84, y=156)

    update_bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/update.gif")
    lb33=tk.Label(dash_ui, bg='#16202C', borderwidth=0,image=update_bg).place(x=8.4,y=205)
    tk.Button(dash_ui, text='UPDATE', bg='#34383C', fg='#ffffff', font='4', borderwidth=0, command=lambda:details_ui('update')).place(x=84, y=207)

#    view_bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/view.gif")
#    lb34=tk.Label(dash_ui, bg='#16202C', borderwidth=0,image=view_bg).place(x=9.6,y=255)
#    tk.Button(dash_ui, text='VIEW', bg='#34383C', fg='#ffffff', font='4', borderwidth=0, command=lambda:details_ui('view')).place(x=84, y=258)
    
    search_bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/search.gif")
    lb53=tk.Label(dash_ui, bg='#16202C', borderwidth=0,image=search_bg).place(x=9.6,y=255)
    tk.Button(dash_ui, text='SEARCH', bg='#34383C', fg='#ffffff', font='4', borderwidth=0, command=lambda:search()).place(x=84, y=258)
    
    anal_bg= tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/anal.gif")
    l102=tk.Label(dash_ui, bg='#16202C', borderwidth=0,image=anal_bg).place(x=9.6,y=310)
    tk.Button(dash_ui, text=' CRIME ANALYSIS', bg='#34383C', fg='#ffffff', font='4', borderwidth=0,command=lambda:analyse()).place(x=84, y=309)
              
    add_user = tk.Button(dash_ui,borderwidth=0,bg='#16202C', command=create_acc)
    add_user_bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/add_user.gif")
    add_user.config(image=add_user_bg)
    add_user.place(x=1100, y=4)

    graph = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/flag.gif")
    lb35=tk.Label(dash_ui, image=graph, borderwidth=0).place(x=280,y=85)
    
    poster = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/poster.gif")
    l101=tk.Label(dash_ui, image=poster, borderwidth=0).place(x=540,y=95)


    
    dash_ui.mainloop()
