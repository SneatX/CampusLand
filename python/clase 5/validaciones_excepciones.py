#masomenos como se usa el ciclo while True
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 03/02/2023
x = int(input("Ingrese un numero entero: "))
while x != -1:
    
    while True:
        try:
            x = int(input("Ingrese un numero entero: "))
            break
        except ValueError:
            print("El valor ingresado no es un numero entero, intente de nuevo...")