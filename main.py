from flask import Flask, render_template

app = Flask(__name__)

# criar primeira pagina do site
# route -> meusite.com/
# funçao -> o que será exibido no site
# templates

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/voltar")
def voltar():
    return render_template("index.html")

@app.route("/ausentes", methods=["POST"])
def ausentes():
    return render_template("ausentes.html")
@app.route("/turmas", methods=["POST"])
def turmas():
    return render_template("turmas.html")

@app.route("/ferias", methods=["POST"])
def ferias():
    return render_template("ferias.html")

@app.route("/incluirAusencia", methods=["POST"])
def incluirAusencia():
    return render_template("incluirAusencia.html")

@app.route("/erro", methods=["POST"])
def erro():
    return render_template("erro.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("erro.html"), 404

# colocar site no ar
if __name__=="__main__":
    app.run(debug=True)

# servidor heroku