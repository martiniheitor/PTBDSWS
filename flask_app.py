from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# Home
@app.route("/")
def index():
    current_time = datetime.utcnow()
    return render_template("index.html", current_time=current_time)

# Identificação
@app.route("/user/<name>/<prontuario>/<instituicao>")
def identificacao(name, prontuario, instituicao):
    return render_template(
        "user.html",
        name=name,
        prontuario=prontuario,
        instituicao=instituicao,
    )

# Contexto da requisição
@app.route("/contextorequisicao/<name>")
def contexto(name):
    user_agent = request.headers.get("User-Agent", "desconhecido")
    remote_ip = request.remote_addr or "desconhecido"
    host = request.host or "desconhecido"
    return render_template(
        "contexto.html",
        name=name,
        user_agent=user_agent,
        remote_ip=remote_ip,
        host=host,
    )

if __name__ == "__main__":
    app.run(debug=True)
