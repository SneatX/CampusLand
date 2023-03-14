#Calcular el valor a pagar a los docentes dependiendo de sus horas hechas y su categoria y la sumatoria de el total a pagar
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 01/02/2023

cantidad_docentesA = 0
cantidad_docentesB = 0
cantidad_docentesC = 0
valor_total_pagar = 0


N = int(input("Ingrese el numero de usuarios: "))

for i in range (1 , N + 1):
    nombre = input("Ingrese su nombre por favor: ")
    id = input("Ingrese su documento de identidad ")
    categoria = input("Ingrese su categoria\nA = $25.000\nB = $35.000\nC = $50.000\nCategoria a la cual pertenezco: ")
    horas_trabajadas = int(input("Ingrese el numero total del horas trabajadas hasta el momento:  "))
    
    if categoria == "A" or categoria == "a":
        valorHora = 25000
        cantidad_docentesA = cantidad_docentesA +1
        
    elif categoria == "B" or categoria =="b":
        valorHora = 35000
        cantidad_docentesB = cantidad_docentesB + 1
        
    elif categoria == "C" or categoria =="c":
        valorHora = 50000
        cantidad_docentesC = cantidad_docentesC +1
        
    else:
        print("Ingrese un valor valido por favor y intente de nuevo")
        
    valorTotal = valorHora * horas_trabajadas
    
    valor_total_pagar = valor_total_pagar + valorTotal
    
    print("El total de honorarios para  " , nombre , "es de: $" , valorTotal)
    
print("El valor total a pagar por todos los docentes es: $" , valor_total_pagar , "\nCantidad de docentes categoria A = " , cantidad_docentesA , "\ncantidad de docentes categoria B = " , cantidad_docentesB , "\nCantidad de docentes categoria C = " , cantidad_docentesC)

            
            