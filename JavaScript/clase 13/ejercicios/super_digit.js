function superDigit(n,k){
    let valorOriginal = String(n)
    let nString = String(n)
    for (let i = 0 ; i > k ; i++){
        nString = nString + valorOriginal
        console.log(nString)
    }
}



let n = 9875;
let k = 4;

superDigit(n,k)
