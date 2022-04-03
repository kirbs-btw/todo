import tkinter as tk

class count:
    def __init__(self, n):
        self.count = n

class ram:
    def __init__(self):
        self.notes = []

countObj = count(0)
ramObj = ram()

def addNote(text, box):
    countObj.count += 1
    ramObj.notes.append(text)
    print(ramObj.notes)

    tk.Label(box, text=text, anchor="w").grid(row=countObj.count)


def main():
    root = tk.Tk()
    root.title("Notes")

    canvas = tk.Canvas(root, height=500, width=500, highlightthickness=0)
    canvas.pack()

    # upper part
    box = tk.Canvas(canvas, height=400, width=500, bg="#bbff00", highlightthickness=0)
    box.place(rely=0, relx=0)

    # lower part
    addBox = tk.Canvas(canvas, height=100, width=500, bg="#00ffbb", highlightthickness=0)
    addBox.place(rely=0.8, relx=0)

    description = tk.Entry(addBox, width=50)
    description.place(relx=0.05, rely=0.5)

    addButton = tk.Button(addBox, text="add", command=lambda: addNote(description.get(), box))
    addButton.place(relx=0.7, rely=0.5)

    root.mainloop()


    pass

if __name__ == '__main__':
    main()


"""
to do:
    -colors
    -scroll bar

raw to do app


Bastian Lipka
"""