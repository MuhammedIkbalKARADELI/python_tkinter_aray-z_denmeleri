import tkinter as tk

form = tk.Tk()
form.title("Entry")
form.geometry("500x300")

entry = tk.Entry()
entry.pack()
entry2 = tk.Entry(show="*")
entry2.pack()


etiket = tk.Label(text="Verileri burada getirilimasi lazım")


def al():
    etiket["text"] = entry.get()

def sil():
    entry.delete(0,"end")
    entry2.delete(0,"end")


button = tk.Button(text="verileri al", fg="red",bg="green", command=al)
button.pack()
button2 = tk.Button(text="sil",fg="red",bg="green",command=sil)
button2.pack()


etiket = tk.Label(text="Verileri burada getirilimasi lazım")
etiket.pack()


form.mainloop()

