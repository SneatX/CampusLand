#reto 1
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 08/02/2023


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

cli_mas = 0
cli_fem = 0

valor_final_productos_iva = 0
valor_final_iva = 0
valor_final_productos = 0

N = validar_enteros("Ingrese la cantidad de clientes del dia a procesar: ")

for i in range (N):
    
    valor_total_iva = 0
    valor_total_productos = 0
    valor_final = 0
    
    cedula_cliente = validar_enteros("Ingrese la cedula del cliente: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    
    while True:
        try:
            genero_cliente = input("Ingrese el genero del cliente\nM = masculino\nF = femenino\n")
            if genero_cliente.upper() != "M" and genero_cliente.upper() != "F"  :
                print("El genero debe ser M de masculino o F de femenino.")
                continue
            break
        except ValueError:
            print("El genero del cliente debe ser M/m de masculino o F/f de femenino")
            
    if genero_cliente == "M" or genero_cliente == "m":
        cli_mas += 1
    else:
        cli_fem +=1
    
    
    M = validar_enteros("Ingrese la cantidad de productos a procesar: ")
    for x in range(M):
        cod_producto = validar_enteros("Ingrese el codigo del producto: ")
        valor_unitario = validar_enteros("Ingrese el valor unitario del producto: $")
        cantidad_producto = validar_enteros("Ingrese la cantidad de productos que adquirio: ")
        
        tipo_iva = validar_numeros("Ingrese el tipo de IVA del producto, puede ser:\n1 : exento de IVA\n2 : Bienes, donde se aplica como IVA el 5%\n3 : General, donde se aplica como IVA el 19%\n" , 1 , 3)
       
        valor_producto = cantidad_producto * valor_unitario
        if tipo_iva == 1:
            iva= 0
        elif tipo_iva == 2:
            iva = valor_producto * 0.05
        else:
            iva = valor_producto * 0.19
            
        valor_final_producto = valor_producto + iva
        
        valor_total_iva +=iva
        valor_total_productos += valor_producto
        valor_final += valor_final_producto
    
        print("El valor del producto (valor unitario x cantidad) es de: $" , valor_producto)
        print("El valor del IVA para este producto es de: $" , iva)
        print("El valor final del producto es de: $" , valor_final_producto , "\n")
        
    valor_final_iva += valor_total_iva    
    valor_final_productos += valor_total_productos
    valor_final_productos_iva += valor_final_producto 
    print("valor total productos = $" , valor_total_productos)
    print("valor total iva = $" , valor_total_iva)
    print("El valor final de la compra es: $" , valor_final , "\n")

print("\n \n ")
 
print("Cantidad de clientes durante el dia = " , N)
print("Cantidad de clientes masculinos = " , cli_mas)
print("Cantidad de clientes femeninos = " , cli_fem)

print("Valor final iva = $" , valor_final_iva)
print("Valor mercancia vendida (iva excluido) = $" ,valor_final_productos )
print("Valor venta todos los productos (iva incluido) = $" , valor_final_productos_iva)





