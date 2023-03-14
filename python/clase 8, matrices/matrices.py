##############Estructa de datos#########
##### listas: 
#0[ ][ ][ ][ ]
#1[ ][ ][ ][ ]
#2[ ][ ][ ][ ]
#3[ ][ ][ ][ ]
#  0  1  2  3

#para llamar los datos se llama primero fila y luego columna y empieza a contar desde 0


def imprimirMatriz(mat):
    for fila in range (len(mat)):
        for colu in range (len(mat[fila])):
            print(mat[fila][colu], end="\t")
        print("")
    
    
mat = [[3,4,7],
       [2,8,10],
       [1,5,6],
       [13,15,17]]

#impresion
#print("mat[2,2] = " , mat[2][2])

#modificacion por el usuario
#mat[1][0] = int(input("Ingrese un numero "))
#print("mat[1,0] = " , mat[1][0])

#imprimir una matriz
imprimirMatriz(mat)
