const readline = require('readline-sync');

function calculateChargues(horas){
  if (horas <= 2){
    var valor = 2
  }
  else if(horas > 2 && horas < 18){
    var valor = ((horas-2) * 0.5) +2
  }
  else{
    var valor = 10
  }

  console.log(valor)
  return valor;
}
//--------------------------------------------------------
let totalDia = 0

do{
  horas = Number(readline.question("Ingrese el numero de horas, para finalizar ingrese 0: "));
  if(horas > 24){
    console.log("El maximo de horas diarias son de 24")
  }
}while(horas > 24)

while (horas != 0){
  
  totalDia = totalDia + calculateChargues(horas)
  
  do{
    horas = Number(readline.question("Ingrese el numero de horas, para finalizar ingrese 0: "));
    if(horas > 24){
      console.log("El maximo de horas diarias son de 24")
    }
}while(horas > 24)
  
}
console.log("total dia: $" + totalDia + ".00")
