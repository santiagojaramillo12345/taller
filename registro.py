#validar la confirmacion de una contraseña, si coinciden clave y la confirmacion coinciden debe salir bienbenido , de lo contrario usuario bloqueado

key = input("porfavor ingrese la contraseña")
password = input("porfavor confirme la contraseñña")

if key ==  password:
    print("bienbenidos al sistema")
    
else:
    print("contraseña incorrecta")
    
    
    #upper(): cambia el texto a mayuscula
    #tittle(): cambia a mayuscula la primera letra de cada palabra
    #lower(): cambia todo a minuscula
    