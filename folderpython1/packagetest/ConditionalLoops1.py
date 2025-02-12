#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys

a=0
b=0

c=("sit0","sit1","sit2")
#BOUCLE WHILE
while a < 10 :
    print("comptage actuel vaut",a)
    if a >= 4 and a <=8 :
        print("comptage vaut plus ou égal à 4")
        
    elif a > 8:
        print("comptage vaut plus de 9")
        break
    else:
        print("faire rien")
    a+=1
print("fin du script,la variable a vaut=",a)

     
# BOUCLE FOR
print("le tuple1 vaut",c[0])
for i in c :
    print("la variable du tuple vaut =",i)
print ("fin du boucle for")

