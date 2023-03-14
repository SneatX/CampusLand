#Decir la tarifa de un servicio dependiendo del consumo y estrato de N usuarios con sumatoria
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 01/02/2023


valorFinal=0

while True:
    try:
        N=int(input("Ingrese el numero de usuarios: "))
        break
    except ValueError:
        print("El numero de usuarios tiene que ser un entero")

for i in range(1 , N + 1):
    nombre = input("Ingrese su nombre: ")
    codigo = (input(nombre + " ingrese su codigo: "))
    
    while True:
        try:
            estrato = int(input(nombre + " ingrese su estrato de 1 a 6: "))
            if estrato <1 or estrato >6:
                print("El estrato debe estar entre 1 y 6")
                continue
            break
        except ValueError:
            print("El valor debe ser numerico")
             
    while True:
        try:
            consumo = float(input(nombre + " ingrese su consumo del ultimo mes (en m^3): "))
            break
        except ValueError:
            print("El consumo debe ser un valor numerico")
    
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
        else:
            tarifaBasica = 70000
            
        valorConsumo = consumo * 200
        valorTotal = valorConsumo + tarifaBasica
        valorFinal += valorTotal #Tambien se puede poner ----- valorFinal = valorFinal + valorTotal
        
                                     #se usa el --- "{:,.0f}".format(variable) --- para agregar las comas al mil y el numero dice la cantidad de decimales deseados
        print(nombre , " su tarifa basica es de: $" , "{:,.0f}".format(tarifaBasica) , "y un valor por consumo de: $" , "{:,.0f}".format(valorConsumo) )
        print("Saldo total = $" ,"{:,.0f}".format(valorTotal))
        
        
        
    else:
        print("Comuniquese con un asesor para dar solucion a su problema.")
        
print("El valor total a pagar de todos los usuarios es de: $" , "{:,.0f}".format(valorFinal) , "\n")
        
    
    
    
        



