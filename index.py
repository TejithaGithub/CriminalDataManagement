# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:29:58 2020

"""

from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox
import dash


#LOGIN PAGE
dash.create()
dash.create_admin()


def index():
    global lb36,lb37,lb38,lb39,lb40,lb41,lb42,lb43,lb44
    index_ui =tk.Tk()
    index_ui.geometry("1280x720")
    index_ui.configure(background = "#FFC8FB")
#    index_ui.resizable(0,0)
#    bg =tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/background.gif")
#    lb36=tk.Label(index_ui,image=bg).grid(row=0, column=0, rowspan=80, columnspan=80)

#    lb37=tk.Label(index_ui, text='Welcome', font='Helvetica 18 ', fg='black', bg='white').place(x=10, y=10)
    lb38=tk.Label(index_ui, text='CRIMINAL RECORD MANAGEMENT SYSTEM ', font=('times',29,'bold'),fg='black').place(x=200, y=10)
#    message3 =tk.Label(window, text="STUDENT PERFORMANCE PREDICTION" ,fg="black",bg="white" ,width=55 ,height=1,font=('times', 29, ' bold '))
#message3.place(x=10, y=10)
    #    lb39=tk.Label(index_ui, text='Add / Remove / update and view the records using this interactive application', font='Helvetica 10', fg='black', bg='white').place(x=50, y=290)
#    lb40=tk.Label(index_ui, text='Reduced function calls, improved speed', font='Helvetica 10', fg='#0D90CB', bg='#34383C').place(x=50, y=310)
#    lb41=tk.Label(index_ui, text='Code made readable for further developement', font='Helvetica 10', fg='#0D90CB', bg='#34383C').place(x=50, y=330)
    

    logo = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/logo.gif")
    lb42=tk.Label(index_ui, image=logo,borderwidth=0).place(x=640,y=120)


    username_logo = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/username_logo.gif")
    lb43=tk.Label(index_ui, image=username_logo).place(x=600, y=260)
    username = tk.Entry(index_ui, font=(14),fg='#0B8FCC')
    username.place(x=635, y=260)

    pass_logo = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/password_logo.gif")
    lb44=tk.Label(index_ui, image=pass_logo).place(x=600, y=290)
    password = tk.Entry(index_ui, font=(14), show='*',fg='#0B8FCC')
    password.place(x=635, y=290)

    login_button = tk.Button(index_ui, borderwidth=0,bg='#1A2E39',command=lambda:dash.sign_in(index_ui,username.get(), password.get()))
    login_button_bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/login_button.GIF")
    login_button.config(image=login_button_bg)
    login_button.place(x=635 , y=370)

    help_button = tk.Button(index_ui, borderwidth=0, command=show_help,bg='#00BC90')
    help_bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/help.gif")
    help_button.config(image=help_bg)
    help_button.place(x=1100, y=570)
                      
    index_ui.mainloop()

def show_help():
    global lb45,lb46,lb47,lb48,lb49,lb50,lb51
    help_win = tk.Toplevel()
    help_win.geometry("1280x720")
#    help_win.resizable(0,0)

    help_win_bg = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/other_bg.gif")
    lb45=tk.Label(help_win, image=help_win_bg).place(x=0, y=0)

    lb46=tk.Label(help_win , text="Administrator's account", font="Helvetica 15 bold", fg='white', bg='#34383C').place(x=331, y=60)

    lb47=tk.Label(help_win, text='Username:', fg = '#34383C', bg='white', font='Helvetica 11 bold').place(x=300, y=160)
    lb48=tk.Label(help_win , text='admin', fg = '#34383C', bg='white', font='Helvetica 11 ').place(x=300, y=200)
    lb49=tk.Label(help_win, text='Password:', fg = '#34383C', bg='white',font='Helvetica 11 bold').place(x=300, y=260)
    lb50=tk.Label(help_win , text='admin', fg = '#34383C', bg='white', font='Helvetica 11 ').place(x=300, y=300)

    lb51=tk.Label(help_win , text='Use this password ', font = 'Helvetica 16 bold',bg='white', fg='#028CCA' ).place(x=300, y=400)
    help_win.mainloop()


    
root=tk.Tk()
root.geometry("1280x720")
#root.resizable(0,0)
root.overrideredirect(1)
#splash_image = tk.PhotoImage(file="C:/Users/Giri/OneDrive/Documents/hobby project/Images/splash.gif")

def to_index():
    root.destroy()
    index()
    
#global lb52
#lb52=tk.Label(root, image = splash_image).place(x=0,y=0)
root.after(3000,to_index)
root.mainloop()
