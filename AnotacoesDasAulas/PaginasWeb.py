"""
Aplicações WEB - Flask
Microframework python que permite a criação de aplicações web facil
"""

from flask import Flask
app = Flask(__name__) #Cria a instância principal de sua aplicação
@app.route("/")

def home():
    return "Olá, mundo! Flask funcionando"

if __name__ == "__main__":
    app.run(debug=True)

    #Ele fala ali no terminal: Running on http://127.0.0.1:5000
    #O que são portas e endereços de máquina local?

#Para programar as páginas em HTML o flask usa uma pasta chamda templates.
#Estrutura do projeto recomendada

#Meu_projeto/
#
# - app.py
# - templates/
#        # - index.html
#        # - usuario.html   
# 
# - static/
#       # - style.css
#       # - script.js

#Para comunicações com apicações web -- para passar parâmetros por exemplo --, pode se usar métodos posts (internos), ou gets (por URL)
#Cadastro por exemplo, geralmente é feito por POST pois contem senha.