#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys

#FONCTIONS AVEC ARGUMENTS MULTYPLES
def displayManyStrings(*argu):    
    print("les parametres argu sont:",argu,"avec une taille",len(argu),"objet de type type(argu)",type(argu),"ou égal au type type((*argu,))",type((*argu,)) )

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

#FONCTIONA VAEC VAELURS PAR DEFAULT OU KEYWORD ARGUMENT 
def displayKwordargsDefault(name="toto",age=45):
    print("mon nom c'est %s de type %s et j'ai %s de type %s" %(name,type(name),age,type(age)))

#positional et kword 
#def example(arg_1, arg_2, *args, **kwargs):
#positional et kword arguments hierachie
#def example2(arg_1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):
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



#utilisation de fonction positionnel avec passage de ARGS* (tuple)
display3parameters("hola1", 45, "hola3")
tuple1=("hola1",45,"hola5")
tuple11=(*tuple1,)
#tuple2=("hola1",45,"hola5","extra")

#RELATION ENTRE ARGUMETS MULTIPLES *ARGS  ET TUPLE
print("le type de variable tuple1 est =",type(tuple1),"avec taille(len)=",len(tuple1))
print("le type de variable (*tuple1,) est =",type((*tuple1,)),"avec taille(len)=",len((*tuple1,)))
print("le type de variable *tuple11=(*tuple1,) est =",type(tuple11),"avec taille(len)=",len(tuple11))
# ERROR TypeError: display3parameters() missing 2 required positional arguments: 'param2' and 'param3' 
try:
    display3parameters(tuple1)
except :
    print("TypeError: display3parameters() missing 2 required positional arguments: param2 and param3")
print("END du programme")

#
try:
    display3parameters(*tuple1)
except :
    print("TypeError:ERROR")
print("END du programme")


display3parameters(*tuple1)



#-------------APPEL D'UNE FONCTION AVEC KEWORD ARGUMENTS
displayKwordargsDefault("Carlos",33 )
displayKwordargsDefault("Carlos","trente-trois" )
displayKwordargsDefault()

#APPEL AVEC UN ARGUMENT DEFINIT EXPLICITEMENT PAR NOM
displayKwordargsDefault(name="yuyu", age=77)
displayKwordargsDefault( age=77,name="yuyu")
displayKwordargsDefault( name="yuyu")

#ERROR UN ARGUMENT DEFINIT EXPLICITEMENT NON CONNU
try:
    displayKwordargsDefault(name="yuyu", poids=77)
except (TypeError):
    print("TypeError: displayKwordargsDefault() got an unexpected keyword argument poids NON DEFINIT")
