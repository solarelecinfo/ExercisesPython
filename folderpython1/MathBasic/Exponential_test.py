def Main():
    a=10e-3
    b=0.01
    c=a-b
    print("a="+str(a)+" b="+str(b))
    print("result is "+str(c))

    a=10e3
    b=10000
    c=a-b
    print("a="+str(a)+" b="+str(b))
    print("result is "+str(c))


if __name__ == "__main__":
    Main()