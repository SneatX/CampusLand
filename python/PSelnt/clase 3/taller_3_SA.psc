Algoritmo valor_a_pagar_docentes
	
	Escribir "Ingrese el numero de usuarios"
	Leer i
	
	cantidad_docentes = 0
	valor_total_pagar = 0
	
	
	Para i<-1 Hasta i Con Paso 1 Hacer
		
		Escribir "Ingrese su nombre:"
		leer nombre
		
		Escribir nombre " Ingrese su documento de identidad:"
		Leer id
		
		Escribir "El valor de las horas laborales dependera de su categoria: "
		Escribir "A = 25.000"
		Escribir "B = 35.000"
		Escribir "C = 50.000"
		Escribir nombre " ingrese la letra de la categoria a la cual pertenece"
		Leer categoria
		
		Escribir nombre " ingrese la cantidad de horas laborales que realizo"
		Leer horasHechas
		
		Si categoria = "A" Entonces
			valorHoras = 25000
		SiNo
			Si categoria = "B" Entonces
				
				valorHoras = 35000
			SiNo
				Si categoria = "C" Entonces
					valorHoras = 50000
				SiNo
					Escribir "Ingrese un dato valido"
				Fin Si
			Fin Si
		Fin Si
		
		
		pagaProfe = valorHoras * horasHechas
		valor_total_pagar = pagaProfe + valor_total_pagar
		cantidad_docentes = cantidad_docentes + 1
		Escribir "El profesor " nombre " recibira una paga de :$" pagaProfe 
		Escribir " "
		
		
	Fin Para
	
	Escribir "Con un total de " cantidad_docentes " docentes."
	Escribir "El valor total a pagar a todos los docentes es de: $" valor_total_pagar
	
	
FinAlgoritmo
