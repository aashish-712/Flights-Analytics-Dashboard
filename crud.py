import mysql.connector

#connection to my sql workbench
try:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '5555',
        database = 'indigo'
    )
    mycursor = conn.cursor()
    print("connection sucessfull")
except:
    print("connection unsucessfull")

#create database on database server
# myc ursor.execute("CREATE DATABASE indigo")
# conn.commit()

#create table 
# mycursor.execute("""
    #  CREATE TABLE airpot(
    #  airport_id INTEGER PRIMARY KEY,
    #  code VARCHAR(10) NOT NULL,
    #  name VARCHAR(255) NOT NULL,
    #  city VARCHAR(50) NOT NULL
# )
#     """)
# conn.commit()

#insert data to the table
# mycursor.execute("""
#     INSERT INTO airpot VALUES
#     (1, 'DEL', 'New Delhi', 'IGIA'),
#     (2,'CCU', 'Kolkata', 'NSCA'),
#     (3,'BOM', 'Mumbai', 'CSMA')
# """)
# conn.commit()


# Search / Retrieve
# mycursor.execute("SELECT * FROM airpot WHERE airport_id > 1")

# data = mycursor.fetchall()
# print(data)

# for i in data:
#     print(i[3])

#Update
# mycursor.execute("""
# UPDATE airpot
# SET name = 'Bombay'
# WHERE airport_id = 3
# """)
# conn.commit()


# #Delete
# mycursor.execute("DELETE FROM airpot WHERE airport_id = 3")
# conn.commit

# #retrive
# mycursor.execute("""
# SELECT * FROM airpot
# """)
# data = mycursor.fetchall()
# print(data)