
let incorrecto = 0
let correcto = 0
let palabras = ["auto", "avion", "procesador", "reir", "paleta", "elefante", "leon", "brazo", "padre", "lupa", "gordo", "silla", "casco", "ocho", "estrella", "hielo", "trompeta", "hojas", "caballo", "tomate"];
let palAleatoria = palabras[Math.floor(Math.random() * palabras.length)]

function ahorcado() {

    let letra = document.getElementById("letra").value
    
    console.log(palAleatoria)

    if (letra.length === 1) {
        let resultado = palAleatoria.indexOf(letra)
        if (resultado != -1) {
            correcto++
            palAleatoria = palAleatoria.replace(letra, " ")
        }
        else {
            incorrecto++ 
        }

        let resultado2 = palAleatoria.indexOf(letra)
        if(resultado2 != -1){
            palAleatoria = palAleatoria.replace(letra, " ")
        }
    }
    console.log("correctos: ", correcto)
    console.log("incorrectos: ", incorrecto)
    console.log(palAleatoria)
}
