"""
side - left-right-top-bottom
fill - x - y
expand 0 - 1
anchor=>  'n' yukarı 's' aşağı 'e' sağ 'w' sol
'ne' yukarı sağ 'nw' yukarı sol 'se' aşağı sağ 'sw' aşağı sol 
'center' orta
"""

import tkinter as tk

form = tk.Tk()
form.geometry("500x500")

label = tk.Label(form,text="Geometrik yöneticiler")
label.pack(side=tk.TOP)

buton = tk.Button(text="Pack()", bg="red")
#buton.pack( fill=tk.Y)
#buton.pack( fill=tk.X)
#buton.pack(side=tk.BOTTOM, fill=tk.X)
#buton.pack(side=tk.LEFT, fill=tk.Y)
#buton.pack(side=tk.LEFT, fill=tk.Y, expand=tk.YES)

#sbuton.pack(expand=1,anchor="se")
#buton.pack(expand=1,anchor="sw")
buton.pack(expand=1,anchor="nw",padx=200,pady=125) # padx=200,pady=125 penceredeki butonun x y kordinatları 


form.mainloop()

