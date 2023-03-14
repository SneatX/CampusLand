#Dado el nombre y el estrato, calcular cuanto pagaria por el servicio de energia
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 31/01/2023

nombre=input("Ingrese el nombre del ciudadan@: ")
estrato=int(input("Ingrese el estrato del ciudadan@: "))

if estrato ==1:
    tarifa = 10000
elif estrato==2:
    tarifa = 15000
elif estrato ==3:
    tarifa = 30000
elif estrato ==4:
    tarifa = 50000
else:
    tarifa = 65000

print("Nombre: " , nombre)
print("Tarifa: " , tarifa)