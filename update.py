import mysql.connector
from mysql.connector import Error

db = input("Type in database name: ")
name = input("Type in new name for id = 4: ")

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='',
                                         database=db)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version!!! ", db_Info)
        cursor = connection.cursor()

        print("Updating data...")
        cursor.execute("UPDATE users SET name = '" + name + "' WHERE id = 4")
        connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
