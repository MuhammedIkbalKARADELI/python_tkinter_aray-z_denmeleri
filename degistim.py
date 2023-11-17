import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulama Hoş Geldiniz!")

def butonFonksiyonu():
    # print("Butona tıkladın...")

    etiket.config(
        text="Değiştim",
        bg="red",
        font="Verdana"
    )

buton = tk.Button(
    pencere,
    text="Ben Bir Butonum",
    bg="orange",
    fg="black",
    activebackground="red",
    activeforeground="white",
    font=24,
    height=5,
    width=20,
    cursor="hand2",
    command= butonFonksiyonu
)

buton.pack()

etiket = tk.Label(
    pencere,
    text="Ben Bir Etiketim",
    font="Tahoma 24",
    bg="blue",
    fg="white",
    wraplength=150
)

etiket.pack(pady=10)

giris = tk.Entry(
    pencere,
    width=50
)

giris.insert(
    string="Kafanıza göre bir şeyler yazın...",
    index=0
)

giris.pack()

pencere.mainloop()