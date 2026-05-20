"""
class Banco:
    def __init__(self):
        self.contas = {}

    def adicionar_conta(self, conta):
        self.contas[conta.numero_conta] = conta

    def listar_contas(self):
        total = 0

        for conta in self.contas.values():
            conta.exibir_conta()
            total += conta.saldo

        print(f"Total de clientes: {len(self.contas)}")
        print(f"Total armazenado: {total}")

        
        Através da pesquisa e conversa com colegas, a melhor ideia seria a utilizaçãod de uma outra classe para gerenciamento
        """