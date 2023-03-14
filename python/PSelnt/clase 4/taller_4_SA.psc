Algoritmo comision_ventas_por_categoria
	Escribir "Ingrese su cedula: "
	Leer cedula
	
	ventas_mes = 0
	total_comision = 0
	Mientras cedula <> -1 Hacer
		
		Escribir "Ingrese el tipo de vendedor que es:"
		Escribir " 1 = Puerta a puerta"
		Escribir " 2 = Telemercado"
		Escribir " 3 = Ejecutivo de ventas"
		leer tipo_vendedor
		Escribir"Ingrese el valor de las ventas realizadas durante este mes: "
		leer valor_vendido
		
		
		Si tipo_vendedor = 1 Entonces
			comision = valor_vendido * 0.2
		SiNo
			Si tipo_vendedor = 2 Entonces
				comision = valor_vendido * 0.15
			SiNo
					comision = valor_vendido * 0.25
			Fin Si
		Fin Si
		
		Escribir "Valor a pagar por comision: $" comision
		
		ventas_mes = ventas_mes + valor_vendido
		total_comision = total_comision + comision
		
		Escribir "Ingrese su cedula: "
		Leer cedula

	Fin Mientras
	
	Escribir "El total de ventas es: $" ventas_mes 
	Escribir "El total de comisiones es: $" total_comision
	
	
FinAlgoritmo
