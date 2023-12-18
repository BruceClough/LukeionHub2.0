import sqlite3

#Database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except:
        print("Error")
    return conn

#Create table
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except:
        print("Error")

#Menu Interface
def show_menu():
    print("\nMenu: ")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Update Note")
    print("5. Add Book")
    print("6. View Books")
    print("7. Delete Book")
    print("8. Update Book")
    print("9. Exit")

#Note opeations
def add_note(conn):
    print("Add a new note: ")
    title = input("Enter the title: ")
    content = input("Enter the content: ")
    sql = '''INSERT INTO notes(title, content) VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, (title, content))
    conn.commit()

def view_notes(conn):
    print("\nNotes: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_note_by_id(conn, id):
    id = input("Enter the id of the note you want to delete: ")
    sql = 'DELETE FROM notes WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def update_note_by_id(conn, id):
    id = input("Enter the id of the note you want to update: ")
    title = input("Enter the new title: ")
    content = input("Enter the new content: ")
    sql = '''UPDATE notes SET title=?, content=? WHERE id=?'''
    cur = conn.cursor()
    cur.execute(sql, (title, content, id))
    conn.commit()

#Book operations
def add_book(conn):
    print("Add a new book: ")
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    category = input("Enter the category: ")
    sql = '''INSERT INTO books(title, author, category) VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, (title, author, category))
    conn.commit()

def view_books(conn):
    print("\nBooks: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_book_by_id(conn, id):
    id = input("Enter the id of the book you want to delete: ")
    sql = 'DELETE FROM books WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def update_book_by_id(conn, id):
    id = input("Enter the id of the book you want to update: ")
    title = input("Enter the new title: ")
    author = input("Enter the new author: ")
    category = input("Enter the new category: ")
    sql = '''UPDATE books SET title=?, author=?, category=? WHERE id=?'''
    cur = conn.cursor()
    cur.execute(sql, (title, author, category, id))
    conn.commit()

#Main function
def main():
    database = "lukeionhub2.db"

    sql_create_notes_table = """ CREATE TABLE IF NOT EXISTS notes (id integer PRIMARY KEY, title text NOT NULL, content text NOT NULL); """
    sql_create_books_table = """ CREATE TABLE IF NOT EXISTS books (id integer PRIMARY KEY, title text NOT NULL, author text NOT NULL, category text NOT NULL); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_notes_table)
        create_table(conn, sql_create_books_table)
    else:
        print("Error")

    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_note(conn)
        elif choice == "2":
            view_notes(conn)
        elif choice == "3":
            delete_note_by_id(conn,id)
        elif choice == "4":
            update_note_by_id(conn,id)
        elif choice == "5":
            add_book(conn)
        elif choice == "6":
            view_books(conn)
        elif choice == "7":
            delete_book_by_id(conn,id)
        elif choice == "8":
            update_book_by_id(conn,id)
        elif choice == "9":
            conn.close()
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()    
