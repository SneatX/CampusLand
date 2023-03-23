var cedula = prompt("Ingrese la cedula, para finalizar el programa ponga 0: ");
var datos = `
<tr>
    <th>cedula</th>
    <th>nombre</th>
    <th>horas trab</th>
    <th>valor hora</th>
    <th>sal bruto</th>
    <th>EPS</th>
    <th>pension</th>
    <th>aux trans</th>
    <th>sal Neto</th>
</tr>`

while (cedula != "0"){
    const salarioMinimo = 1160000
    
    let nombre = prompt("Ingrese su nombre: ");
    let horas = Number(prompt("ingrese la cantidad de horas trabajadas: "));
    let valHora = Number(prompt("Ingrese el valor de cada hora: "));
    
    let salBruto = horas * valHora ;
    let EPS = salBruto * 0.04;
    let pension = salBruto * 0.04;
    
    if (salBruto <= salarioMinimo){
        var auxTransporte = 140606;
    }else{
        var auxTransporte = 0;
    }

    let salarioNeto = salBruto + auxTransporte - EPS - pension;

    var datos = datos + `
    <tr>
        <td>${cedula}</td>
        <td>${nombre}</td>
        <td>${horas}</td>
        <td>$${valHora}</td>
        <td>$${salBruto}</td>
        <td>$${EPS}</td>
        <td>$${pension}</td>
        <td>$${auxTransporte}</td>
        <td>$${salarioNeto}</td>
    </tr>`
    
document.getElementById("TABLA").innerHTML = datos
var cedula = prompt("Ingrese la cedula, para finalizar el programa ponga 0: ");
}