from distutils.command.config import config
from this import d
import tkinter as tk

form = tk.Tk()
form.geometry("400x400")
form.title("spinbox")
form.config(bg="pink")

x = tk.IntVar()
y = tk.IntVar()

spin = tk.Spinbox(form, from_=10, to=100, textvariable=x).pack()
spin2 = tk.Spinbox(form, from_=10, to=20, textvariable=y).pack()


def verial():
    print("x: " + str(x.get()))
    print("y: " + str(y.get()))

buton = tk.Button(form, text="verial", command=verial).pack()



form.mainloop()