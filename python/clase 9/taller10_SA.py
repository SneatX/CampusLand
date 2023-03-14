articulos = {1:"Lapiz" , 2:"Cuadernos" , 3:"Borrador" , 4:"Calculadora" , 5:"Escuadra"}

valores = {1:2500 , 2:3800 , 3:1200 , 4:35000 , 5:3700}

valor_total_compra = 0

lista_comprada = []

N = int(input("Ingrese la cantidad de articulos comprados: "))

for i in range (N):
    codigo = int(input("\nIngrese el codigo del articulo: "))
    cantidad = int(input("Ingrese la cantidad comprada: "))
    
    valor_compra = valores.get(codigo) * cantidad
    
    print("Nombre del articulo: " , articulos.get(codigo))
    print("Precio unitario: " , valores.get(codigo))
    print("Articulos comprados: " , cantidad)
    print("valor compra: $" , valor_compra)
    valor_total_compra += valor_compra
    lista_comprada.append(articulos.get(codigo))
    
print("\nEl total de la compra es de: $" , valor_total_compra)
print("Productos comprados" , lista_comprada)
