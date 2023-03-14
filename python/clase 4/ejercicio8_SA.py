#Decir si un numero es par o impar y mostrarlo
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 02/02/2023

numero = int(input("Ingrese el numero que desea hasta -1: "))
numPar = 0
numImpar = 0

while numero != -1:
    if numero %2 == 0:
        print("El numero es par")
        numPar = numPar + 1
        
    else:
        print("El numero es impar")
        numImpar = numImpar +1

    numero = int(input("Ingrese el numero que desea hasta -1: "))

print("Hubo un total de: " , numPar , "numeros pares")
print("Hubo un total de: " , numImpar , "numeros impares")

        



