class Conta():
    def __init__(self,titular, saldo, numero_conta, limite ): 
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.limite = limite

    def depositar(self,valor): 
        self.saldo += valor

    def sacar(self, valor):
        if (self.saldo-valor) < (0 - self.limite):
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
    
    def exibir_conta(self):                                   #Lucca falou que tem um método diferette que pode ser utilzado quando o método for somente de impressão, para facilitar o acesso no main
        print(f"Número: {self.numero_conta} | Nome: {self.titular} | Saldo: {self.saldo}")

        """
        def __str__(self):
        return f"Número: {self.numero_conta} | Nome: {self.titular} | Saldo: {self.saldo}"

        Assim, toda vez que colocar print(Conta) no main, vai ser devolvido isso. --Mais usado para uma mensagem padrão

        Se não tiver isso devolve:..................
        """