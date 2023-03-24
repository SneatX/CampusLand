const prodImpares = function(ini, fin){
    let prod = 1;

    console.log("NUM t\ t\ PRODUCTO");
    console.log("-".repeat(40));


    for (let i = ini ; i <= fin ; i++){
        /*prod *=(i%2 !== 0) ? i : 1;*/ // es un if resumido, si es true devuelve la izquierda de los dos puntos, si es false devuelve la derecha de los dos puntos
        if(i % 2 !== 0 ){
            prod *= i;  
            console.log(`${i} \t\t\t ${prod} `)      
        }
        
    }

    return prod;
}

console.log(prodImpares(1, 15));