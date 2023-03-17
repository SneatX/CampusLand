const multilinea = `
    esta es una 
    cadena con con muchas
    lineas`
console.log(multilinea);



console.log("*".repeat(15));



const str = "Hola estoy aprendiendo JavaScript en campus";
console.log(str.startsWith("Hola"));
console.log(str.startsWith("Hola", 2));
console.log(str.startsWith("Script", 27));




let isBoss = confirm("¿Eres el jefe?");
alert(isBoss); //si le pongo of el resultado es true, si le pongo cancel es false 



/*Intercambiar */

//ToString
let value = true;
alert(typeof (value));

value = String(value);
alert(typeof (value));

//ToNumber
let string = "123"
alert(typeof string);

let num = Number(string);
alert(typeof num)

let age = Number("Texto cualquiera para probar")
alert(typeof age)
alert(age)

//boolean

alert(Boolean[1]);
alert(Boolean[0]);          //todo que no sea, 0 ,null ,"", undefineld es true
alert(Boolean[""]);
alert(Boolean["a"]);


