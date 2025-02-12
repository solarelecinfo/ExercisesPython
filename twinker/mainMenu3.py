import tkinter as tk

def afficher_texte():
    # Récupère le texte de la boîte de saisie et l'affiche dans la console
    texte = entree.get()
    print(f"Vous avez écrit : {texte}")

# Crée la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Exemple d'interface simple")

# Crée une boîte de saisie (entry)
entree = tk.Entry(fenetre, width=40)
entree.pack(padx=10, pady=10)

# Crée un bouton qui appelle la fonction afficher_texte lors de l'appui
bouton = tk.Button(fenetre, text="Afficher", command=afficher_texte)
bouton.pack(padx=10, pady=10)

# Lance la boucle principale de l'interface
fenetre.mainloop()