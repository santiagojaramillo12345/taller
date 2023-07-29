  #validar si un numero es mayor de edad y tiene pasaporte, si es asi debe monstrar un mensaje que indique que puede salir del pais,de lo contrario muestre no puede abandonar el pais, los datos deben ser solicitado al usuario
    
    
pasaporte =bool(input("tiene pasaporte si o no "))
    

if pasaporte =="si":
            pasaporte=True
else:
    pasaporte=False
    
    edad =int (input("escribe su edad "))
    
    
    if  edad >=18 and pasaporte ==True :
        print ("su pasaporte esta aprobado y puede salir del pais")
    
    else:
        print ("su pasaporte no es aprobado y no puede salir del pais")

