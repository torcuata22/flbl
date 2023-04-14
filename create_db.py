#connect to db: MySQL connector
#install connectors:pip install myqsl-connector
#install connectors:pip install myqsl-connector-python
#install connectors:pip install myqsl-connector-python-rf (this one fails)
#Once connectors installed:

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pa55w0rd123",
)

my_cursor=mydb.cursor()
#my_cursor.execute("CREATE DATABASE our_users") -->just in case

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

#will need to pip install pymysql to create db (MySQLdb module not found)
#pip install cryptography
