import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Ambriel Health")


def butonFonksiyonu():
    # print("Butona tıkladın...")

    etiket.config(
        text="Ambriel Health",
        bg="Red",
        fg="white",
        font="Verdana"
    )

    etiket_giris.config(
        text="Verdiğiniz bilgiler için teşekkür ederiz. ",
        bg="Gray",
        fg="white",
        font="Verdana"
    )


buton = tk.Button(
    pencere,
    text="Buna bastığında bambaşka bir dünyaya geçiceksin",
    bg="Blue",
    fg="Black",
    activebackground="Red",
    activeforeground="white",
    font=24,
    height=5,
    width=35,
    cursor="hand2",
    command= butonFonksiyonu
)


etiket = tk.Label(
    pencere,
    text="Sağlık Için Bir Şirket",
    font="Tahoma 18",
    bg="Gray",
    fg="white",
    wraplength=150
)


etiket_giris = tk.Label(
    pencere,
    text="Bu şirket için sizde ilk izlenim nasıl oldu?",
    font="Tahoma 18",
    bg="Gray",
    fg="white",
    wraplength=150
)


giris = tk.Entry(
    pencere,
    width=50
)

giris.insert(
    string="Buraya yazınız:   ",
    index=0
)



buton.pack()
etiket.pack(pady=10)
etiket_giris.pack(pady=10)
giris.pack()


pencere.mainloop()