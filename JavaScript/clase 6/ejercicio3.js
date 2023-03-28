function existeVector(vector, elemento){
    for (let i = 0; i < vector.length; i++){
        if (vector[i] === elemento){
            return true;    
        }
        
    }
    return false
}




let v = ["daniela","zafiro","ana","gabriela"]
console.log(v)

let v2 = existeVector(v,"zafiro")
console.log(v2)