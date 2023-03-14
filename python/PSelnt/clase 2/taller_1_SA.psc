Algoritmo tarifa_servicio_estrato
	Escribir "Ingrese su nombre"
	Leer nombre
	
	Escribir "Ingrese el estrato al cual pertenece"
	Leer estrato 
	
	Si estrato = 1 Entonces
		tarifa=10000
	SiNo
		Si estrato = 2 Entonces
			tarifa = 15000
		SiNo
			Si estrato = 3 Entonces
				tarifa = 30000 
			SiNo
				Si estrato =  4 Entonces
					tarifa = 50000
				SiNo
					tarifa = 60000
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	
	Escribir "el/la ciudadan@ " nombre " tiene una tarifa de " tarifa "."
	
FinAlgoritmo
