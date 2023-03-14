#Calcular la comision de los vendedores sobre las ventas realizadas en el mes y el tipo de vendedor usando while con mas datos y pago a contado y a credito 
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 03/02/2023
while True:
    try:
        N = int(input("Ingrese la cantidad de vendedores: "))
        break
    except ValueError:
        print("La cantidad de vendedores tiene que ser un numero entero")
    
valor_total_comisiones = 0
for i in range (N):
    
    total_ventas_vendedor = 0
    total_comision_vendedor = 0
    
    nombre = input("Ingrese su nombre: ")
    cedula = input(nombre + " ingrese su documento de identidad: ")
    tipo_vendedor = float(input("Ingrese el tipo de vendedor al cual pertenece\n1 = puerta a puerta\n2 = Telemercadeo\n3 = ejecutivo de ventas\n"))
    numero_ventas = int(input("Ingrese la cantidad de ventas que realizo: "))
    
   
    
    for i in range(numero_ventas):
        
        
        
        nombre_cliente = ("Ingrese el nombre del cliente: ")
        codigo_cliente = ("Ingrese el codigo del cliente: ")
        tipo_venta = float(input("Ingrese el tipo de venta que realizo\n1 = contado\n2 = credito\n"))
        valor_venta = float(input("Ingrese el valor de la venta: "))
        
        
            
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
                
        elif tipo_vendedor == 3:
            if tipo_venta ==1:
                comision = valor_venta * 0.2
            else:
                comision = valor_venta * 0.15
                
        total_comision_vendedor +=comision
        
        valor_total_comisiones +=comision
        
        total_ventas_vendedor += valor_venta
        print("comision por esta venta: $" , "{:,.0f}".format(comision))
        
    print("Las ventas totales de " , nombre , "son de: $" , "{:,.0f}".format(total_ventas_vendedor))
                      
    print("El valor a pagar a " , nombre , " por concepto de comision por ventas es de: $" , "{:,.0f}".format(total_comision_vendedor))
    
print("El valor total a pagar por todas las comisiones de todos los vendedores es: $" , "{:,.0f}".format(valor_total_comisiones))
                    
                    
                
                
            
        
    
