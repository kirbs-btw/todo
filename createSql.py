import sqlite3

def main():
    #f = open("db.sql", "w+")
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    command = "CREATE TABLE notes(note TEXT)"
    cur.execute(command)
    conn.commit()

def printSQL():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    command = "SELECT * FROM notes"
    table = cur.execute(command).fetchall()

    for i in table:
        print(i[0])

def clearSQL():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    command = "DELETE FROM notes"
    cur.execute(command)
    conn.commit()


if __name__ == '__main__':
    clearSQL()
    printSQL()