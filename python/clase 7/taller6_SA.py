#programa en el cual se ingresaran numeros hasta el 99999 se deseara conocer cuales y cuantos son pares e impares
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 07/02/2023

def validar_enteros(etiqueta):
    while True:
        try:
            dato = int(input(etiqueta))
            if dato <1:
                print("El numero tiene que ser mayor que 0")
                continue
            break
        except ValueError:
            print("El numero a ingresar debe ser entero.")
    return dato

############################################################################################################################################

numero_ingresado = validar_enteros("Ingrese el numero deseado, para acabar poner el 99999: ")
numeros = []
lista_pares = []
numeros_pares = 0

lista_impares = []
numeros_impares = 0

while numero_ingresado != 99999:
    numeros.append(numero_ingresado)
    numero_ingresado = validar_enteros("Ingrese el numero deseado, para acabar poner el 99999: ")
    
for x in numeros:
    if x %2 == 0:
        lista_pares.append(x)
        numeros_pares += 1
    else:
        lista_impares.append(x)
        numeros_impares += 1
            
        
print(lista_pares)
print("Hay un total de " , numeros_pares , " numeros pares")
print(lista_impares)
print("Hay un total de " , numeros_impares , " numeros impares")
