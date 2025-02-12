#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys

def checkType(objet1):
    print("le type d'objet est ",type(objet1),"et la valeur est=",objet1)


#LIST=> ordonée , indexée
a=[",tomate","salade","mirabelle","pommedeterre"]
b=["janvier","fevrier","mars","avril"]
b2=b
b3=list(b)
extra=["mai","juin","juillet"]
#-----------------------------------------TUPLE: collection ordonée, unchangeable
c=("une","deux","trois","quatre")

tuple1=("hola1",45,"hola5")
tuple11=(*tuple1,)
#tuple2=("hola1",45,"hola5","extra")

#RELATION ENTRE ARGUMETS MULTIPLES *ARGS  ET TUPLE
print("le type de variable tuple1 est =",type(tuple1),"avec taille(len)=",len(tuple1))
print("le type de variable (*tuple1,) est =",type((*tuple1,)),"avec taille(len)=",len((*tuple1,)))
print("le type de variable *tuple11=(*tuple1,) est =",type(tuple11),"avec taille(len)=",len(tuple11))
for i in tuple1:    print(i)
#concatenation
tuple2=("valeur2-deux",)
tuple3=tuple1+tuple2
tuple33=(*tuple3,)

print("le type de variable tuple3 est =",type(tuple3),"avec taille(len)=",len(tuple3))
print("le type de variable (*tuple3,) est =",type((*tuple3,)),"avec taille(len)=",len((*tuple3,)))
print("le type de variable *tuple11=(*tuple3,) est =",type(tuple33),"avec taille(len)=",len(tuple33))
for i in tuple3:    print(i)

#SET
d={"janvier","fevrier","mars","avril"}


print("le première mos de l'année est=",b[0])

#LIST
for i in b:
    print("la liste contien l'info suivante",i)
#AJOUTER ELEMNTS À LA LISTE
b.append("mai")
taillelist=len(b)
print("la taille de la liste est ",taillelist)
checkType(b)
checkType("mai")
checkType(["mai","juin"])


for i in b:
    print("la liste contien l'info suivante",i)

for i in b2:
    print("la liste2 contien l'info suivante",i)
for i in b3:
    print("la liste3 contien l'info suivante",i)
b3+=extra
for i in b3:
    print("la liste3 CONCATENE contien l'info suivante",i)


for i in c:
    print("le tuple contient l'info suivante ",i)

for i in d:
    print("le set contient l'info suivante ",i)
    