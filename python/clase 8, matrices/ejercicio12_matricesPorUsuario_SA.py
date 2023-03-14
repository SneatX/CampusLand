#matrices por usuario
def imprimirMatriz(mat):
    for fila in range (len(mat)):
        for colu in range (len(mat[fila])):
            print(mat[fila][colu], end="\t")
        print("")


mat = []
fil = int(input("cuantas filas? "))
col = int(input("cuantas columnas? "))

for fila in range(fil):
    lstfil = []
    
    for colu in range (col):
        dato = input(f"ingrese un dato para mat[{fila+1},{colu+1}]:") #f string es un nuevo tipo de string que me permite poner variables sin la ,
        lstfil.append(dato)
    mat.append(lstfil)
    
#imprimir matriz 
imprimirMatriz(mat)

