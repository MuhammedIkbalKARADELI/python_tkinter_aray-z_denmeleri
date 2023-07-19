import tkinter as tk

form = tk.Tk()
form.title("TKinter Dersleri-1")
etiket = tk.Label(text = "Tkinter Python")
etiket.pack() # Yazdığımız yazıların kalmasaını sağlıyor.
etiket2 = tk.Label(form,text="Python TkinterDersleri")
etiket2.pack()
form.mainloop() # pencerimizin kalmasını sağlıyor.

