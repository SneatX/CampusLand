//crea un nuevo array con los resultados de llamar a una funcion para cada elemento del array

// la diferencia del foreach es que este me genera el resultado en un nuevo array

let arr = [1,2,3];
let mappedArr = arr.map(function(element){
    return element *2;
})

console.log(mappedArr)