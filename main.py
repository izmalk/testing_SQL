import mysql.connector
from mysql.connector import Error


def connect2db(db): #various actions with selected DB
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='',
                                             database=db)

        if connection.is_connected(): #Successfull conection
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
                if action == 1:
                    print("Executing show table command...")
                    query = "SELECT * FROM users"
                    cursor.execute(query)
                    records = cursor.fetchall()
                    for record in records:
                        print(record)
                elif action == 2:  # Add record
                    name = input("Name of the user to add: ")
                    login = input("Login name of the user to add: ")
                    query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
                    values = (name, login)
                    cursor.execute(query, values)
                    connection.commit()
                    print(cursor.rowcount, "User added")
                elif action == 3:  # Delete record
                    login = input("Type in login of the user to delete: ")
                    query = "DELETE FROM users WHERE name = '" + login + "'"
                    cursor.execute(query)
                    print("Processing transaction...")
                    connection.commit()
                    print("User deleted")

                elif action == 4:  # SQL Command
                    s = input("Type in correct SQL command: ")
                    cursor.execute(s)
                    connection.commit()

                else:  # other
                    print("Invalid choice. Session terminated.")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        print("All instructions complete. Closing connection...")
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# check whether the db exist
def check_db(db):
    if db == '':
        print("Empty input")
        return 2
    else:
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 user='root',
                                                 password='')

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version!!! ", db_Info)
                cursor = connection.cursor()

                print("Requesting databases list...")
                cursor.execute("SHOW DATABASES")

                print("Getting the answer...")
                databases = cursor.fetchall()  # it returns a list of all databases present
                print("List of databases: ", databases)
                # printing the list of databases
                print("Printing every database name:")
                # showing one by one database
                n = 1
                f = False
                for database in databases:
                    if database[0] == db:
                        print(n, ": ", database[0], " — found")
                        f = True
                        return 3
                    n = n + 1
                if not f:
                    print("Creating a database " + db)
                    cursor.execute("CREATE DATABASE " + db)
                    return 4

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


def initialise_db(db):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='',
                                             database=db)

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version!!! ", db_Info)
            cursor = connection.cursor()

            print("Preparing auto generated contents for the database " + db)
            cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")
            print("Table users created.")

            query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
            values = [
                ("Peter", "peter"),
                ("Amy", "amy"),
                ("Michael", "michael"),
                ("Hennah", "hennah"),
                ("Bob", "marley"),
                ("Alexander", "alex"),
                ("Vasilisa", "vasya")
            ]
            #cursor.execute(query, values)
            cursor.executemany(query, values)
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == '__main__':
    db_name = input("Type in database name to proceed: ")
    check_result = check_db(db_name)
    if check_result == 2:
        print("Empty input — Terminating program!")
    elif check_result == 3: #the DB existed before
        connect2db(db_name)
    elif check_result == 4: #new DB - just created
        initialise_db(db_name)
        connect2db(db_name)
    else:
        print("Invalid behaviour!")
