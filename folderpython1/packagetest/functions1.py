#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys

#FONCTIONS AVEC ARGUMENTS MULTYPLES
def displayManyStrings(*argu):    
    print("les parametres sont:",argu,"avec une taille",len(argu),"objet de type",type(argu) )

#FONCTIONS AVEC DEUX PARAMETRES POSITIONNELS
def display2parameters(param1,param2):
    tup1=(param1,param2)
    for i in tup1:
        print ("les parametres valent",i)
    return tup1        

#FONCTIONS AVEC TROIS PARAMETRES POSITIONNELS
def display3parameters(param1,param2,param3):
    tup1=(param1,param2,param3)
    print("le tuple resultant tup1(param1,param2,param3) vaut",type(tup1))
    for i in tup1:
        print ("les parametres valent",i)
    return tup1  

#FONCTION AVEC PLUSIEURS PARAMETRES >= 0 PARAMETRE
displayManyStrings("hola",1)
displayManyStrings("salut")
displayManyStrings()

#FONCTION POSITIONNEL
var1=display2parameters(4, "maisons")
print("le type de la reponse vaut",type(var1))
#FONCTION POSITIONNEL SANS NOMBRE DE PARAMETRES CORRESPONDANTS


try:
    var2=display2parameters("choco")
except TypeError:
    print("TypeError: display2parameters() takes 2 positional arguments but 1 were given")

print("fin d'éxécution du programme")   


try:
    var22=display2parameters("hola", "hola2","hola3")
except TypeError:
    print("TypeError: display2parameters() takes 2 positional arguments but 3 were given")

print("fin d'éxécution du programme")   



params=input("Ajouter vos parametres")
print("le type de params est ",type(params))
tup2=tuple(params)
print("le type de params après tupelisation est ",type(tup2))

try:
    print("try d'utiliser *args en passant un tuple tup2=",tup2)
    display2parameters(*tup2)
except TypeError:
    print("expeption le nombre de parametres est insuffiçante où il y en a de trop ,il faut exactement 2 parametres posiionnels dans la fonction ")

print("fin d'éxécution du programme2")   




#utilisation de fonction positionnel avec passage de ARGS* (tuple)
display3parameters("hola1", 45, "hola3")
tuple1=("hola1",45,"hola5")



