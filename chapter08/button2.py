from tkinter import *

root = Tk()
root.geometry("300x200")

button = Button(
    text="This is a button!",
    width=30,
    height=10,
    bg="blue",
    fg="yellow",
)

button.pack()
root.mainloop()
