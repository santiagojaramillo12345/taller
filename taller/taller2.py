"""
Escribir un programa donde se ingrese la nota de las materias: desarrollo de
software, matemáticas, lógica programación, si el promedio es mayor o igual
que 3,0 muestre
"""

desarrolloDeSoftware =float(input("digite su nota de desarrollo de software de 0 a 5 "))

matematicas =float(input("digite su nota de matematicas 0 a 5 "))

lógicaProgramación =float(input("digite su nota de logica de programación 0 a 5 "))

promedio= (desarrolloDeSoftware+matematicas+lógicaProgramación+lógicaProgramación)/5

if promedio>=3.0:
    print(f"aprobo el curso con un acumulado de {promedio}")
    
else:
    print(f"perdio el curso :C  esfuersate mas su promedio fue de  {promedio} ")