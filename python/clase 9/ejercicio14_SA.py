#Contar el numero de veces que una palabra aparece dentro de un texto
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 13/02/2023

dpalabras = {}
texto = input("Ingrese un texto: ")
lista_palabras = texto.strip().split()              #El strip quita los espacios de antes y despues del texto ,#El split me divide el texto por lo que yo le diga, osea espacios 

for pal in lista_palabras:
    if pal in dpalabras:
        dpalabras[pal] +=1
    else:
        dpalabras[pal] =1
        
for k in dpalabras:
    print(k, " ---- veces ---- " , dpalabras[k])