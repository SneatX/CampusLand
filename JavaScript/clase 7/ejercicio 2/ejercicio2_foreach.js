function filterByLength(vector){
    let respuesta = []
    vector.forEach(function(element){
        if (element.length >= 4){
            respuesta.push(element)
        }
    })
    return respuesta
}

vector = ["hola","adi","palabra","pap"]
console.log(filterByLength(vector))