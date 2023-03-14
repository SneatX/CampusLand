#Calcular la comision de los vendedores sobre las ventas realizadas en el mes y el tipo de vendedor usando while
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 02/02/2023

cedula = int(input("Ingrese su cedula: "))
ventas_mes = 0
comision_total = 0


while cedula != -1:

    nombre = input("Ingrese su nombre: ")
    tipo_vendedor  = float(input("Ingrese la categoria a la cual pertenece: \n1 = Puerta a puerta\n2 = Telemercadeo\n3 = ejecutivo de ventas\nPertenezco a la categoria:  "))
    valor_ventas = float(input("Ingrese el valor de ventas total realizado durante el mes:  "))
    
    if tipo_vendedor == 1:
        comision = 0.2 * valor_ventas

    elif tipo_vendedor == 2:
        comision = 0.15 * valor_ventas

    elif tipo_vendedor ==3:
        comision = 0.25 * valor_ventas
        
    else:
        print("Ingrese un valor valido")

    ventas_mes += valor_ventas
    comision_total += comision


    print("Valor a pagar en comision a" , nombre , "es de: $" , comision)
    
    cedula = int(input("Ingrese su cedula: "))


print("El valor total de ventas del mes es de" , ventas_mes)
print("Valor total a pagar en comision es: $" , comision_total)




    





