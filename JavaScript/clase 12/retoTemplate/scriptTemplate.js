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


    //-----------fragment----------//
    const lista = document.getElementById("respuesta")
    const arrayItem = [cedula, nombre, categoria, salarioBruto, auxilioTX, bonificacion, eps, pension, salarioNeto]

    const fragment = document.createDocumentFragment()
    const template = document.querySelector("template").content

    arrayItem.forEach((item) =>{
        template.querySelector("td").textContent = item
        const clone = template.cloneNode(true)
        fragment.appendChild(clone)
    })

    lista.appendChild(fragment)
}