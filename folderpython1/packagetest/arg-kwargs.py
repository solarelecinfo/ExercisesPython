#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys


def displayKwargsNow(**kwargus):
    print("la variable kwargus vaut ",kwargus,"est de type ",type(kwargus),"est de taile ",len(kwargus))
    for key,value in kwargus.items():
        print("le key est",key,"le values est=",value,"de type type(value)",type(value))
    
    #**KWARGS : principe utilisé pour passer une nombre infinite des parametres avec key=value syntax 



#positional et kwword arguments hierachie
#def example2(arg_1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):

#FUNCTION WITH POSITIONAL AND KWARS ARGUMENTS
def displayPargKwar(param1,param2="default2",param3="default3"):
    params=(param1,param2,param3)
    print("la taille des parametres est =",len(params))
    for i in params:
        print ("les parametres sont %s" % i)

kwags_var={'resp1':1,'resp2':2,'resp3':3,5:500}

displayKwargsNow(resp1=1,resp2=2,resp3=3,resp4="numero4")
#FUNCTIONAL WITH POSYIONAL AND KWORD ARGUMENT

displayPargKwar("positional")#1 PARAMETRE# 
displayPargKwar("positional1", "kword2","kword3")#2 PARAM
#displayPargKwar(param2="kword2", "positional1")#1 ERROR SYNTAX ERROR
displayPargKwar("positional1",param3="kword3",param2="kword2" )

