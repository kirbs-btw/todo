import tkinter as tk

def addNote(text, box):

    tk.Label(box, text=text).pack()
    pass

def main():
    root = tk.Tk()

    canvas = tk.Canvas(root, height=500, width=500, highlightthickness=0)
    canvas.pack()

    # upper part
    box = tk.Canvas(canvas, height=400, width=500, bg="#bbff00", highlightthickness=0)
    box.place(rely=0, relx=0)

    # lower part
    addBox = tk.Canvas(canvas, height=100, width=500, bg="#00ffbb", highlightthickness=0)
    addBox.place(rely=0.8, relx=0)

    description = tk.Entry(addBox)
    description.place(relx=0.5, rely=0.2)

    addButton = tk.Button(addBox, command = lambda: addNote(description.get(), box))
    addButton.place(relx=0.5, rely=0.5)

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