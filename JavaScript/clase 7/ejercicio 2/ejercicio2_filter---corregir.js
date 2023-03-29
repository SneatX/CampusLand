const filterByLength = vector.filter(function(element){
    return element.length >= 4;
})

let vector = ["hola","adi","palabra","pap"]
console.log(filterByLength(vector))