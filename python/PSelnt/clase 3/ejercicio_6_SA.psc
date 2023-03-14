Algoritmo tarifa_dependiendo_del_cosumo_estrato
	Escribir "Ingrese el numero de usuarios"
	Leer i
	
	Para i<-1 Hasta i Con Paso 1 Hacer
		Escribir "Ingrese su nombre:"
		Leer nombre
		
		Escribir nombre " ingrese su codigo por favor:"
		Leer codigo 
		
		Escribir nombre " ingrese su estado de cuenta:"
		Escribir "1 = Vigente"
		Escribir "2 = Suspendido"
		Leer estado
		
		
		Escribir "Ingrese su estrato, tiene que ser del 1 al 6:"
		Leer estrato
		
		Escribir "Ingrese su consumo del mes (cm^3)"
		leer consumo
		
		Si estado = 1 Entonces
			Si estrato = 1 Entonces
				tarifaBasica = 10000
			SiNo
				Si estrato = 2 Entonces
					tarifaBasica = 20000
				SiNo
					Si estrato = 3 Entonces
						tarifaBasica = 30000
					SiNo
						Si estrato = 4 Entonces
							tarifaBasica = 45000
						SiNo
							Si estrato = 5 Entonces
								tarifaBasica = 60000
							SiNo
								Si estrato = 6 Entonces
									tarifaBasica = 70000
								SiNo
									Escribir "Ingrese un dato valido"
								Fin Si
							Fin Si
						Fin Si
					Fin Si
				Fin Si
			Fin Si
			
			Escribir nombre " su tarifa basica es de: $" tarifaBasica " y su consumo esta por un valor de: $" valorConsumo " dando un total de: $" valorTotal
		SiNo
			Escribir "Su estado de cuenta esta suspendido"
		FinSi
			
			
			
		
		valorConsumo = consumo * 200
		valorTotal = valorConsumo + tarifaBasica
		
		
	
	Fin Para
FinAlgoritmo
