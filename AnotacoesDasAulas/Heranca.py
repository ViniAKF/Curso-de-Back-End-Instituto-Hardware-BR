"""
Cotinuando o conteúdo, na aula de hoje vamos dar um foco maior ao conteudo de heranças

22/04/2026
"""

#sempre que for chamar da pai, coloca o super()

# CLASSE PAI
class Impressora:
    def __init__(self, marca, modelo, colorida, peso):
        self.marca = marca
        self.modelo = modelo
        self.colorida = colorida
        self.peso = peso

    def exibir_dados(self):
        return f"Marca = {self.marca} | Modelo = {self.modelo} | Colorida = {self.colorida} | Peso = {self.peso}"


# CLASSE HERDEIRA/FILHA
class Laser(Impressora):
    def __init__(self, marca, modelo, colorida, peso, capacidade_toner, frente_verso):
        super().__init__(marca, modelo, colorida, peso)                                                           #tu vai ter q inicializar as variaveis nessa classe. ai para n escrever tudo d novo, usa da classe pai
        self.capacidade_toner = capacidade_toner
        self.frente_verso = frente_verso

    def exibir_dados(self):
        base = super().exibir_dados()
        return base + f" | Toner = {self.capacidade_toner} | Frente e verso = {self.frente_verso}"


# OUTRA HERANÇA
class Matricial(Impressora):
    def __init__(self, marca, modelo, colorida, peso, agulhas, varias_vias):
        super().__init__(marca, modelo, colorida, peso)                                                             # No caso tu vai sempre instanciar um objeto a partir da classe filha, então o valor de marca, modelo e etc. nunca vai ser igual para um impressora matricial e uma laser, pois vao ser colocados diferentes no objeto 
        self.agulhas = agulhas
        self.varias_vias = varias_vias

    def exibir_dados(self):
        base = super().exibir_dados()
        return base + f" | Agulhas = {self.agulhas} | Várias vias = {self.varias_vias}"


# LISTAS
lista_laser = []
lista_matricial = []


def ler_booleano(msg):
    valor = input(msg + " (s/n): ").lower()
    return valor == 's'                                     #Aqui tem dois '=', ou seja, é uma comparação. Toda vez que no return tiver uma comparação. ele retorna um valor boleano, true se for verdadeiro e false se for falso.


while True:
    print("\nEscolha de impressoras")
    print("1 - Cadastrar impressora laser")
    print("2 - Cadastrar impressora matricial")
    print("3 - Listar impressoras laser")
    print("4 - Listar impressoras matriciais")
    print("5 - Listar todas as impressoras")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == '1':
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        colorida = ler_booleano("Colorida?")
        peso = float(input("Peso: "))
        toner = input("Capacidade do toner: ")
        frente_verso = ler_booleano("Frente e verso?")
        
        impressora = Laser(marca, modelo, colorida, peso, toner, frente_verso)
        lista_laser.append(impressora)
        
        print("Impressora laser cadastrada com sucesso.")

    elif opcao == '2':
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        colorida = ler_booleano("Colorida?")
        peso = float(input("Peso: "))
        agulhas = int(input("Quantidade de agulhas: "))
        vias = ler_booleano("Lê várias vias?")
        
        impressora = Matricial(marca, modelo, colorida, peso, agulhas, vias)
        lista_matricial.append(impressora)
        
        print("Impressora matricial cadastrada com sucesso.")

    elif opcao == '3':

        if len(lista_laser) == 0:
            print("Nenhuma impressora laser cadastrada.")

        else:
            print("\nLista de impressoras laser:")
            
            for impressora in lista_laser:
                print(impressora.exibir_dados())

    elif opcao == '4':

        if len(lista_matricial) == 0:
            print("Nenhuma impressora matricial cadastrada.")
        
        else:
            print("\nLista de impressoras matriciais:")
            
            for impressora in lista_matricial:
                print(impressora.exibir_dados())

    elif opcao == '5':
        
        if len(lista_laser) == 0 and len(lista_matricial) == 0:
            print("Nenhuma impressora cadastrada.")
        
        else:
            print("\nTodas as impressoras cadastradas:")

            if len(lista_laser) > 0:
                print("\nImpressoras Laser:")
                
                for impressora in lista_laser:
                    print(impressora.exibir_dados())

            if len(lista_matricial) > 0:
                print("\nImpressoras Matriciais:")
                
                for impressora in lista_matricial:
                    print(impressora.exibir_dados())

    elif opcao == '0':
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida.")