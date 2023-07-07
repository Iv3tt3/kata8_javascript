from mi_cartera_js import app
from flask import render_template
from mi_cartera_js.models import MovemenetDAOSqlite

dao = MovemenetDAOSqlite(app.config["PATH_SQLITE"]) #Es lo mismo que dao = MovemenetDAOSqlite(app.config.get["PATH_SQLITE"]) aunque esta forma si no encuentra la clave en config te crea una bd None

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/v1/all") #Añadimos la ruta que nos parece con la version y el nombre de all
def todos():
    movements = dao.get_all()
    return movements