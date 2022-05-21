# -*- coding: utf-8 -*-
"""
Created on Thu May 19 15:39:54 2022

@author: usuario
"""


distancia=int(input("ingrese distancia a recorrer en kilometros"))
dias=int(input("número de días de estancia"))



if distancia>500 and distancia<700 :
    if dias>4:
        print("la aereo linea le ha hecho un descuento del 10% ")
        print("valor total a pagar =",distancia *25000- 0.10)

if distancia>700 and distancia<1000 :
    if dias>7:
        print("la aereo linea le ha hecho un descuento del 20% ")
        print("valor total a pagar =",distancia *25000- 0.20)
        
        
if distancia>=1000  :
    if dias>12:
        print("la aereo linea le ha hecho un descuento del 30% ")
        print("valor total a pagar =",distancia *25000- 0.30)





















