"""

1. Para tributar un determinado impuesto se debe ser mayor de 18 años y tener
unos ingresos iguales o superiores a 2.500.000 mensuales. Escribir un
programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
por pantalla si el usuario tiene que tributar o no.

""" 

edad= int (input("digite su edad "))
ingreso= int (input("digite sus ingresos mensuales "))


if edad>17 and ingreso>=2500000:
    print ("el usuario tiene que tributar")
else:
    print ("el usuario no tiene que tributar")