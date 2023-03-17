/*---------------------------------------------------------------------*/
alert("hola mundo")   /*muestra una alerta al entrar a la pagina*/
alert("xd")
/*---------------------------------------------------------------------*/
/*se hacen comentarios como en css*/
/*---------------------------------------------------------------------*/


/*-------------------------tipos de variables------------------------- */
/*variables tipo string*/
let user = "jhon", age = "17", mensaje = "hola" /*puedo escibir varias variables en una sola linea*/

let user2 = "jhon",
    age2 = "17",     /*algunas personas tambien las llaman asi, o simplemente les ponen el var a cada una en cada linea, pero es lo mismo*/
    mensaje2 = "hola"



/*----------variables tipo number----------*/
let n = 123     //no pueden representar un numero mayor a 2^53-1 (9007199254740991) y lo mismo para negativos, puede almacenar datos mas grandes pero habra errores de precision
n = 123.456     /*las variables tipo number representan tanto a enteros como a flotanter*/
 


/*----------Infinity----------*/
infinity = 1/0 /*es un valor especial que es mayor que cualquier otro numero, se obtiene de la siguiente division  */
console.log(infinity)
alert(1/0);



/*----------variables tipo string----------*/
//es una cadena de caracteres y debe colocarse entre comillas 
let str = "hola";
let str2 = 'las comillas simpres tambien estan bien';
let phrase = `se puede incrustar otro ${str}`; 
//las comillas invertidas (backticks) se hacen con ctrl + shift + u + 60 y tienen mas funciones que las sencillas y dobles
//nos permiten incrustar variables y expresiones en una cadena de caracteres encerrandolos en ${...}

let nombre ="jhon";
//incrustar una variable
alert(`hola, ${nombre}!`); //hola, jhon!
//incrustar una expresion 
alert(`el resultado de 4 + 7 es:  ${4 + 7}`); //el resultado de 4 + 7 es: 11



/*----------variables tipo boolean----------*/
/*solo tiene dos valores, true or false
se utiliza para almacenar valores de si/no
true significa: si / correcto / verdadero
false significa: no / incorrecto / falso*/

let nameFieldChecked = true; //si, el campo name esta marcado
let ageFieldChecked = false; //no, el campo age no esta marcado

let isGreater = 4 >1;
alert(isGreater); //true (el resultado de la comparacion es "si")



/*----------variables tipo null----------*/
let edad = null; // este codigo demuestra que la edad es desconocida por alguna razon
/* es una referencia a objeto inexistente, representa "nada", "vacio" o "valor desconocido"*/



/*----------variables tipo undefined----------*/
let codigo;
alert(codigo) // muestra, "undefined" ya que no esta definido   
/*hace un tipo igual que null, aparece cuando una variable no es asignada y significa "valor no asignado"*/ 









/*-------------------------diferencias entre var y let------------------------- */

/*las variables con var pueden tener a la funcion como entorno de visibilidad, o bien ser globales. su visibilidad atraviesa bloques*/
if (true){
    var test = true; //uso de "var"
}

alert (test) //true, porque la variable vive fuera del if


if (true){
    let test2 = true; //uso de "let"
}

alert (test2) //ReferenceError: test no esta definido, muere fuera del if 


/*var tolera re declaraciones */
var hola = 123;
var hola = 432;

/*let no las tolera, declarar la misma variable dos veces con let en un entorno es un error */
let hola2 = 432;
// let hola2 = 234;