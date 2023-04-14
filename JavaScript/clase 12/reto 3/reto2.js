function compareTriplets( matrizAlice , matrizBob){
    let puntosTotales = [0 , 0]
    for (let i = 0; i < 3 ; i++){
        if(matrizAlice[i] > matrizBob[i])
            puntosTotales[0] += 1
        
        else if(matrizAlice[i] < matrizBob[i])
            puntosTotales[1] += 1
    }
    console.log(puntosTotales)
}


matrizAlice = [2 , 2 , 3]
matrizBob   = [3 , 2 , 2]

compareTriplets(matrizAlice , matrizBob)


