# Homework 13: Python DB connection
# Author: Jongwook Woo
# Date: 04/09/2017

import sqlite3

try:
    # Create a database in RAM
    # db = sqlite3.connect(':memory:')
    
    # Creates or opens a file called mydb.db with a SQLite3 DB
    db = sqlite3.connect('mydb.db')
    # Get a cursor object
    cursor = db.cursor()
    # Check if table users does not exist and create it
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                      users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''')
    # Commit the change
    db.commit()    
    # user 1 
    name1 = 'Andres'
    phone1 = '3366858'
    email1 = 'user@example.com'
    password1 = '12345'
 
    # user 2 
    name2 = 'John'
    phone2 = '5557241'
    email2 = 'johndoe@example.com'
    password2 = 'abcdef'

    # user 3
    name3 = 'George'
    phone3 = '5555555'
    email3 = 'gsturrock@smu.edu'
    password3 = 'pw1234'
 
    # Insert user 1
    cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
    print('First user inserted')
 
    # Insert user 2
    cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name2,phone2, email2, password2))
    print('Second user inserted')
    
    # TODO: create the third user with your name, phone, email, password (any password is fine)
    # Insert user 3
    cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name3,phone3,email3,password3))
    print('Third user inserted')    
    
    db.commit()
    
    
    # TODO: Fill in SQL statement to select name, email, phone from user
    cursor.execute('''SELECT name, email, phone from users''')
    
    user1 = cursor.fetchone() #retrieve the first row
    print(user1[0]) #Print the first column retrieved(user's name)

    #retrieve all rows
    all_rows = cursor.fetchall()
    for row in all_rows:
        # row[0] returns the first column in the query (name), 
        # row[1] returns phone column.
        # row[2] returns email column.
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
    
    
    # To retrive data with conditions, use again the "?" placeholder:
    user_id = 3
    cursor.execute('''SELECT name, email, phone FROM users WHERE id=?''', (user_id,))
    user = cursor.fetchone()
    print(user1) #Print the all columns of the first row 
    
    # TODO: Fill in SQL statement using UPDATE users for phone WHERE id is user_id using "?" placeholder
    newphone = '3432916'
    #cursor.execute('''[Fill In]''', (newphone, user_id))
    cursor.execute('''UPDATE users SET phone=? where id=?''', (newphone, user_id))
    db.commit() #Commit the change
    
    # TODO: The row factory class sqlite3.Row is used to access the columns of a query by name instead of by index:
    #   Fill in the SQL statement to INSERT INTO users for the columnes name, phone, email, password using
    #    "?" placeholders for the following user 1
    # user 1 
    name1 = 'JW'
    phone1 = '3433000'
    email1 = 'jwoo@smu.edu'
    password1 = '123456'
    
    with db:
            db.execute('''INSERT INTO users (name, phone, email, password) VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
            
    cursor.execute('''SELECT * FROM users''')
    all_rows = cursor.fetchall()
    # TODO: print all columns of all_rows using for loop shown above
    for row in all_rows:
        print(row) 
            
# Catch the exception
except sqlite3.IntegrityError:
    print('Record already exists')
except Exception as e:
    # Roll back any change if something goes wrong
    db.rollback()
    raise e
finally:
    # Close the db connection
    db.close()
