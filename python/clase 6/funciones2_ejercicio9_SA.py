#Realizar la facturacion de una empresa telefonica dependiendo del estrato con funciones
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 01/02/2023


################################################################### funcion 1. ####################################################################
def facturacion(estrato,impulsos):
    if estrato == 1:
        tarifa_basica = 10000
    elif estrato == 2:
        tarifa_basica = 15000
    elif estrato == 3:
        tarifa_basica = 20000
    elif estrato == 4:
        tarifa_basica = 25000
    else:
        tarifa_basica = 30000
        
    valor_impulsos = impulsos * 100
    pagar_abonador = valor_impulsos + tarifa_basica
    
    return pagar_abonador, tarifa_basica, valor_impulsos

########################################################## funcion 2, validar enteros y estrato.####################################################

 #manera 1
def validar_enteros(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))                      
            break
        except ValueError:
            print("El dato a ingresar debe ser un numero entero.")
    return dato

 #manera 2
def validar_estrato():
    while True:
        try:
            estrato=int(input("Ingrese el estrato del abonado\n1 = 10000\n2 = 15000\n3 = 20000\n4 = 25000\n5 = 30000\n"))
            if estrato <1 or estrato >5:
                print("El estrato debe ser entre 1 y 5")
                continue                                    
            break
        except ValueError:
            print("Ingrese un valor numerico entero.")
    return estrato

############################################################# Programa principal.###################################################################
valor_total = 0
numero_abonados = validar_enteros("cantidad de abonados: ")
for i in range (numero_abonados):
    
    nombre = input("Ingrese al nombre del abonado: ")
    
    estrato = validar_estrato()
              
    impulsos = validar_enteros("Ingrese la cantidad de impulsos: ")
    
    
    ########################################################## llamar a la funcion. ################################################################
    pagar_abonador , tarifa_basica , valor_impulsos = facturacion(estrato,impulsos)#no importa como se llamen las variables, solo importa el orden
    valor_total += pagar_abonador
    
    print("Nombre: " , nombre)
    print("tarifa basica: $" , "{:,.0f}".format(tarifa_basica ))
    print("valor de los impulsos: $" , "{:,.0f}".format(valor_impulsos))
    print("Valor a pagar abonador: $" , "{:,.0f}".format(pagar_abonador))
print("El valor total es de: $" , "{:,.0f}".format(valor_total))
    

