import sqlite3 as sqlite


def add_newbook():
    name = input("Enter the name of the book you want to enter : ")
    author = input("Enter the name of the book author : ")
    connect = sqlite.connect("Data.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Books(name text primary key,author text,read number)")
    cursor.execute(f'INSERT INTO Books VALUES(?,?,0)', (name, author))
    connect.commit()
    connect.close()


def list_books():
    connect = sqlite.connect("Data.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Books")
    books = [{'name': line[0], 'author': line[1], 'read': line[2]} for line in cursor.fetchall()]
    connect.commit()
    connect.close()
    return books

def mark_read():
    name = input("Enter the name of the book you want to mark as read : ")
    connect = sqlite.connect("Data.db")
    cursor = connect.cursor()
    cursor.execute(f'UPDATE Books SET read=1 WHERE name=?', (name,))
    connect.commit()
    connect.close()

def del_book():
    name = input("Enter the name of the book you want to delete : ")
    connect = sqlite.connect("Data.db")
    cursor = connect.cursor()
    cursor.execute(f'DELETE FROM Books WHERE name=?', (name,))
    connect.commit()
    connect.close()

