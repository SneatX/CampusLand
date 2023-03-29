//crea un nuevo array con todos los elementos que cumplan una condicion especificada en una funcion

let arr = [1,2,3,4,5];
let filteredArr = arr.filter(function(element){
    return element % 2 === 0;
})

console.log(filteredArr)