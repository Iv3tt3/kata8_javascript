from mi_cartera_js import app

@app.route("/")
def index():
    return "Flask rulando"