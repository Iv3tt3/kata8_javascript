var pet_todos = new XMLHttpRequest() /*Creamos el objeto HMLHttpRequest que es un manejador de peticiconnes. Es lo mismo que el requests.get de la kata APicoin. la peticion, que hace la peticion a la api de todos. Como queremos hacerla nada mas cargar hacemos: pet_todos.open*/


function appendCell(row, data){
    let the_cell = document.createElement("td") 
    the_cell.innerHTML = data
    row.appendChild(the_cell)
}


function muestraTodos() {
    let pedido = this.responseText
    /*Este this es el objeto HttpRequest. Aqui asignamos a pedido la lista de diccionarios movements de la ruta api/v1/all, gracias al metodo responseText del objeto this
    1 elegir el padre que es la table del index, por lo que le aado una id
    2 transformar el pedido en objeto de Json
    3 para cada objeot de la lista de movimientos, crear una fila html en el DOMException y anadir la fila a la table el padre */
    let data = JSON.parse(pedido) //Aqui parseo el JSON
    let the_father = document.querySelector("#table_movements")
    
    for (let i=0; i< data.length; i++) {//El for empieza en el elemento 0 de data, luego hae un for hasta la longitud de data y luego mes umas 1 por cada vez que pase por el for
        let the_row = document.createElement("tr") //Creamos una fila
        
        appendCell(the_row, data[i].date)
        appendCell(the_row, data[i].amount)
        appendCell(the_row, data[i].abstract)
        appendCell(the_row, data[i].currency)
        
        /*let the_cell = document.createElement("td") //Creamos la celda. Aqui ponemos el led porque creamos la variable. Luego ya no lo usamos, sino que sobrescribimos la variable
        the_cell.innerHTML = data[i].date //Anadimos el campo a la celda
        the_row.appendChild(the_cell) //Aqui cuelga la celda y se anade al padre row
        
        the_cell = document.createElement("td")
        the_cell.innerHTML = data[i].abstract
        the_row.appendChild(the_cell) 

        the_cell = document.createElement("td")
        the_cell.innerHTML = data[i].amount
        the_row.appendChild(the_cell)

        the_cell = document.createElement("td")
        the_cell.innerHTML = data[i].currency
        the_row.appendChild(the_cell)*/

        the_father.appendChild(the_row) //Aqui cuelga la row y se anade al padre father
    }
}

window.onload = function() {
    pet_todos.open("GET", "api/v1/all") //Elige el tipo de peticion y a quien se la voy a hacer. Aqui hacemos la peticion nada mas cargar la pagina
    pet_todos.addEventListener("load", muestraTodos) //Eliges el evento a elegir y lo que se va a hacer. Aqui decimos que espere a que se haya hecho la carga, con el load. Una vez cargado, llama a muestraTodos. Pero aun no estamos haciendo la peticion, estamos configurando.
    
    pet_todos.send() //Y en este momento se manda la peticion al servidor. Esto es la accion de pedir
}