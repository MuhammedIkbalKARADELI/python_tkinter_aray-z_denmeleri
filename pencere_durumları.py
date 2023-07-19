import tkinter as tk

form = tk.Tk()
form.geometry("500x500+350+250")
form.title("Ders4")

form.state("normal") # pencereyi istediğimiz boyuta ayarlayabiliriz
#form.state("zoomed") # tam ekran olark gelir penceree
#form.state("iconic")  # icon olarak açılır 

form.wm_attributes("-alpha",0.5) # Penceremizi %50 saydam yaptık
 

form .mainloop()