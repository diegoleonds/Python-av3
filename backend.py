from config import * 
from modelo import Contato 
from flask import request

@app.route("/listar_contatos")
def getContatos():
    contatos = db.session.query(Contato).all()
    contatos_em_json = [ x.json() for x in contatos ]
    resposta = jsonify(contatos_em_json)

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)