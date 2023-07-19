from tabnanny import check
import tkinter as tk

form = tk.Tk()
form.title("Checkbutton")
form.geometry("500x500")


x = tk.IntVar()
x.set(0)

def kontrol():
    if x.get() == 0:
        print("Onaylanmadı")
    else:
        print("Onaylandı")



check = tk.Checkbutton(form, text="onay", fg="pink",bg="blue",variable=x,command=kontrol)
check.pack()

form.mainloop()