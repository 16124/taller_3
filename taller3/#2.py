# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:14:14 2022

@author: usuario
"""

producto=input("ingrese nombre del producto")
precio=int(input("ingrese valor del producto"))

descuento=precio-0.10
iva=descuento+0.19
if producto=="computador":
    if precio>=1000000:
        print("se le ha hecho un descuento del 10%")
        print("valor con descunto=",descuento)
        print("valor total mas iva=",iva)
        
        
descuento=precio-0.10
if producto=="celular":
    
    if precio>=500000 and precio<=1000000:
        
        print("se le ha hecho un descuento del 5%")
        print("valor con descunto=",descuento)
        print("valor total mas iva=",iva)
        
descuento=precio-0.10
 
if producto=="camara":
    
    print("se le ha hecho un descuento del 3%")
    print("valor con descunto=",descuento)
    print("valor total mas iva=",iva)
    

                
        








