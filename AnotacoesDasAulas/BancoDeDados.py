"""

Aula de hoje é sobre banco de dados - Vamos utilizar o SQLite

27/05/2026

"""

#Se der algum erro no comando do SQL ele avisa por aqui também

import sqlite3

#é o canal de comunicação com o banco de dados.
conexao = sqlite3.connect("empresa.db")

#cursor é quem vai mandar no canal de conexão com o sqlite3
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,        -- diz que é autoincrmentavel iniciando em 1
    nome TEXT NOT NULL,
    preco REAL NOT NULL
    )
""")

print("Tabela criada com sucesso !")

conexao.commit()     #Precisa sempre dar commit na alteração
conexao.close()




#Depois disso temos a incersçao de dados dentro desta tabela

nome = "Monitor"
preco = 899.90

#Sempre temos que fazer uma conexão com o banco de daddos
conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

cursor.execute("""
INSERT INTO produtos(nome, preco)
VALUES(?, ?)
""", (nome, preco))

conexao.commit()

print("Produto Cadastrado")

conexao.close()



#Agora vamos pegar dados de dentro do banco ded ados e passar para a memória RAM da cpu para poder utilizar eles.
conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos")

produtos = cursor.fetchall()

for produto in produtos :
    print(produto)

conexao.close()




conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

#Aqui nós pegamos a variável x, o que nós queremos trocar e depois com o id nós botamos a variável y para trocar especificamente onde queremos trocar
cursor.execute("""
UPDATE produtos
SET preco = ?
WHERE id = ?   
""", (1200, 1))

conexao.commit()

print("produto atualizado")

conexao.close()




conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

cursor.execute("""
DELETE FROM produtos
WHERE id=?
""", (1,))

conexao.commit()

print("Produto removido!")

conexao.close

