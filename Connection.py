import mysql
import mysql.connector as mysql
from mysql.connector import Error
import petl as etl
#connection = mysql.connector.connect(host='localhost',database='appmysql',user='root',password='Cummins@2020')
#connection = mysql.createConnection(host='localhost',database='appmysql',user='root',password='Cummins@2020')
#try:
connection = mysql.connect(host='localhost',database='appmysql',user='root',password='Cummins@2020')
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL database... MySQL Server version on ",db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print ("Your connected to - ", record)
    table = etl.fromdb(connection, 'SELECT * FROM student')
    print(table)
#except Error as e :
            #print ("Error while connecting to MySQL", e)
#finally:
               
if(connection.is_connected()):
    cursor.close()
    connection.close()
print("MySQL connection is closed")
