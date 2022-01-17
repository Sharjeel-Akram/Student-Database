import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="12345", database= "mydatabase")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Students (name VARCHAR(255), password VARCHAR(255))")

