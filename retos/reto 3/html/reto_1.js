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
const buildFila2 = (nota, espacio ,salarioBruto, auxilioTX, bonificacion, eps, pension, salarioNeto) => {
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
    <td>${salarioNeto}</td>
    `

}






let salarioBrutoTotal = 0
let auxilioTXTotal = 0
let bonificacionTotal = 0
let epsTotal = 0
let pensionTotal = 0
let salarioNetoTotal = 0

function tabla() {
    let cedula = document.miFormulario.cedula.value
    let nombre = document.miFormulario.nombre.value
    let categoria = document.miFormulario.categoria.value

    let strHTML = ""
    let salarioBruto
    let auxilioTX = 0
    let bonificacion
    let empleadoMAS = 0
    let nEmpleadoMas
    let empleadoMENOS = Infinity
    let nEmpleadoMenos

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

    if (salarioNeto < empleadoMENOS) {
        empleadoMENOS = salarioNeto
        nEmpleadoMenos = nombre
    }
    if (salarioNeto > empleadoMAS) {
        empleadoMAS = salarioNeto
        nEmpleadoMas = nombre

    }

    salarioBrutoTotal += salarioBruto
    auxilioTXTotal += auxilioTX
    bonificacionTotal += bonificacion
    epsTotal += eps
    pensionTotal += pension
    salarioNetoTotal += salarioNeto


    strHTML += buildFila(cedula, nombre, categoria, salarioBruto, auxilioTX, bonificacion, eps, pension, salarioNeto)

    strHTML += buildFila2("Suma total","---",salarioBrutoTotal, auxilioTXTotal, bonificacionTotal, epsTotal, pensionTotal, salarioNetoTotal)

    return document.getElementById("respuesta").innerHTML = strHTML
}
