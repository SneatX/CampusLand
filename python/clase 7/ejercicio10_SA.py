#sumar cantidad de vocales con una lista
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 07/02/2023



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

###########################################################################################################################
N = validar_enteros("Ingrese la cantidad de letras: ")

lista_letras = [] 
letraA = 0
letraE = 0
letraI = 0
letraO = 0
letraU = 0

for i in range (N):
    letras =(input("Ingrese las letras una a la vez: "))
    lista_letras.append(letras)
    
for x in lista_letras:    
    
    if x == "a" or x == "A":
        letraA += 1
    elif x == "e" or x == "B":
        letraE += 1
    elif x == "i" or x == "I":
        letraI += 1
    elif x == "o" or x == "O":
        letraO += 1
    elif x == "u" or x == "U": 
        letraU += 1
        
print("a= ", letraA)
print("e= ", letraE)
print("i= ", letraI)
print("o= ", letraO)
print("u= ", letraU)
        
        
        
