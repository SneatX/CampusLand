N = int(input("Cuantos clientes va a procesar? :"))

numH = 0
numF = 0

valTotalCompraFinal = 0
valTotalIvaFinal = 0
valTotalProdIvaFinal = 0

for i in range (N):
    print("Cliente #", i)
    cedula = input("Cedula del cliente: ")
    nombre = input("nombre del cliente: ")
    sexo = input("Sexo (M: masculino o F: femenino)").upper()
    
    if sexo == "M":
        numH += 1
    else:
        numF += 1
        
    mprod = int(input("Ingrese la cantidad de productos: "))
    vaTotalCompra = 0
    valTotalProdIva = 0
    vaTotalIVA = 0
    
    for i in range (mprod):
        cod = int(input("Codigo del producto: "))
        valu = int(input("Valor del producto: "))
        cantp = int(input("cantidad de productos: "))
        tipoIva = int(input("tipo de iva (1 o 2 o 3): "))
        valprod = valu * cantp
        
        if tipoIva == 1:
            ivaprod = 0
        elif tipoIva == 2:
            ivaprod = valprod * 0.05
        else:
            ivaprod = valprod * 0.19
            
        #----valores de compra----#
        print("Valor del producto: " ,valprod)
        print("Valor del iva: " , ivaprod)
        valprodiva = valprod + ivaprod
        print("Valor del producto con iva: " , valprodiva)
        
        vaTotalCompra += valprod
        valTotalProdIva += ivaprod
        vaTotalIVA += ivaprod
    print("valor de los productos en total: " , valTotalProdIva)
    print("valor total iva: " ,vaTotalIVA )
    
    valTotalCompraFinal += vaTotalCompra
    valTotalIvaFinal += vaTotalIVA
    valTotalProdIva += valTotalProdIva

print("-----Resumen del dia-----")
print("Cantidad de clientes hombres: " , numH)
print("Cantidad de clientes mujeres: " , numF)
print("El valor de la compra sin incluir el iva del dia es: " , valTotalCompraFinal)
print("El valor total del iva del dia es: " , valTotalIvaFinal)
print("El valor de la compra del dia incluido el iva es" , valTotalProdIva)

