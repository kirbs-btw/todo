import sqlite3

def main():
    #f = open("db.sql", "w+")
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    command = "CREATE TABLE notes(note TEXT)"
    cur.execute(command)
    conn.commit()

if __name__ == '__main__':
    main()