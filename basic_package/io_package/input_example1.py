

def Main():
    #variables
    validator = False
    age = None
    nom = None

    print ("ajouter votre nom")
    nom= input()
    print(f"bonjour {nom}")


    while not validator:
        print("ajouter votre age")
        try:
            age= int(input())
            validator = True
        except ValueError:
            print(f"error a priori ce n'est pas une {age}")

    print ("merci votre age est {validator}")
if __name__ ==  "__main__":
    Main()