#Calcular la comision de los vendedores sobre las ventas realizadas en el mes y el tipo de vendedor usando while con mas datos y pago a contado y a credito 
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 03/02/2023


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

def validar_numeros(etiqueta, a, b):
    while True:
        try:
            dato = int(input(etiqueta))
            if dato <a or dato>b:
                print("El numero ingresado no esta en el rango permitido")
                continue
            break
        except ValueError:
            print("El numero a ingresar debe ser entero.")
    return dato
###############################################################################################################################################
N = validar_enteros("Ingrese la cantidad de vendedores: ")
 
valor_total_comisiones = 0
for i in range (N):
    
    total_ventas_vendedor = 0
    total_comision_vendedor = 0
    
    nombre = input("Ingrese su nombre: ")
    cedula = input(nombre + " ingrese su documento de identidad: ")
    tipo_vendedor = validar_numeros("Ingrese el tipo de vendedor al cual pertenece\n1 = puerta a puerta\n2 = Telemercadeo\n3 = ejecutivo de ventas\n" , 1, 3 )        
    numero_ventas = validar_enteros("Ingrese la cantidad de ventas que realizo: ")
    
    for i in range(numero_ventas):
        
        nombre_cliente = ("Ingrese el nombre del cliente: ")
        codigo_cliente = ("Ingrese el codigo del cliente: ")
        tipo_venta = validar_numeros("Ingrese el tipo de venta que realizo\n1 = contado\n2 = credito\n" , 1 , 2)
        valor_venta = validar_enteros("Ingrese el valor de la venta: ")
        
        if tipo_vendedor == 1:
            if tipo_venta == 1:
                comision = valor_venta * 0.25
            else:
                comision = valor_venta * 0.2 
                
        elif tipo_vendedor == 2:
            if tipo_venta == 1:
                comision = valor_venta * 0.15
            else:
                comision = valor_venta * 0.1      
        else: 
            if tipo_venta ==1:
                comision = valor_venta * 0.2
            else:
                comision = valor_venta * 0.15
                
        total_comision_vendedor += comision
        
        valor_total_comisiones += comision
        
        total_ventas_vendedor += valor_venta
        
        print("comision por esta venta: $" , "{:,.0f}".format(comision))
        
    print("Las ventas totales de " , nombre , "son de: $" , "{:,.0f}".format(total_ventas_vendedor))           
    print("El valor a pagar a " , nombre , " por concepto de comision por ventas es de: $" , "{:,.0f}".format(total_comision_vendedor))
    
print("El valor total a pagar por todas las comisiones de todos los vendedores es: $" , "{:,.0f}".format(valor_total_comisiones))