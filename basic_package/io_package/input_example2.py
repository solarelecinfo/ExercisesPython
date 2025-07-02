

def Main():
    validator = True
    while validator:
        print ("Ajouter une liste de 3 chiffres uniquement")
        var_string = input()
        print (f"vous avez écrit = {var_string}")
        list_by_space=var_string.split()
        if (len(list_by_space) != 3 ):
            print("vous avez pas mis le nombre de chiffres demandés")
        else:
            validator = False

    #Creation d'un map object
    map_object= map(int,list_by_space)
    a,b,c =map_object
    #depackaging d'objet map
    print(f"value={a} , value={b} et value={c}")

    #conversion en list( obligation de recréer l'objet map car il a été consommée auparavant"
    map_object2 = map(int, list_by_space)
    list_integers=list(map_object2)
    for i in list_integers:
        print(f"value is ={i}")

if __name__ ==  "__main__":
    Main()