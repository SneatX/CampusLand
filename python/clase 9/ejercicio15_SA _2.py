#agrupar unos datos y llamarlos despues (de otra manera)
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 13/02/2023

id = int(input("Ingrese su id: "))

persona ={}

while id > 0:
    datos = {}
    datos["nombre"] = input("Ingrese su nombre: ")
    datos["apellido"] = input("Ingrese su apellido: ")
    datos["fecha_na"] = input("Ingrese su fecha de nacimiento: ")
    persona[id]= datos
    
    
    id = int(input("\nIngrese el id de otra persona: "))
    
print("\n", "=" *30 , "\n")

for k in persona:
    print("\n", "=" *30 , "\n")
    print("ID: " , k)
    print("Nombre: " , persona[k]["nombre"])
    print("Apellido: " , persona[k]["apellido"])
    print("Fecha de nacimiento: " , persona[k]["fecha_na"])
    
    
    
    