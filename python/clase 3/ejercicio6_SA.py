#Decir la tarifa de un servicio dependiendo del consumo y estrato de N usuarios
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 01/02/2023

N=int(input("Ingrese el numero de usuarios: "))
for i in range(1 , N + 1):
    nombre = input("Ingrese su nombre: ")
    codigo = (input(nombre + " ingrese su codigo: "))
    estrato = int(input(nombre + " ingrese su estrato: "))
    consumo = int(input(nombre + " ingrese su consumo del ultimo mes (en m^3): "))
    estado = input("Ingrese su estado de cuenta:\n1=Vigente\n2=Suspendido\n")
    
    
    if estado == "1":
        if estrato == 1:
            tarifaBasica = 10000
        elif estrato == 2:
            tarifaBasica = 20000
        elif estrato == 3:
            tarifaBasica = 30000
        elif estrato == 4:
            tarifaBasica = 45000
        elif estrato == 5:
            tarifaBasica = 60000
        elif estrato == 6:
            tarifaBasica = 70000
        else:
            print("Ingrese un dato valido")
            
        valorConsumo = consumo * 200
        valorTotal = valorConsumo + tarifaBasica
        
        print(nombre , " su tarifa basica es de: $" , tarifaBasica , "y un valor por consumo de: $" , valorConsumo )
        print("Saldo total = $" , valorTotal)
        
    else:
        print("Comuniquese con un asesor para dar solucion a su problema.")
        
print("Fin del ciclo")
        
    
    
    
        



