
# ------utilisation de map--------------

def multiplicateur_double(a,b):
    result = a*b
    return result
def multiplicateur_simple(a):
    result = 2*a
    return result

def Main():
    print("******utilisation map directe*******")
    a = [1,10,100,1000]
    list(map(print,a))
    for element in a:
        print("value="+str(element))

    print("******fonction avec 1 argument via map*******")
    numbers = [1,2,3,4,5,6]
    list_result = map(multiplicateur_simple,numbers)
    for i in list_result:
        print ("result is "+str(i))
    map(print,numbers)

    print("******fonction avec 2 argument via map*******")
    numbers_list_a = (1,2,3,4,5,6)
    numbers_list_b = (1,2,3,4,5,6)
    list_result2 = map(multiplicateur_double,numbers_list_a,numbers_list_b)

    for i in list_result2:
        print("result multiplication est :"+str(i))

if __name__ == "__main__":
    Main()