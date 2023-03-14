#programa que cuente las palabras de un nombre o texto que le ingresemos con diccionarios
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 14/02/2023
lista_nombres = {}
nombre = input("Ingrese su nombre completo: ")
while nombre.upper() != "FIN":
    lista_palabras = nombre.strip().split()
    lista_nombres[nombre] = len(lista_palabras) 
    nombre = input("Ingrese su nombre completo: ")
for k in lista_nombres:
    print(k , "==>" ,lista_nombres[k])