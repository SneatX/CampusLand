// reduce el array a un unico valor mediante la ejecucion de una funcion para cada elemento del array

let arr = [1,2,3,4,5]
let sum = arr.reduce(function(accumulator,currentValue){
    return accumulator + currentValue
})
console.log(sum)



let arr2 = [5,10,2,8,3];
let maxNumber = arr2.reduce(function(accumulator, currentValue){
    return Math.max(accumulator, currentValue)
});
console.log(maxNumber)


let arr3 = [5,10,2,8,3];
let sum2 = arr3.reduce(function(accumulator,currentValue){
    return accumulator + currentValue
})
let average = sum2 / arr3.length
console.log(average)