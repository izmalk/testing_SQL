import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='',
                                         database='test_db')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version!!! ", db_Info)
        cursor = connection.cursor()

        print("Executing command...")
        cursor.execute("SHOW TABLES")

        tables = cursor.fetchall()

        ## showing all the tables one by one
        for table in tables:
            print(table[0])

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
