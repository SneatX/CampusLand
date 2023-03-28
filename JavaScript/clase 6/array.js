let casa = ["1BHK","2BHK","3BHK","4BHK"];   //asi se crea un array normal

let house = new Array(10,20,30,40,50);      //esta es la otra manera

let house1 = new Array(5);                  //esta es otra donde se crea con un tamaño pero vacia


function elevarImparesCuadrado(vector){
    let [...vector2] = vector; //asi se crea una copia del vector vector2 = vector no sirve
    for(let i=0 ; i<vector2.length ; i++ ){
        if(vector2[i] % 2 !== 0){
            vector2[i] = vector2[i] ** 2
        }
    }
    return vector2;
}

let v = [2,5,6,7,8,9,0,-1]
console.log(v);
let v2 = elevarImparesCuadrado(v);
console.log(v2);
console.log(v)

