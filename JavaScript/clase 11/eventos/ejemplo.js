function mostrarMensaje(){
    console.log("Se ha dado un clic en el titulo")
}

const titulo = document.querySelector("h1")
const parrafo = document.querySelector("p")


let contador = 0
titulo.addEventListener("click",mostrarMensaje)
parrafo.addEventListener("mouseover",() => {
    
    parrafo.textContent = "haz pasado " + (++contador) + " veces"
})

parrafo.addEventListener("mouseout" , () =>{
    parrafo.textContent = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Distinctio magnam excepturi, dolorem odio et, alias temporibus eaque deleniti recusandae, nemo odit reprehenderit! Deserunt, et accusantium quas ducimus ipsa distinctio accusamus."
})
