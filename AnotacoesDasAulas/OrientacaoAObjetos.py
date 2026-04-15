"""
------------Orientação à Objetos------------
(Paradigm que organiza o codigo em objetos. que representam entidades do mundo real ex: Aluno, prodto, carro)

Aula do dia 15/04/2026
"""


#Classe = modelo
#Objeto = instância da classe

#Cada objeto possui:
#atributos (carat=cteristicas)
#métodos(ações)

class Pessoa:
    def __init__(self,nome,idade):   #Def é para definir os métodos de uma classe -- __init__ (com 2 underline) é o construtor da classe(roda automaticamente toda vez que for instanciada)
        self.nome = nome             #Self é o "termo geral" das variáveis (como o N em matemática) - Ele é "substituido" pelo objeto, para que cada vez salve no objeto instanciado(ex: p1.nome = nome)
        self.idade = idade

#Criando o objeto
p1 = Pessoa("Ana", 25)

print(p1.nome)
print(p1.idade)




class Conta:
    def __init__(self,titular, saldo=10): #Tu pode ja colocar valores default quando instancia um objeto  -- o default te permite chamar o metodo sem especificar aquele valor
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor): #Novo método
        self.saldo += valor

    def exibir_saldo(self):
        print("Saldo:", self.saldo)


c1 = Conta("João", 100)  #Aqui o sor fez para ser mais facil de demonstrar, mas em uma situação real, seria dentro de um main
c1.depositar(50)
c1.exibir_saldo()

class Produto: #Criando uma classe sem um construtor
    nome : str
    preco : float
    estoque : int

prod = Produto() #quando a gente não tem o método construtor, precisamos instanciar em branco e colocar diretamente nos atributos
prod.nome="Notebook"
prod.preco=2500.0
prod.estoque=10 # se eu tirar grita
           
print(f"Produto {prod.nome} tem estoque {prod.estoque}")     ##Ta, mas e se eu quisesse fazer um método que faça esse print(para ser mais facil para as outras variáveis) - eu teria que passar eles p algum lugar entre um metodo e outro, ou era só utilizar?

#Metodo destrutor - destroi a instancia do objeto
"""
class Cachorro: #O python tem uma coleta automática de lixo para coisas que não são mais utilizadas, então não seria tão util, mas em C sim
    def __del__:
"""        

#Encapsulamento
#(sor não explicou muito bem  -- falou que vai falar melhor nas próximas aulas)----------REVISAR


#UML - Unifined Modeling Language - Diagrama utilizado por analistas para "conversar" com os devs - Simbolos utilizados:
# - => privado      || No python: self.__nome    -- só a classe pode manipular
# + => publico      || No python: self.nome      -- todos                     (sor não explicou muito bem  -- falou que vai falar melhor nas próximas aulas)----------REVISAR
# # => protegido    || No python: self._nome     -- herdeiros

class ContaPrivado:
    def __init__(self, saldo): 
        self.__saldo = saldo

    def depositar(self,valor): 
        self.__saldo += valor

    def ver_saldo(self):
        return self.__saldo  #Lorenzo falou algo bem interessante sobre isso não ser intuitivo, a nivel de experiência do usuário. Se eu quero só ver o saldo, é só printar aqui, n tem sentido dar um return, isso seria caso quisesse usar o saldo pra algo

c = ContaPrivado(100)
c.depositar(50)
print(c.ver_saldo())

#PRojeto - ConferenciaDeAprovacao.py