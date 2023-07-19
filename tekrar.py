from cgi import test
import tkinter as tk
import random as rd

form = tk.Tk()
form.title("Tekrarr Uygulaması")
form.geometry("500x400+500+350")
liste = []

for i in range(5):
    while len(liste)!=6:
        a = rd.randint(1,50)
        if a not in liste:
            liste.append(a)

def goster():
    label.config(text=liste, bg="green")

def saydamlastır():
    form.wm_attributes("-alpha",0.3)
    label.config(text="saydamlaştırdın", fg="black",bg="white")

def dondur():
    form.wm_attributes("-alpha",0.9)
    label.config(text="döndür", fg="black",bg="white")

def maxYap():
    form.state("zoomed")
    label.config(text="Max yaptın", fg="black",bg="white")

def minYap():
    form.state("iconic")
    label.config(text="Min yaptın", fg="black",bg="white")

def normalSize():
    form.state("normal")
    form.geometry("500x400+500+350")
    label.config(text="Normale döndürdün", fg="black",bg="white")
    form.wm_attributes("-alpha",1)

label = tk.Label(form,fg="red",bg="red")
label.pack()

goster = tk.Button(form,text="göster",fg="black",bg="yellow",command=goster)
goster.pack()

goster2 = tk.Button(form,text="saydamlaştır",fg="black",bg="yellow",command=saydamlastır)
goster2.pack()

goster3 = tk.Button(form,text="döndr",fg="black",bg="yellow",command=dondur)
goster3.pack()

goster4 = tk.Button(form,text="maxYap",fg="black",bg="yellow",command=maxYap)
goster4.pack()

goster5 = tk.Button(form,text="minYap",fg="black",bg="yellow",command=minYap)
goster5.pack()

goster6 = tk.Button(form, text="normal size", fg="black",bg="yellow",command=normalSize)
goster6.pack()


form.mainloop()