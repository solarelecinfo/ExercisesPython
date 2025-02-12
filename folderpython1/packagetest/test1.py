#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys, getopt

from _curses import version

#username=input("Veuillez ecrire votre nom")

#print("bonjour ",username)

def main(argv):
    print ("configuration info ",sys.version)

    param_a=''
    param_b=''
    try:
        opts, args =getopt.getopt(argv,"a:b:")
    except getopt.GetoptError:
        print("error")
    
    for option,argument in opts:
        if option == '-a':
            param_a=argument
        elif option =='-b':
            param_b=argument
        else:
            print("no option choisi")
    
    print ("les options choisis sont=",param_a,"et",param_b)
if __name__=="__main__":
    main(sys.argv[1:])