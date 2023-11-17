import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulama Hoş Geldiniz!")

def butonFonksiyonu():
    print("Butona tıkladın...")

buton = tk.Button(
    pencere,
    text="Ben Bir Butonum",
    bg="orange",
    fg="black",
    activebackground="red",
    activeforeground="white",
    font=30,
    height=5,
    width=20,
    cursor="hand2",
    command= butonFonksiyonu
)


etiket = tk.Label(
    pencere,
    text="Ben Bir Etiketim",
    font="Tahoma 18",
    bg="black",
    fg="white",
    wraplength=300
)

buton.pack()
etiket.pack()


etiket.pack(pady=10) # Label'ı biraz aşağıya alalım.

pencere.mainloop()