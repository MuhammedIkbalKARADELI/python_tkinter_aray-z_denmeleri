import tkinter as tk

form = tk.Tk()
form.title("Place")  # pencerenin konumunu belirler
form.geometry("500x450+250+250")
buton = tk.Button(text="Deneme", fg="red", bg="green", font="Times 17 bold")
#buton.place(x="50",y="40") # pencere içindeki button yazısının konumunu bize verir
buton.place(relx=0.5,rely=0.5) # pencerede belirlediğimiz konumdaki ornda kalır ve pencere boyut değiştirildiğinde de bu oran korunur.
buton.place(relx=0.5,rely=0.5,width=160,height=100)

form.mainloop()