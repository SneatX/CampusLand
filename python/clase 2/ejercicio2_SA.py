#Calcular si recibe o no subsidio de transporte
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 31/01/2023

nombre=input("Ingrese el nombre del trabajador: ")
sueldo=int(input(nombre + " ingrese su sueldo por favor:"))
if sueldo <= 1200000 :
    subsidio=120000 
else: 
    subsidio=0
print(nombre," su subsidio sera de: ",subsidio)
respuesta=input("le gustaria saber cual es el total? (Y/F)")
if respuesta == "Y":
    print(nombre + " su sueldo es de: $",sueldo +subsidio)
    
else: print("Gracias por su atencion :3")
