var el_ultimo

function pulsado(event){
    event.preventDefault() 
    let the_father = document.querySelector("#contenido")
    let the_paragraph = document.createElemennt("p") 
    
    let input = document.querySelector("#texto")
    the_paragraph.innerHTML = input.value 

    the_father.appendChild(the_paragraph)

    el_ultimo = the_paragraph
}

function borrado(event){
    event.preventDefault() 
    let the_father = document.querySelector("#contenido")
    if (el_ultimo){
        the_father.removeChild(el_ultimo)
    } //En este if le decimos que solo elimino el ultimo si hay algo en la lista, si esta vacia no haga nada
}

window.onload = function() {
    let boton = document.querySelector("#btnSubmit") 
    boton.addEventListener("click", pulsado)

    let botonDelete = document.querySelector("#btnDelete") //Si no añadiesemos esto, llamaria el boton de la forma normal por HTML y te iria al servidor
    botonDelete.addEventListener("click", borrado)
}