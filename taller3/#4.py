# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:57:37 2022

@author: usuario
"""

cont_p=0
acum_p=0
cont_t=0
acum_t=0
seguir=""
while seguir!="no":
    
    cantidad=int(input("ingrese cantidad a pagar"))
    tipo=input("con que tipo desea pagar:A(pse)  B(tarjeta de credito)")
    
    
    
    if tipo=="a":
        cont_p=cont_t+1
        acum_p=acum_t+1
    else:
        cont_b=cont_t+1
        acum_b=acum_t+1
        
    seguir=input("¿Desea seguir ingresando mas valores ?")
    
    
    if cont_p==cont_t:
        print("ambos medios de pago se utilizaron la misma canidad de veces ")
    elif cont_p>cont_t:
        print("el medio de pago mas usado due (pse)")
    else:
        print("el medio de pago mas usado fue (tarheta de credito)")
        
        
print("pagos total",cont_p+cont_t)
print("pagos total ( pse)",acum_p)
print("pagos total ( tarjeta de credito)",acum_t)
        
    

    