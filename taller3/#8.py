
# Online Python - IDE, Editor, Compiler, Interpreter

acum=0
respon=""
while respon!="N":
    print("hamburguesas sencillas (S)")
    print("dobles (D)")
    print("triples (T)")
    print("salir(x)")
    
    opc=input("seleccione tipo de hamburguesa:")
    cantidad=int(input("ingrese cantidad de hamburguesa"))
            
        
    if opc=="s":
        acum=acum+(14000*cantidad)
    elif opc=="d":
        acum=acum+(19000*cantidad)
    elif opc=="t":
        acum=acum+(23500*cantidad)
     
    respon=input("desea agregar mas ham (S) Sí (N) No") 
        
    t_pago=input("desea pagar con tarjeta??")
    if t_pago=="si":
        print("el valor total ",acum*0.05)
        
    else:
        print("el valor total ",acum)
    
            
            
            
            
        