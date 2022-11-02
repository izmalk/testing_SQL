import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

        print("Executing 'Show databases' command...")
        cursor.execute("SHOW DATABASES")

        print("Getting the answer...")
        databases = cursor.fetchall()  # it returns a list of all databases present
        print("List of databases: ", databases)
        # printing the list of databases
        print("Printing every database name:")
        # showing one by one database
        n = 1
        for database in databases:
            print(n, ": ", database[0])
            n = n + 1

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
