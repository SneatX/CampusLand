
nombres = []
cantidad_parabras_total =[]
nombre = input("ingrese el nombre: ")
while nombre.lower() !="fin": #lower es para poner el texto ingresado en minuscula, upper es para ponerlo en mayuscula
    
    cantidad_parabras = len(nombre.split())
    cantidad_parabras_total.append(cantidad_parabras)
    nombres.append(nombre)
    nombre = input("ingrese el nombre: ")
    
print(nombres)
print(cantidad_parabras_total)