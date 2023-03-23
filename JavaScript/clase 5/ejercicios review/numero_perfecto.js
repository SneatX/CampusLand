function numeroPerfecto (max){
  for (let numero = 1 ; numero <= max ; numero++){
    var suma = 0;
    
    for (let divisor = 1 ; divisor < numero ; divisor++){
      if (numero % divisor === 0){
        var suma = suma + divisor;
      }
    }
    if (suma === numero){
      console.log(suma)
    }
  }
}

let max = Number(prompt("Ingrese el numero maximo: "));
numeroPerfecto(max)