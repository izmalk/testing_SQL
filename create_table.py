import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='',
                                         database='testdb')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version!!! ", db_Info)
        cursor = connection.cursor()

        print("Executing command...")
        cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
