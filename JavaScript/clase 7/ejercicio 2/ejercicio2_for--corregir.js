function filterByLength(vector){
    let respuesta = []
    
    for(let i = 0 ; i < vector.length ; i++){
        if (vector[i].length >= 4){
            respuesta.push(vector[i])
        }
    }
    return arr
}

let arr = ["hola","papa","xd"]


console.log(filterByLength(arr))