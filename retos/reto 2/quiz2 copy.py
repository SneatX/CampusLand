#Quiz 
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 28/02/2023

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



nombre=input("Ingrese su nombre: ")
sueldo = 0
sueldo_total = 0

while nombre != "Fin":
    sueldo2= validar_enteros("Ingrese su sueldo: ")
    sueldo=sueldo+sueldo2
    nombre=input("Ingrese su nombre, para finalizar escriba literalmente Fin: ")
nomina=sueldo +(sueldo*0.25)

print("Salario total empleados: $" , "{:,.0f}".format(sueldo))
print("Nomina neta de todos los empleados con incremento de 25%: $" , "{:,.0f}".format(nomina))



    

