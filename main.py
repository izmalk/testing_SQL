import mysql.connector
from mysql.connector import Error

def connect2db(db=''):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='',
                                             database=db)

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()

            if db == '':
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
            else:
                print("Choose your action with table ", db, ":")
                print("1. Show all records")
                print("2. Add user")
                print("3. Delete user")
                print("4. Execute SQL command")
                action = int(input())
                if action == 1 :
                    print("Executing show table command...")
                    query = "SELECT * FROM users"
                    cursor.execute(query)
                    records = cursor.fetchall()
                    for record in records:
                        print(record)
                elif action == 2 : #Add record
                    name = input("Name of the user to add: ")
                    login = input("Login name of the user to add: ")
                    query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
                    values = (name, login)
                    cursor.execute(query, values)
                    connection.commit()
                    print(cursor.rowcount, "User added")
                elif action == 3 : #Delete record
                    login = input("Type in login of the user to delete: ")
                    query = "DELETE FROM users WHERE name = '" + login + "'"
                    cursor.execute(query)
                    print("Processing transaction...")
                    connection.commit()
                    print("User deleted")

                elif action == 4 : #SQL Command
                    s = input("Type in correct SQL command: ")
                    cursor.execute(s)
                    connection.commit()

                else : #other
                    print("Invalid choice. Session terminated.")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        print("All instructions complete. Closing connection...")
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == '__main__':
    connect2db(input("Type in database name: "))
