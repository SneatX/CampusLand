const buildFila = (cedula, nombre, categoria, salarioBruto, auxilioTX, bonificaciones, EPS, pension, salarioNeto) => {
    return `
    <tr>
    <td>${cedula}</td>
    <td>${nombre}</td>
    <td>${categoria}</td>
    <td>${salarioBruto}</td>
    <td>${auxilioTX}</td>
    <td>${bonificaciones}</td>
    <td>${EPS}</td>
    <td>${pension}</td>
    <td>${salarioNeto}</td>
    `
}
const buildFila2 = (nota, espacio, salarioBruto, auxilioTX, bonificacion, eps, pension, salarioNeto) => {
    return `
    <tr>
    <td>${nota}</td>
    <td>${espacio}</td>
    <td>${espacio}</td>
    <td>${salarioBruto}</td>
    <td>${auxilioTX}</td>
    <td>${bonificacion}</td>
    <td>${eps}</td>
    <td>${pension}</td>
    <td style="color: red; font-size: 2em;">${salarioNeto}</td>
    `
}

const buildFila3 = (cantEmpleados, nEmpleadoMenos, empleadoMENOS, promedio, nEmpleadoMas, empleadoMAS, salarioNetoTotal) => {
    return `
    <tr>
        <td>${cantEmpleados}</td>
        <td>${nEmpleadoMenos} <br> (${empleadoMENOS})</td>
        <td>${promedio}</td>
        <td>${nEmpleadoMas} <br> (${empleadoMAS})</td>
        <td style="color: red; font-size: 2em;">${salarioNetoTotal}</td>
    </tr>
    `
}


//Totales tabla 1, fila 2
let salarioBrutoTotal = 0
let auxilioTXTotal = 0
let bonificacionTotal = 0
let epsTotal = 0
let pensionTotal = 0
let salarioNetoTotal = 0

//Totales tabla 2
let cantEmpleados = 0
let empleadoMAS = 0
let nombreEmpleadoMas
let empleadoMENOS = Infinity
let nombreEmpleadoMenos

let strHTML = ""

function tabla() {
    let cedula = document.miFormulario.cedula.value
    let nombre = document.miFormulario.nombre.value
    let categoria = document.miFormulario.categoria.value

    let salarioBruto
    let auxilioTX = 0
    let bonificacion

    if (categoria === "Auxiliar A") {
        salarioBruto = 1160000
        auxilioTX = 400000
        bonificacion = 100000
    }
    else if (categoria === "Auxiliar B") {
        salarioBruto = (1.2 * 1160000)
        auxilioTX = 400000
        bonificacion = 100000
    }
    else if (categoria === "Tecnico A") {
        salarioBruto = (1.5 * 1160000)
        bonificacion = 150000
    }
    else if (categoria === "Tecnico B") {
        salarioBruto = (2 * 1160000)
        bonificacion = 150000
    }
    else if (categoria === "Profesional A") {
        salarioBruto = (2.5 * 1160000)
        bonificacion = 200000
    }
    else if (categoria === "Profesional B") {
        salarioBruto = (3 * 1160000)
        bonificacion = 250000
    }
    else if (categoria === "Director A") {
        salarioBruto = (4 * 1160000)
        bonificacion = 500000
    }
    else if (categoria === "Director B") {
        salarioBruto = (4.5 * 1160000)
        bonificacion = 1000000
    }
    else if (categoria === "Gerente Departamento") {
        salarioBruto = (6 * 1160000)
        bonificacion = 2000000
    }
    else if (categoria === "Gerente General") {
        salarioBruto = (10 * 1160000)
        bonificacion = 5000000
    }

    let eps = salarioBruto * 0.04
    let pension = salarioBruto * 0.04
    let salarioNeto = salarioBruto + auxilioTX + bonificacion - eps - pension

    if (categoria ==="Auxiliar A" || categoria ==="Auxiliar B" || categoria ==="Tecnico A" || categoria ==="Tecnico B" || categoria ==="Profesional A" || categoria ==="Profesional B") {
        if (salarioNeto > empleadoMAS) {
            nombreEmpleadoMas = nombre
            empleadoMAS = salarioNeto
        }
        if (salarioNeto < empleadoMENOS) {
            nombreEmpleadoMenos = nombre
            empleadoMENOS = salarioNeto
        }
    }

    //Calculos totales tabla 1, fila 2
    salarioBrutoTotal += salarioBruto
    auxilioTXTotal += auxilioTX
    bonificacionTotal += bonificacion
    epsTotal += eps
    pensionTotal += pension
    salarioNetoTotal += salarioNeto


    //Calculos totales tabla 2
    cantEmpleados += 1
    let promedio = salarioNetoTotal / cantEmpleados

    strHTML += buildFila(cedula, nombre, categoria, salarioBruto, auxilioTX, bonificacion, eps, pension, salarioNeto)

    document.getElementById("respuesta").innerHTML = strHTML
    document.getElementById("resultadoFinal").innerHTML = buildFila2("Suma total", "---", salarioBrutoTotal, auxilioTXTotal, bonificacionTotal, epsTotal, pensionTotal, salarioNetoTotal)
    document.getElementById("tablaFinal").innerHTML = buildFila3(cantEmpleados, nombreEmpleadoMenos, empleadoMENOS, promedio, nombreEmpleadoMas, empleadoMAS, salarioNetoTotal)

}
