def imprimirDic(d):
    d2 = d.copy() #Guarda en lugares diferentes d y d2 por lo que no significan lo mismo
    d2["Ciudad"] = "Bucaramanga"
    print("d2['Ciudad'] = " , d2["Ciudad"])
    print("d['Ciudad'] = " , d["Ciudad"])





#d1 = {"Nombre":"sara","Edad":27,"Documento":1003882}
#print(d1)

d3 = dict(Nombre="sara" , Edad=27 , Documento=1003452)


print(d3.get("Sexo"))   #manera 1    si se pone un valor que no existe como print(d3.get("Sexo")) sale none
print(d3.get("Sexo","Otro"))   #sale el valor del segundo valor, osea Otro
#print(d3["Sexo"])       #manera 2   si se pone un valor que no existe como print(d3["Sexo"])  sale un error}


print("\n")


####################  si ponemos eso nos dice si el valor existe o no, con false o true  ###########
print("Edad" in d3)     #en este caso True
print("Sexo" in d3)     #en este caso False


print("\n")


d3["Edad"]=20    #De esta manera modificamos las claves
print(d3.get("Edad")) 

d3["Sexo"]="F"  #Y de la misma manera agregamos claves
print(d3.get("Sexo")) 

del d3["Sexo"]  # Y de esta manera con la clave se elimina
print(d3.get("Sexo")) 


print("\n")


### KEYS devuelve una lista con todas las llaves del diccionario 
print(d3.keys())

### VALUES devuelve una lista con los valores del diccionario
print(d3.values("Nombre"))

### ITEMS devuelle una pareja, o una lista de tuplas 
print(d3.items())


print("\n")


##### Iterar o recorrer el diccionario
for k in d3:
    print(k , "==>" ,d3[k])
    
    
print("\n")


#otra manera de iterar (normalmente mas usada)
for x,y in d3.items():
    print(x,y)
    
    
print("\n")


#Asi eliminamos el diccionario completo con variable.clear() o con variable = {}
d3.clear()
d3= {}

print(d3)


    