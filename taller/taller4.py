"""

Realizar un programa que muestre un menú con opciones de colores primario
(Amarillo, azul, rojo, blanco y negro), el usuario debe escoger 2 colores de los
ofrecidos en el menú y con una secuencia de if y elif evaluar las posibles
combinaciones generadas con los colores primarios. Si el usuario escogió
colores que no generan otro al ser combinados debe mostrar un mensaje de
“opciones no validas”

"""

print ("Elije un color de los siguientes colores")
print ("1. amarillo")
print ("2. azul")
print ("3. rojo")
print ("4. blanco")
print ("5. negro")
color1 = int (input ())

print ("Elije un color para cobinarlo con el primer color elegido de los siguientes colores")
print ("1. amarillo")
print ("2. azul")
print ("3. rojo")
print ("4. blanco")
print ("5. negro")
color2 = int (input ())

if color1==1 and color2==1 :
    print (f"El color combinado es amarillo")
elif color1==2 and color2==2:
    print (f"El color combinado es azul")
elif color1==3 and color2==3:
    print (f"El color combinado es rojo")
elif color1==4 and color2==4:
    print (f"El color combinado es blanco")
elif color1==5 and color2==5:
    print (f"El color combinado es negro")
elif color1==1 and color2==2 or color2==1 and color1==2:
    print (f"El color combinado es verde")
elif color1==2 and color2==3 or color2==3 and color1==2:
    print (f"El color combinado es violeta")
elif color1==1 and color2==5 or color2==1 and color1==5:
    print (f"El color combinado es naranja")
elif color1==1 and color2==4 or color2==4 and color1==1:
    print (f"El color combinado es amarillo claro" )
elif color1==2 and color2==4 or color2==4 and color1==2: 
    print (f"El color combinado es azul claro")
elif color1==3 and color2==4 or color2==4 and color1==3:
    print (f"El color combinado es rojo claro")
elif color1==1 and color2==5 or color2==5 and color1==1:
    print (f"El color combinado es amarillo oscuro")
elif color1==2 and color2==5 or color2==5 and color1==2:
    print (f"El color combinado es azul oscuro")
elif color1==3 and color2==5 or color2==5 and color1==3:
    print (f"El color combinado es rojo oscuro")
else: 
    print ("Opcion novalida  elige un numero del 1 al 5 ")














