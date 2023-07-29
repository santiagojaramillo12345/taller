#ELIF: Validar 2 o mas condiciones.
"""
sintaxis

if condicional1:
        instruction
elif condicional2:
        instruction
elif condicional3:  
        instruction
elif condicional4:
    instruction
 .
 .
 .
 else(opcional)           
                
"""

#validar cual numero de dos ingresados es mayor que el otro, considerar la posibilidad en que sean iguales.


numero1= int (input("digite un numero "))

numero2= int (input("digite un numero a comparar con el anterior "))


if numero1 > numero2:
    numeroM = numero1
    print (f"el numero mayor es {numeroM}")
    
elif numero2 > numero1:
    numeroM = numero2
    print (f"el numero mayor es {numeroM}")
else:
    print("son iguales")
    
    