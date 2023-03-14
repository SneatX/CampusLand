#calcular la nota cualitativa dependiendo de la nota cuantitativa
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 31/01/2023

nombre=input("Ingrese el nombre del estudiante por favor: ")
notaT=int(input("Ingrese la calificacion cuantitativa: "))
motivacion1 = "Felicidades, continua por el camino de la excelencia 📖 😁"
motivacion2 = "muy bien 😃"
motivacion3 = "esfuerzate un poco mas 😒"
antimotivacion = "cho pndjo"
if notaT <= 59:
    notaL = "C " + antimotivacion
elif notaT <= 79:
    notaL = "D " + motivacion3 
elif notaT <= 89: 
     notaL = "B " + motivacion2
else:
     notaL="A ," + motivacion1
     
print("El estudiante ", nombre , "tiene una nota cuantitativa de: " , notaT , " y una nota cualitativa de:" , notaL)