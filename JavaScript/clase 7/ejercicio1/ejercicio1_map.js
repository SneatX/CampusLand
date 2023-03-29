/*# Enunciado

Tienes un array de objetos que representan datos de productos con los siguientes atributos:

* name
* price
* stock

Tu reto hace una función que devuelva un nuevo vector con el valor de los impuestos. Debes tener en cuenta que como resultado se debe dejar un valor entero, **sin decimales**.

La función recibe como parámetros un vector y el impuesto a aplicar.

Por ejemplo si aplicamos el **19%** de impuestos para un producto con precio de **$1000** el resultado de los "taxes" será **$190**, o para un producto con precio de $656 el resultado de los "taxes" será **$124**.*/

function calcularIva(vector, iva) {
    let arr = vector.map(function (valor) {               //usando una funcion normal
        return Math.round(valor * (iva/100));
    })
    return arr
}

const porcentaje = function(vector, iva){
    return vector.map(e => Math.round(e * (iva/100)))          //usando una funcion anonima
}

const mimap = (vector, iva) => vector.map(e => Math.round(e*(iva/100)))  //usando una funcion flecha



let arr = []
let N = Number(prompt("Ingrese un valor para aplicar el iva, para finalizar ponga 0"))
while (N != 0){
    arr.push(N)
    N = Number(prompt("Ingrese un valor para aplicar el iva"))
}

let iva
do{
    iva = Number(prompt("Ingrese el iva"))
}while (iva <= 0)


console.log(calcularIva(arr, iva))
console.log(porcentaje(arr, iva))
console.log(mimap(arr, iva))
