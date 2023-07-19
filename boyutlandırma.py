from cProfile import label
import tkinter as tk

form = tk.Tk()
form.title("Tkinter Dersleri ders-3")

form.geometry("500x250+500+350") # Peencerenin boyutunu belirledik ve ekranda x= 500, y=350 kordinatlarında olacak şekilde verdik.
form.minsize(450,400) 
form.maxsize(550,550)

label = tk.Label(form,text="Ders-3")
label.pack()

form.mainloop()


form2 = tk.Tk()
form2.title("Tkinter Dersleri ders-3")
form2.geometry("500x250+0+0")
form2.resizable(False,False) # Boyut değiştilemez yaptık.
form2.mainloop()
