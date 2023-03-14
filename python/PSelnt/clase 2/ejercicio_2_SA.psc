
Algoritmo Subcidio_transporte
	Escribir "Ingrese su nombre por favor"
	Leer nombre
	
	Escribir nombre " ingrese su salario"
	Leer sueldo
	
	Si sueldo<=1200000 Entonces
		Escribir nombre " recibira un subsidio de $120.000"

	SiNo
		Escribir nombre " no recibira subsidio"
	Fin Si
	
	
	Escribir "Le gustaria saber cual sera su nomina final? (Y/F) "
	Leer respuesta	
	Si respuesta == "Y" Entonces
		Escribir nombre " su salario final sera de: " sueldo + 120000 
	SiNo
		Escribir "Un placer atenderlo"
	Fin Si

	
FinAlgoritmo
