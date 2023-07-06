//alert("Hola mundo") Vamos a hacer que el JS no se renderice primero por defecto, sino cuando queramos renderizarlo

//creamos una funcion que va a ser llamada al pulsar el boton
function pulsado(event){
    event.preventDefault() // Le dice, no hagas lo que harias por defecto (es decir no lances la peticion GET POST del formulario html)
    alert("Has hecho click")
}

window.onload = function() {

//vamos a atrapar el evento de cuando pulse el boton crear me guarde el texto que introduzco en una variable
    let boton = document.querySelector("#btnSubmit") //le pongo la id del boton que he puesto en index.html
    alert(boton)
//Al boton le pongo un metodo que escucha eventos
    boton.addEventListener("click", pulsado)//Cuando escuches el evento click, vas a ejecutar la funcion pulsado. Buscar eventos de JS

}

//IMPORTANTE QUE TODO ESTO SUCEDERA EN EL NAVEGADOR, No en el servidor.

//Para que el evento click se gestione en el JS no en el HTML, es decir, al pulsar el boton clik, no haga un methodo GET o POST hacemos la function pulsado() -->LA METEMOS AL INICIO VER LINIA 4
