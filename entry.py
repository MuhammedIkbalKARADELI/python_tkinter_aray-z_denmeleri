import tkinter as tk
form = tk.Tk()



form.title("Ders -6")
form.geometry("500x450+250+250")

giris = tk.Entry(form,fg="black",bg="red")
giris.pack(side=tk.RIGHT)

giris2 = tk.Entry(form,fg="black",bg="blue")
giris2.pack(side=tk.LEFT)

form.mainloop()
