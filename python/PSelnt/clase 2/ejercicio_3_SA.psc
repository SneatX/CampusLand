Algoritmo nota_cuantitativa_a_cualitativa
	Escribir "Ingrese el nombre del estudiante: "
	Leer nombre
	
	Escribir "Ingrese la calificacion cuantitativa"
	Leer notaT
	
	Si notaT<=59 Entonces
		notaL= "D"
	SiNo
		Si notaT<=79 Entonces
			notaL = "C"
		SiNo
			Si notaT<=89 Entonces
				notaL = "B"
			SiNo
				notaL = "A"
			Fin Si
		Fin Si
	Fin Si
	
	Escribir "La nota de " nombre " es de " notaT " de manera cuantitativa y " notaL " de manera cualitativa"
FinAlgoritmo
