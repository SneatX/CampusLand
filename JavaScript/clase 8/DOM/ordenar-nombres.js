
let vnombres = new Array(); // igual a []

function ordenar(){     //----------SOLUCION 1----------//

    let nombre = document.miformulario.nombre.value;

    vnombres.push(nombre);
    vnombres.sort();  //ordena de menor a mayor

    document.miformulario.ordenados.value = vnombres.join("\n")

    document.miformulario.nombre.value = ""

}

function ordenar2(){    //----------SOLUCION 2----------//
    let nombre = document.miformulario.nombre.value;

    let vnombre2 = document.miformulario.ordenados.value.split("\n")
    vnombre2.push(nombre)
    vnombre2.sort()

    document.miformulario.ordenados.value = vnombre2.join("\n");
    document.miformulario.nombre.value = ""
}


function flimpiarTxtArea(){
    document.miformulario.ordenados.value = "";
}