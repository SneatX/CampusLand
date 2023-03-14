#Realizar la facturacion de una empresa telefonica dependiendo del estrato 
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 01/02/2023


valor_total = 0

while True:
    try:
        numero_abonados = int(input("Ingrese el numero de abonados: "))
        break
    except ValueError:
        print("El numero de abonados debe ser un entero.")
        
for i in range (numero_abonados):
    nombre = input("Ingrese el nombre del abonado: ")
    
    while True:
        try:
            estrato = float(input("Ingrese el estrato del abonado\n1 = 10000\n2 = 15000\n3 = 20000\n4 = 25000\n5 = 30000\n"))
            if estrato <1 or estrato >5:
                print("El estrato tiene que estar entre 1 y 5.")
                continue
            break
        except ValueError:
            print("El estrato tiene que ser un valor entero")
            
    while True:
        try:
            cantidad_impulsos = float(input("Ingrese la cantidad de impulsos de " + nombre +": "))
            break
        except ValueError:
            print("Ingrese un valor numerico.")
            
    if estrato == 1:
        tarifa_basica = 10000
    elif estrato == 2:
        tarifa_basica = 15000
    elif estrato == 3:
        tarifa_basica = 2000
    elif estrato == 4:
        tarifa_basica = 25000
    else:
        tarifa_basica = 30000
        
    valor_impulsos = cantidad_impulsos * 100
    valor_abonador = valor_impulsos + tarifa_basica
    valor_total += valor_abonador
    
    print("El valor a pagar a ", nombre , " es de: $" , valor_abonador , "\ntarifa basica = $" , tarifa_basica , "\nvalor impulsos = $" , valor_impulsos)

print("El valor a pagar a todos los abonados es de: $" , valor_total)
            
            
            
            