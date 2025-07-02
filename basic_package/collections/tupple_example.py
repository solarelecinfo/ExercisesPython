


def test_tuple(a):
    if (isinstance(a,tuple)):
        print ("tuple trouvé contenu est "+str(a))
    else:
        print("l'element n'est pas un tuple" + str(type(a)))

def test_tuple_iteration(a):
    
    for element in a :
        print("element of tuple vaut=="+str(element))


def Main():
    test_tuple(5)
    test_tuple([5,4,3])
    test_tuple((5,4,3))
    print("=============================================")
    tuple1=(1,2,3,4,5,6)
    test_tuple_iteration(tuple1)

if __name__ == "__main__":
    Main()

