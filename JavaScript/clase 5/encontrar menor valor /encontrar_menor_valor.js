function menorValor(){
    let cantNum = Number(prompt("Ingrese la cantidad de numeros a calcular: "));

    let menor = Infinity;
    for(let i = 0; i < cantNum; i++){
        let num = Number(prompt("Ingrese un numero: "));
        if (num <menor) menor = num;
    }

    return menor;
}

console.log(menorValor());