from flask import Flask, render_template, request, redirect
import sqlite3
from init_db import conectar

app = Flask(__name__)



@app.route("/")
def home():
    return redirect("/usuarios")


# LISTAR
@app.route("/usuarios")
def usuarios():
    conn = conectar()
    cursor = conn.cursor()
    pesquisa = request.args.get("pesquisa")
    if pesquisa:
        cursor.execute("""
        SELECT * FROM usuarios WHERE nome LIKE ? OR cpf LIKE ? OR email LIKE ?
        ORDER BY nome """,   (f"%{pesquisa}%", f"%{pesquisa}%", f"%{pesquisa}%"))
    else:
        cursor.execute(""" SELECT * FROM usuarios ORDER BY nome """)
    usuarios = cursor.fetchall()
    conn.close()

    return render_template(
        "usuarios.html",
        usuarios=usuarios
    )


# NOVO
@app.route("/usuarios/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO usuarios (nome, senha, cpf, email, perfil)
        VALUES (?, ?, ?, ?, ?) """,
        (request.form["nome"], request.form["senha"], request.form["cpf"],
            request.form["email"], request.form["perfil"]))
        conn.commit()
        conn.close()
        return redirect("/usuarios")
    return render_template("usuario_form.html", usuario=None)


# EDITAR
@app.route("/usuarios/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conn = conectar()
    cursor = conn.cursor()
    if request.method == "POST":
        cursor.execute(""" UPDATE usuarios SET nome=?, senha=?,cpf=?,
            email=?, perfil=? WHERE id_usuario=? """,
        (request.form["nome"], request.form["senha"], request.form["cpf"],
            request.form["email"], request.form["perfil"], id))
        conn.commit()
        conn.close()
        return redirect("/usuarios")

    cursor.execute("SELECT * FROM usuarios WHERE id_usuario=?",(id,))
    usuario = cursor.fetchone()
    conn.close()
    return render_template("usuario_form.html", usuario=usuario)


# EXCLUIR
@app.route("/usuarios/excluir/<int:id>")
def excluir(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id_usuario=?",(id,))
    conn.commit()
    conn.close()
    return redirect("/usuarios")


if __name__ == "__main__":
    app.run(debug=True)