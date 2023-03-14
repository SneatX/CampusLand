#Calcular nota definitiva estudiante
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 27/01/2023

nombre=input("Ingrese el nombre del estudiante: ")
nota1=float(input("Ingrese la nota 1: "))
nota2=float(input("Ingrese la nota 2: "))
nota3=float(input("Ingrese la nota 3: "))
notaIngles=float(input("Ingrese la nota de ingles: "))

promedio= (nota1*0.2) + (nota2*0.25) + (nota3*0.35) + (notaIngles*0.2)
print("El estudiante " , nombre , " tiene un promedio de: " , promedio)
