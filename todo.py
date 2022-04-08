import tkinter as tk
from tkinter import ttk
import sqlite3
import keyboard

class count:
    def __init__(self, n):
        self.count = n

countObj = count(0)


def displayTableNotes(canvas, canvas1):
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    command = "SELECT * FROM notes"
    table = cur.execute(command).fetchall()

    for i in table:
        addNote(i[0], canvas, canvas1)

def saveNote(content, canvas, inputLable, canvas1):
    canvas1.configure(scrollregion=canvas1.bbox("all"))
    inputLable.delete(0, 1000000)

    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = f"INSERT INTO notes VALUES('{content}')"
    cur.execute(command)
    conn.commit()

    conn.close()
    addNote(content, canvas, canvas1)

def addNote(text, box, canvas1):
    if text == "":
        return

    countObj.count += 1

    line = tk.Canvas(box)
    line.pack()

    tk.Label(line, text=text, width=65, anchor="w").grid(column=0, row=0)
    tk.Button(line, text="x", command=lambda m=line, f=text: delItem(m, f, canvas1)).grid(column=1, row=0)

def delItem(line, content, canvas1):
    canvas1.configure(scrollregion=canvas1.bbox("all"))
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

    toCanvas = tk.Canvas(canvas, height=100, width=500, highlightthickness=0, bg="#ffffff")
    toCanvas.place(rely=0, relx=0)

    topLabel = tk.Label(toCanvas, text="Todo:", font=("gotham black", 25), fg="#000000", bg="#ffffff")
    topLabel.place(rely=0.5, relx=0.4)

    # upper part
    table = tk.Canvas(canvas, bg="#ffffff", highlightthickness=0)
    table.place(relx=0.0, rely=0.2, anchor='nw', relheight=0.6, relwidth=1,)
    # create a main frame
    mainFrame = tk.Frame(table, bg="#ffffff")
    mainFrame.pack(fill='both', expand=1)
    # canvas
    canvas1 = tk.Canvas(mainFrame)
    canvas1.pack(side='left', fill='both', expand=1)
    # scrollbar
    canvScroll = ttk.Scrollbar(mainFrame, orient='vertical', command=canvas1.yview)
    canvScroll.pack(side='right', fill='y')
    # cofig canvas
    canvas1.configure(yscrollcommand=canvScroll.set)
    canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))
    # create another frame in canvas
    frameScroll = tk.Frame(canvas1)
    # add fram to window in canvas
    canvas1.create_window((0, 0), window=frameScroll, anchor="nw")


    #box = tk.Canvas(canvas, height=300, width=500, bg="#ffffff", highlightthickness=0)
    #box.place(rely=0.2, relx=0)

    # lower part
    addBox = tk.Canvas(canvas, height=100, width=500, bg="#e3e3e3", highlightthickness=0)
    addBox.place(rely=0.8, relx=0)

    description = tk.Entry(addBox, width=50)
    description.place(relx=0.05, rely=0.5)

    addButton = tk.Button(addBox, text="add", command=lambda: saveNote(description.get(), frameScroll, description, canvas1))
    addButton.place(relx=0.7, rely=0.5)

    displayTableNotes(frameScroll, canvas1)

    keyboard.on_press_key("enter", lambda _: saveNote(description.get(), frameScroll, description, canvas1))

    root.mainloop()


if __name__ == '__main__':
    main()


"""
to do:
    -fix scroll bar last item missing
    
raw to do app
Bastian Lipka
"""