# La institución educativa “SamEduca” cuenta con N docentes, conociendo de cada uno de ellos su número de cédula, nombre, categoría y números de horas laboradas en el mes. Se pide realizar un programa que calcule el valor de los honorarios de cada docente y el valor total a pagar por concepto de honorarios. Para este proceso, nos suministran el diccionario donde se define el valor de la hora para cada categoría, así: diccionario_categoria={1:25000,2:30000,3:40000,4:45000,5:60000} Se debe imprimir el nombre del docente, el valor de sus honorarios y el valor total de honorarios, el de los N docentes.
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 13/02/2023
total_honorarios = 0
lista_docentes = []

N = int(input("Ingrese el numero de docentes: "))

diccionario_categoria = {1:25000 , 2:30000 , 3: 40000 , 4:45000 , 5:60000}
for k in range (N):
    
    nombre = input("\nIngrese su nombre: ")
    id = input("Ingrese su id: ")
    categoria = int(input("Ingrese la categoria a la cual pertenece: "))
    horas_realizadas = int(input("Ingrese la cantidad de horas realizadas: "))
    
    honorarios = diccionario_categoria[categoria] * horas_realizadas
    total_honorarios += honorarios
    
    print("El docente " , nombre , "se le debe pagar: $" , honorarios)

print("\nTotal honorarios: $" , total_honorarios)