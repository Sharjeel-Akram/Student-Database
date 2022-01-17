import mysql.connector
import tkinter
from tkinter import Label, Entry, Button, messagebox

def Registration():
    mydb=mysql.connector.connect(host="localhost",user="root",password="12345", database= "mydatabase")
    mycursor = mydb.cursor()
    username  = User_TextField.get()
    password  = Pass_TextField.get()
    
    Username = username,
    Password = password,
    
    mycursor.execute("SELECT name from Students")
    Temp = mycursor.fetchall()
    Flag = False
    for i in Temp:
        if i == Username:
            Flag = True
    if Flag == True:
        print("Username Exists")
            
        messagebox.showinfo("Try Again", "This username is already exists, please enter new one")
    else:
        sql = "INSERT INTO Students (name, password) VALUES (%s, %s)"
        val = (username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        
        messagebox.showinfo("Stored", "This username has been stored in the table")
        
def Login():
    mydb=mysql.connector.connect(host="localhost",user="root",password="12345", database= "mydatabase")
    mycursor = mydb.cursor()
    username  = User_TextField.get()
    password  = Pass_TextField.get()
    
    Username = username,
    Password = password,
    
    mycursor.execute("SELECT name from Students")
    Temp = mycursor.fetchall()
    Flag = False
    for i in Temp:
        if i == Username:
            Flag = True
    mycursor.execute("SELECT password from Students")
    Temp1 = mycursor.fetchall()
    Flag1 = False
    for i in Temp1:
        if i == Password:
            Flag1 = True
    if Flag == True and Flag1 == True:
        root2 = tkinter.Tk()
        root2.title("Welcome")
        root2.geometry('400x250')
        root2.configure(bg = 'Light Blue')
        Text = Label(root2, text = 'Hey Handsome! Welcome to Namal Institute Mianwali',bg = 'Red').place(x=50,y=50)
        root2.mainloop()
    else:
        messagebox.showinfo("Login Failed", "Please Enter some legal Information.")

root = tkinter.Tk()
root.title("Login")
root.geometry('400x250')
root.configure(bg = 'Light Blue')

Username = Label(root, text = 'Username: ', bg = 'Yellow').place(x=30,y=40)
Passwrord = Label(root, text = 'Password:  ', bg = 'Yellow').place(x=30,y=65)

global User_TextField
global Pass_TextField

User_TextField = Entry(root, width = 30, bg = 'White')
User_TextField1 = User_TextField.place(x=100,y=40)
Pass_TextField = Entry(root, width = 30, bg = 'White')
Pass_TextField1 = Pass_TextField.place(x=100,y=65)

Button(root, text="Login", bg = 'Red', command=Login).place(x=30,y=90)
Button(root, text="Register", bg = 'Red', command= Registration).place(x=90, y=90)
root.mainloop()