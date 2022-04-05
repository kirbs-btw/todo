import tkinter as tk
import sqlite3

class count:
    def __init__(self, n):
        self.count = n

countObj = count(0)


def displayTableNotes(canvas):
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    command = "SELECT * FROM notes"
    table = cur.execute(command).fetchall()

    for i in table:
        addNote(i[0], canvas)

def saveNote(content, canvas):
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = f"INSERT INTO notes VALUES('{content}')"
    cur.execute(command)
    conn.commit()

    conn.close()
    addNote(content, canvas)

def addNote(text, box):
    countObj.count += 1

    line = tk.Canvas(box, width=500)
    line.grid(row=countObj.count)

    tk.Label(line, text=text).grid(row=1)
    tk.Button(line, text="hi", command = lambda m=line, f=text: delItem(m, f)).grid(row=2)

def delItem(line, content):
    line.destroy()
    delSQLItem(content)

def delSQLItem(content):
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    command = f"DELETE FROM notes WHERE note LIKE '{content}'"
    cur.execute(command)
    conn.commit()

def main():
    root = tk.Tk()
    root.title("Notes")

    canvas = tk.Canvas(root, height=500, width=500, highlightthickness=0)
    canvas.pack()

    # upper part
    box = tk.Canvas(canvas, height=400, width=500, bg="#ffffff", highlightthickness=0)
    box.place(rely=0, relx=0)

    # lower part
    addBox = tk.Canvas(canvas, height=100, width=500, bg="#e3e3e3", highlightthickness=0)
    addBox.place(rely=0.8, relx=0)

    description = tk.Entry(addBox, width=50)
    description.place(relx=0.05, rely=0.5)

    addButton = tk.Button(addBox, text="add", command=lambda: saveNote(description.get(), box))
    addButton.place(relx=0.7, rely=0.5)

    displayTableNotes(box)

    root.mainloop()


if __name__ == '__main__':
    main()


"""
to do:
    -scroll bar
    
raw to do app


Bastian Lipka
"""