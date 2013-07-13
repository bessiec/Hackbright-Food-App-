import sqlite3

DB = None
CONN = None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def login(email, password):
    query = """SELECT email, password FROM Users WHERE email = ? AND password = ?"""
    DB.execute(query, (email.strip(), password.strip()))
    row = DB.fetchone()
    print row
    # if row == (email, password):
    #     return True
    # else:
    #     return False


def get_all_posts():
    query="""SELECT title FROM Posts;"""
    DB.execute(query,)
    rows = DB.fetchall()
    print rows

def search_title(title):
    query = """SELECT title, body, value FROM Posts JOIN Votes ON (Votes.user_id=Posts.user_id) WHERE title = ?"""
    DB.execute(query, (title.strip(),))
    row = DB.fetchone()
    # return rows
    print row

def main():
    connect_to_db()
    command = None
    while command != 'quit':
        input_string = raw_input('Food Database> ')
        tokens = input_string.split(",")
        command = tokens[0]
        args = tokens[1:]

        if command == 'login':
            login(*args)  
        # elif command == 'get_all_posts':
        #     get_all_posts()       

    CONN.close()

if __name__ == '__main__':
    main()  