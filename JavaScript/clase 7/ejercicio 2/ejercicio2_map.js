const filterByLength = vector => vector.map(element => {
    if(element.length >= 4){
        return element
    }
})


vector = ["hola","adi","palabra","pap"]
console.log(filterByLength(vector))