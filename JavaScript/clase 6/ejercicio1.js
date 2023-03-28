let calcularValorMayor = (vector) => {
    if(vector.legth === 0){
        return null
    }

    let mayor = vector[0]
    for (let i = 1 ; i < vector.length ; i++){
        if (vector[i] > mayor){
            mayor = vector[i]
        }
    }
    return mayor
}

let v = [2,5,6,7,-1]
console.log(v)
let v2 = calcularValorMayor(v)
console.log(v2)