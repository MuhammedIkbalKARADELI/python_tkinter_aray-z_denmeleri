from cProfile import label
import tkinter as tk

form = tk.Tk()
form.title("Uygulama")
form.geometry("500x300")

mail = tk.Label(text="Mail: ", fg="black", bg="blue", font="Times 10 bold")
mail.place(x=10, y=30)

sifre = tk.Label(text="Sifre: ", fg="black", bg="blue", font="Times 10 bold")
sifre.place(x=10, y=60)

mail_enter = tk.Entry()
mail_enter.place(x=50, y=30)

sifr_enter = tk.Entry(show="*")
sifr_enter.place(x=50, y=62)

def kayıtol():
    mail = tk.Label(text="Mail:", fg="black", bg="blue", font="Times 10 bold")
    mail.place(x=10, y=150)
    sifre = tk.Label(text="Sifre:", fg="black", bg="blue", font="Times 10 bold")
    sifre.place(x=10, y=180)
    ad = tk.Label(text="Ad:",fg="black", bg="blue", font="Times 10 bold")
    ad.place(x=10,y=120)

    mail_enter = tk.Entry()
    mail_enter.place(x=50, y=150)

    sifr_enter = tk.Entry(show="*")
    sifr_enter.place(x=50, y=180)

    ad_enter = tk.Entry()
    ad_enter.place(x=50, y=120)

def giris():
    mail_enter.delete(0,"end")
    sifr_enter.delete(0,"end")


kayıt_buton = tk.Button(form, text="Kayıt ol", fg="black", bg="green", command=kayıtol)
kayıt_buton.place(x=45, y=90)

giris_buton = tk.Button(form, text="Giris yap", fg="black", bg="green", command=giris)
giris_buton.place(x=120, y=90)




form.mainloop()