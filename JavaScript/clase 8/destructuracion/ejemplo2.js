let v = ["uno" , "dos" , "tres" , "cuatro"]
let x = ["lun" , "mar" , "mier", "juev" , "vier"]

function prueba([param1, param2, ...otros1] , [param3, ...otros2]){
    console.log(`primera entrada ${param1} ${param2} ${otros1}`)
    console.log(`primera entrada ${param3} ${otros2}`)
}

prueba(v,x)