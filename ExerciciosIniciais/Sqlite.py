import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect("loja.db")

# Cursor para executar comandos SQL
cursor = conexao.cursor()

# Criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

conexao.commit()

while True:
    print("\n=== SISTEMA DE PRODUTOS ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))

        cursor.execute("""
        INSERT INTO produtos(nome, preco)
        VALUES(?, ?)
        """, (nome, preco))

        conexao.commit()

        print("Produto cadastrado!")

    elif opcao == "2":
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        print("\nLISTA DE PRODUTOS")

        for produto in produtos:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2]:.2f}")

    elif opcao == "3":
        id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
        novo_nome = input("Novo nome do produto: ")
        novo_preco = float(input("Novo preço: "))

        cursor.execute("""
        UPDATE produtos
        SET nome = ?, preco = ?
        WHERE id = ?
        """, (novo_nome, novo_preco, id_produto))

        conexao.commit()

        print("Produto atualizado!")

    elif opcao == "4":
        id_produto = int(input("Digite o ID do produto que deseja excluir: "))

        cursor.execute("""
        DELETE FROM produtos
        WHERE id = ?
        """, (id_produto,))

        conexao.commit()

        print("Produto excluído!")

    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")

conexao.close()