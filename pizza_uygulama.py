from re import T
import tkinter as tk

form = tk.Tk()
form.geometry("500x500+400+100")
form.title("Pizza Sipariş Programı")

baslik = tk.Label(text="Pizza sipariş programna Hoşgeldiniz",fg="black", font="Times 17 bold").pack()


entr = tk.StringVar()
entr1 = tk.StringVar()



lbl_ad = tk.Label(form,text="Ad Soyad:", bg="pink", font="Times 12 italic").place(x=10,y=40)
lbl_boyut = tk.Label(form,text="Boyut:", bg="pink", font="Times 12 italic").place(x=10,y=70)
lbl_icindekiler = tk.Label(form,text="İçindekiler:", bg="pink", font="Times 12 italic").place(x=10,y=100)
lbl_adres = tk.Label(form,text="Adres:", bg="pink", font="Times 12 italic").place(x=10, y=130)

entry_ad = tk.Entry(textvariable=entr).place(x=100,y=40)
entry_adress = tk.Entry(textvariable=entr1).place(x=100,y=130)

boyut = tk.StringVar()

rad_button_kucuk = tk.Radiobutton(form, text="Küçük Boy", activebackground="green", value="Küçük Boy", variable=boyut).place(x=100,y=70)
rad_button_orta = tk.Radiobutton(form, text="Orta Boy", activebackground="green", value="Orta Boy",variable=boyut).place(x=160,y=70)
rad_button_buyuk = tk.Radiobutton(form, text="Büyük Boy", activebackground="green", value="Büyük Boy", variable=boyut).place(x=240,y=70)

deger1 = tk.StringVar()
deger2 = tk.StringVar()
deger3 = tk.StringVar()

Check1 = tk.Checkbutton(form, text="Sucuklu", variable=deger1, onvalue="Sucuklu").place(x=100,y=100)
Check2 = tk.Checkbutton(form, text="Zeytinli", variable=deger2, onvalue="Zeytinli").place(x=170,y=100)
Check3 = tk.Checkbutton(form, text="Acı Soslu", variable=deger3, onvalue="Acı soslu").place(x=240,y=100)


def siparis_ver():
    
    label_bilgi = tk.Label(form,text="Sipriş bilgileri", fg="black", font="Times 15 bold").place(x=80,y=240)

    lbl_ad = tk.Label(form,text="Ad Soyad:", bg="pink", font="Times 12 italic").place(x=10,y=270)
    lbl_boyut = tk.Label(form,text="Boyut:", bg="pink", font="Times 12 italic").place(x=10,y=300)
    lbl_icindekiler = tk.Label(form,text="İçindekiler:", bg="pink", font="Times 12 italic").place(x=10,y=330)
    lbl_adres = tk.Label(form,text="Adres:", bg="pink", font="Times 12 italic").place(x=10, y=360)

    lbl_ad1 = tk.Label(form,text=entr.get(), font="Times 12 italic").place(x=120,y=270)
    lbl_boyut1 = tk.Label(form,text=boyut.get(), font="Times 12 italic").place(x=120,y=300)
    lbl_icindekiler1 = tk.Label(form,text=deger1.get()+" "+deger2.get()+" "+deger3.get(), font="Times 12 italic").place(x=120,y=330)
    lbl_adres1 = tk.Label(form,text=entr1.get(), font="Times 12 italic").place(x=120, y=360)



def iptal_et():
    form.quit()

siparis = tk.Button(form, text="Siparis Ver", activebackground="green", command=siparis_ver).place(x=150,y=160)
iptal = tk.Button(form, text="Siparis iptal", activebackground="red", command=iptal_et).place(x=150,y=190)


# sipariş bilgileri



form.mainloop()




