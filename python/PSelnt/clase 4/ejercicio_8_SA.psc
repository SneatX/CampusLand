Algoritmo sin_titulo
	
	Escribir "ingrese un numero"
	
	numPar = 0
	numImpar = 0
	
	Mientras num <> -1 Hacer
		
		Leer num 
		Si num % 2 = 0 Entonces
			Escribir  "El numero es par"
			numPar = numPar + 1
		SiNo
			Escribir "El numero es impar"
			numImpar = numImpar +1
		Fin Si
	Fin Mientras
	
	Escribir "hubo un total de: " numPar " numeros pares"
	Escribir "hubo un total de: " numImpar " numeros impares"
	
FinAlgoritmo
