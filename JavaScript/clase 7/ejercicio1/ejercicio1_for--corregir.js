function calcularIva(valor,iva){
    let arr = []
    for(let i = 0 ; i < valor.length ; i++){
        arr.push(valor*(iva/100))
    }
    return arr
}

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