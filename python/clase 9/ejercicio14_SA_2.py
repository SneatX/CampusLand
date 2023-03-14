#Contar el numero de veces que una palabra aparece dentro de un texto
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 13/02/2023

texto = input("Ingrese un texto: ")
dpalabras = {}
lista_palabras = texto.strip().split()              #El strip quita los espacios de antes y despues del texto ,#El split me divide el texto por lo que yo le diga, osea espacios 

for pal in lista_palabras:
    
    dpalabras[pal] = dpalabras.get(pal,0) + 1
        
for k in sorted(dpalabras):            #sorted lo ordena en orden alfabetico
    print(k, " ---- veces ---- " , dpalabras[k])