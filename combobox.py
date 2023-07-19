import tkinter as tk
from tkinter.ttk import Combobox


form = tk.Tk()
form.geometry("500x500")

x=tk.StringVar()
Python = ["Numpy", "Pandas", "Matplotlib","Seaborn", "Tkinter"]
kutu = Combobox(form, values=Python,height=3,textvariable=x).pack()

def yazdır():
    print(x.get())

buton = tk.Button(form, text="yazdır", command=yazdır).pack()

form.mainloop()
