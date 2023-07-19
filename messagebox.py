import tkinter as tk
from tkinter import messagebox

form = tk.Tk()
form.geometry("500x500")
form.title("Messagebox")

def mesaj():
    messagebox.showinfo(title="Mesage1", message="Lütfen Mesaja Rivayet Edin!")
    messagebox.askretrycancel(title="Mesage2", message="Lütfen et artık!!")
    messagebox.askyesno(title="Mesage3", message="Artık yeter da!!!")
    messagebox.askquestion(title="Mesage4", message="Tkinter mesagebox sonuna geldik.")



buton = tk.Button(form, text="tıkla measj gelsin", command=mesaj).pack()






form.mainloop()
