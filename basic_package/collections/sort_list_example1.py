

def retournerOrderedValue(list_a):
    list_new=sorted(list_a)
    print(f"values the list est {list_new}")

def retournerOrderedValueReverse(list_a):
    list_new=sorted(list_a,reverse=True)
    print(f"values the list est {list_new}")


def Main():
    list1= [1,5,8,9,10,27 ,7,25]
    retournerOrderedValue(list1)
    retournerOrderedValueReverse(list1)
if __name__ == "__main__":
    Main()