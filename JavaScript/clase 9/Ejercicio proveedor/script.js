function buildFila(proveedor, producto, precio2022, precio2023) {
    return `<tr>
    <td>${proveedor}</td>
    <td>${producto}</td>
    <td>${precio2022}</td>
    <td>${precio2023}</td>
</tr>`
}
function buildFila2(proveedor, producto, precio2022, precio2023, incremento) {
    return `<tr>
    <td>${proveedor}</td>
    <td>${producto}</td>
    <td>${precio2022}</td>
    <td>${precio2023}</td>
    <td>${incremento}</td>
</tr>`
}

function tabla1() {
    let strHTML = ""
    let strHTML2 = ""
    let incremento = 0
    let proveedorMenor 
    let productoMenor
    let precio2022Menor
    let precio2023Menor
    let valor = Infinity
    

    let cantidad = prompt("Ingrese la cantidad de proveedores: ")

    
    for (i = 0; i < cantidad; i++) {
        let proveedor = prompt("Ingrese el nombre del proveedor:");
        let producto = prompt("Ingrese el nombre del producto: ");
        let precio2022 = Number(prompt("Ingrese el precio en 2022: "));
        let precio2023 = Number(prompt("Ingrese el precio en 2023: "));

        let valor2 = precio2023/precio2022
        console.log("HOLAAAAAAAAAAAAAAA" + valor2)
        if (valor2 < valor){
            proveedorMenor = proveedor
            productoMenor = producto
            precio2022Menor = precio2022
            precio2023Menor = precio2023
            incremento = precio2023/precio2022
            valor = valor2
        }

        strHTML = strHTML + buildFila(proveedor, producto, precio2022, precio2023) 

        strHTML2 = buildFila2(proveedorMenor, productoMenor, precio2022Menor, precio2023Menor, incremento)


    }

    document.getElementById("respuesta").innerHTML = strHTML
    document.getElementById("respuesta2").innerHTML = strHTML2

}