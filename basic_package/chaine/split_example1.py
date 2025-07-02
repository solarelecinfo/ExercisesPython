

def Main():
    #variables
    validator = False
    age = None
    nom = None

    print ("ajouter votre nom")
    nom= input()
    print(f"bonjour {nom}")
    list_nom=nom.split()

    print (f"merci votre nom est {list_nom}")
#this is a comment

    list_lettre= list(nom)
    print(f"merci votre nom est {list_lettre}")
if __name__ ==  "__main__":
    Main()