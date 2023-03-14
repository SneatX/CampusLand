#programa que guarde en diccionarios los precios de las frutas de la tabla
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 13/02/2023

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

fruta = {"platano":1.35 , "manzana":0.80 , "pera":0.85 , "naranja":0.70 }

for x,y in fruta.items():
    print(x, " ===> ",y)
    
while True:
    fruta_elegida = input("Ingrese el nombre de la fruta que desea: ")
    if fruta_elegida in fruta:
            break
    else:
        print("No disponemos de esa fruta")
        continue      
              
kilos = validar_enteros("Ingrese la cantidad de kilos que llevara: ")

precio = fruta[fruta_elegida]*kilos
print("El valor a pagar es: $" , precio)    