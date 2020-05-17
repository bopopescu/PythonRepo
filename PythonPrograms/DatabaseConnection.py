import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root',passwd='1234',database='learn' )

mycursors = mydb.cursor()
#mycursors.execute("show databases")
mycursors.execute("select * from student")

result = mycursors.fetchall()

#for i in mycursors:
for i in result:
    print(i)

