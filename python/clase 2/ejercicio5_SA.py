#Calcular si tiene que irse en bus o taxi dependiendo del tiempo que tenga
#Hecho por: Santiago Alexander Ospina Pabón
#Fecha: 31/01/2023

tiempo=int(input("Ingrese los minutos restantes para llegar a su trabajo: "))

if tiempo <= 45:
    print("Es necesario que se vaya en taxi.")
else:
    print("Puede irse en bus.")
    