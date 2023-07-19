import tkinter as tk
import time

form = tk.Tk()
form.geometry("250x200+500+250")
form.title("Uygulama")
form.config(bg="yellow")


def zaman():
    zaman_fromat = time.strftime("%H:%M:%S")
    zaman_label.config(text=zaman_fromat)
    zaman_label.after(20,zaman)  # zaman her seferinde tekrardan çağrılıyor ki zamnımız güncellensin
 


zaman_label = tk.Label(bg="white",font="Times 35 bold")
zaman_label.place(x=30,y=80)
zaman()

basik = tk.Label(text="Digital saat uygulaması", font="Times 15 bold",bg = "yellow").pack()
basik = tk.Label(text="Tkinter Dersleri 21", font="Times 15 bold", bg="yellow").pack(side=tk.BOTTOM)


form.mainloop()

