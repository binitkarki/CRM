import mysql.connector
database=mysql.connector.connect(
    host='localhost',
    user= 'root',
    passwd='password1234',
)

#prepare a cursor object
cursorObject=database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE crm")

print("all done")