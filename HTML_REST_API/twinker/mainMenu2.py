

# coding: utf-8
from tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

# entrée
value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

print("value is ",entree)
fenetre.mainloop()