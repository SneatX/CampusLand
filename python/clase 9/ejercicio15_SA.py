#agrupar unos datos y llamarlos despues 
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 13/02/2023


id = int(input("Ingrese su id: "))
lspersona=[]
while id > 0:
    persona ={}
    persona["id"] = id
    persona["nombre"] = input("Ingrese su nombre: ")
    persona["apellido"] = input("Ingrese su apellido: ")
    persona["fecha_na"] = input("Ingrese su fecha de nacimiento: ")
    
    lspersona.append(persona)
    
    id = int(input("\nIngrese el id de otra persona: "))
    
print("\n", "=" *30 , "\n")

for d in lspersona:
    print("\n", "=" *30 , "\n")
    print("ID: " , d["id"])
    print("Nombre: " , d["nombre"])
    print("Apellido: " , d["apellido"])
    print("Fecha de nacimiento: " , d["fecha_na"])
    
