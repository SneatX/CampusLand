#decir en cuanto le queda la matricula dependiendo del programa y la beca
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 01/02/2023

nombre=input("Nombre del estudiante: ")
codigo=int(input(nombre + " ingrese su codigo de estudiante: "))
print("Programa academico al cual pertecene")
print("1: Tecnico en sistemas")
print("2: Tecnico en desarrollo de videojuegos")
print("3: Tecnico en animacion digital")
programa = int(input("Ingrese el numero del programa academico al cual pertenece: "))
print("Beca en la cual hace parte")
print("1: Beca por rendimiento academico (50 (%) de descuento)")
print("2: Beca cultural - Deportes (40(%) de descuento)")
print("3: Sin beca")
beca = int(input("Ingrese el numero de beca al cual pertenece: "))
error = print("Por favor reinicie el programa y elija una opcion valida.")
if programa == 1:
    precio = 800000
elif programa ==2:
    precio = 1000000
elif programa == 3:
    precio = 1200000
else:
    print("Por favor reinicie el programa y elija una opcion valida.")

    
print(precio)
if beca == 1:
    precio = precio * 0.5
elif beca == 2:
    precio = precio * 0.6
elif beca == 3:
    precio = precio 
else: 
    print("Por favor reinicie el programa y elija una opcion valida.")
    
print("El estudiante " , nombre , "identificado con el codigo" , codigo , "tiene un valor neto a pagar de: $" , int(precio) )

