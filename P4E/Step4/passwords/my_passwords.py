#!/usr/bin/env python


import sqlite3

conn = sqlite3.connect('passwords.sqlite')
cur = conn.cursor()

# cur.execute("DROP TABLE IF EXISTS Passwords")



cur.execute('''
CREATE TABLE IF NOT EXISTS Passwords (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
website TEXT, 
login TEXT, 
email TEXT, 
password TEXT, 
addInfo TEXT)
''')

def showAll():
    cur.execute("SELECT * FROM Passwords")
    whole_table = cur.fetchall()
    for line in whole_table:
        print(line)
while True:
    command = input("What do you want to do: Show, Add, Update, Remove? Type Quit to exit").lower()
    if command == "quit" or command == "q":
        break

        # ----------------------------Block of code to SHOW item from the table-------------------------
    elif command == "show" or command == "s":
        req = input("What web-site? Press * to show all").lower()
        if req == "*":
            showAll()
        else:
            cur.execute('SELECT * FROM Passwords WHERE website = ? ', (req,))
            rows = cur.fetchall()
            for row in rows:
                print(row)

    #----------------------------Block of code to ADD item to the table-------------------------
    elif command == "add" or command == "a":

        website = input("Enter the website name: ").lower()
        login =  input("Enter the login name: ").lower()
        email =  input("Enter the mail to website: ").lower()
        password =  input("Enter the password to website: ")
        addInfo =  input("Enter the additional information to website: ").lower()
        parameters = [website, login, email, password, addInfo,]
        count = 1

        while count < len(parameters):
            if len(parameters[count]) < 1:
                parameters[count] = None
            count += 1


        cur.execute("INSERT INTO Passwords (website, login, email, password, addInfo) VALUES (?, ?, ?, ?, ?)",
                    (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4]))
        conn.commit()


        cur.execute("SELECT * FROM Passwords WHERE website = ? AND login = ? AND email = ? AND password = ? AND addInfo = ?",
                     (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4]))
        new_data = cur.fetchone()
        print("Your data ", new_data, "has been added successfully")

    #----------------------------Block of code to UPDATE the table-------------------------
    elif command == "update" or command == "u":
        showAll()
        while True:
            changed_numb = input("What Item you want to change? ")
            #changed_numb = int(input("What Item you want to change? "))
            cur.execute("SELECT * FROM Passwords WHERE id = ?", (changed_numb,))
            changed_value = cur.fetchone()
            print(changed_value)

            change = input("Which parameter you want to change: website, login, email, password, addInfo? Or ShowAll or just Quit? ").lower()

            if change == "quit" or change == "q":
                break
            else:
                new_value = input("How put it properly? ")
                if change == "website" or change == "w":
                    cur.execute('UPDATE Passwords SET website = ? WHERE id = ?', (new_value, changed_numb,))
                elif change == "login" or change == "l":
                    cur.execute('UPDATE Passwords SET login = ? WHERE id = ?', (new_value, changed_numb,))
                elif change == "email" or change == "e":
                    cur.execute('UPDATE Passwords SET email = ? WHERE id = ?', (new_value, changed_numb,))
                elif change == "password" or change == "p":
                    cur.execute('UPDATE Passwords SET password = ? WHERE id = ?', (new_value, changed_numb,))
                elif change == "addInfo" or change == "a":
                    cur.execute('UPDATE Passwords SET addInfo = ? WHERE id = ?', (new_value, changed_numb,))
                else:
                    print("You've enter wrong name of column. Please, try again")

            conn.commit()

            cur.execute("SELECT * FROM Passwords WHERE id = ?", (changed_numb,))
            changed_value = cur.fetchone()
            print(changed_value)

    #----------------------------Block of code to DELETE item from the table-------------------------
    elif command == "remove" or command == "r":
        showAll()
        while True:
            deleted_id = input("What id do you want to remove? You also can ShowAll or Quit? ").lower()
            if deleted_id == "quit" or deleted_id == "q":
                break
            elif deleted_id == "showall" or deleted_id == "s":
                showAll()
            else:
                    cur.execute("SELECT * FROM Passwords WHERE id = ?", (deleted_id,))
                    deleted = cur.fetchone()
                    if deleted == None:
                        print("Sorry, there is no such index")
                    else:
                        cur.execute("DELETE FROM Passwords WHERE id = ?", (deleted_id,))
                        conn.commit()
                        print("Line ", deleted, " was deleted")

conn.commit()
cur.close()