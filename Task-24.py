import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)
print(mydb)
dbse = mydb.cursor()




# Create a database


import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)
print(mydb)
dbse = mydb.cursor()
dbse.execute("CREATE DATABASE JSONRECORDS")




#Show databases

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)
dbse = mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
  print(entry)





import json
json_data=[
    {'name':"Yogeswari",'age':20,'staff':True,'salary':45000.00,'dept':'CSE'},
     {'name':"Ramya",'age':25,'staff':False,'salary':55000.00,'dept':'CSE'},
     {'name':"Padma",'age':23,'staff':True,'salary':40000.00,'dept':'IT'},
     {'name':"Manas",'age':26,'staff':True,'salary':45000.00,'dept':'IT'},
     {'name':"Parnika",'age':25,'staff':True,'salary':40000.00,'dept':'CSE'},
    {'name':"Sree",'age':20,'staff':True,'salary':30000.00,'dept':'IT'}
    
]
res =json.dumps(json_data)






# Create a  table

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="password",
  database="jsonrecords"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE employee (name VARCHAR(255),age INT, permanent_staff VARCHAR(255), salary DOUBLE, dept_and_designation VARCHAR(255))")



# Show table

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="jsonrecords"
)
dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for value in dbse:
  print(value)





# Show column in table



import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="jsonrecords"
)
dbse = mydb.cursor()
dbse.execute("SHOW COLUMNS FROM employee")
for value in dbse:
  print(value)



