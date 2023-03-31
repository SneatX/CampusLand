function buildFila(){
    return `<tr>
    <td>${nombre}</td>
    <td>${lunes}</td>
    <td>${martes}</td>
    <td>${miercoles}</td>
    <td>${jueves}</td>
    <td>${viernes}</td>
    <td>${sabado}</td>
    <td>${domingo}</td>
</tr>`
}

let arrNombres = []
let arrLunes = []
let arrMartes = []
let arrMiercoles = []
let arrJueves = []
let arrViernes = []
let arrSabado = []



function datos(){
    let nombre = document.miFormulario.nombre.value;
    alert(nombre)
}

function apoyo(){
    alert("Voy bien")
}