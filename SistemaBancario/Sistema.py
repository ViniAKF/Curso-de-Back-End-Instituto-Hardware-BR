"""
Código do desafio da aula 09/05

(ainda ta dando erro na parte de salvar o dicionário)
(tenq tentar deixar tudo em método)
"""

#Preciso criar valores aleatórios para as contas, ou seja, na hora de aceitar os valores preciso fazer uma verificação com for in, e conferir com todos os valores salvos para saber se já não tem algum assim 
#Vou salvar todos os objetos em um dicionário onde a chave vai ser os valores aleatórios



import random
from Conta import Conta

def main():
    op =1
    quantCadastros = 0
    banco_de_dados = dict()
    igual=0
    diferente =0
    total =0



    print("\n\n--------SISTEMA BANCÁRIO----------")

    while op != 6:  #Não sei as sintaxes certinho, preciso arrumar depois se vai ser com chaves ou coisarada

        print("\nSelecione as seguintes opções:")
        op = int(input(print("1-Criar conta \n2- Depositar \n3- Sacar\n4-Extrato \n5-Listar Contas \n6- Sair")))

        match op:
            case 1:                   #Aqui vou usar a função criadora __init__ , para criar o objeto da classe  --- vou criar o número aletório da conta, fazer a conferência de existencia, e salvar no dicionário!
                nome = input(print("Nome do cliente: "))
                depInicial = float(input(print("Depósito inicial: ")))
                limit = float(input(print("Limite da conta: ")))
                
                while diferente==0:

                    numero= random.randint(1,10000)

                    for keys in banco_de_dados:
                        if numero == keys:
                            igual=1

                    if igual == 0:
                        diferente = 1
                    
                pessoa = Conta(nome,depInicial,numero,limit)

                banco_de_dados[numero]= pessoa

                print(banco_de_dados)

                print(f"--------------Conta Criada! Número: {numero}----------------")
            
            case 2:
                numero = int(input(print("Número da conta: ")))
                valor1 = input(print("Digite o valor: "))
                try:
                    banco_de_dados[numero].depositar(valor1)
                except:
                    print("Essa conta não existe")

            case 3:
                numero = input(print("Número da conta: "))
                valor2 = input(print("Digite o valor: "))
                try:
                    banco_de_dados[numero].sacar(valor2)
                except:
                    print("Essa conta não existe")

                #aqui tbm ter um try caso o valor n seja encontrado

            case 4:
                numero = input(print("Número da conta: "))
                print("Dados: ")
                try:
                    print(banco_de_dados[numero]) #Posso colocar isso como um método também talvez
                except:
                    print("Essa conta não existe")
                ##Fazer verificação para caso n exista uma conta

            case 5:
                #eu posso fazer por um jeito muito fácil, que seria só colocar um loop com as chaves e imprimir as informações de cada objeto, mas vou tentar fazer por método para ficart mais organizado.
                #"""
                print("LISTA DE CONTAS:")
                print("-----------------------")
                try:
                    for keys in banco_de_dados:
                        banco_de_dados[keys].exibir_conta()
                        quantCadastros+=1
                        total += banco_de_dados[keys].saldo
                except:
                    print("Nenhum usuário cadastrado")
                    #dentro dessa lógica, colocar try exception para caso de erro de nenhum valor

                print("-----------------------")
                print(f"Total de clientes: {quantCadastros}")
                print(f"Soma dos saldos: {total}")
                #"""
                
            
if __name__ == "__main__":
    main()


    ###Tem que só que se ligar depois para ver se um número não precisa ser inteiro, ou float coisa assim, str...


    """
    20/05
    Dividi o código por pastas
    """

    #VOu pesquisar no chtagpt até onde é interesante deixar a lógica dentro do métdodo. Por exemplo nesse código, no case 5 eu deixo quase toda a lógica no main, porque vejo que seria difícil colocar ela dentro de um método da classe conta por não ter disponível o dicionario.
    #Maior parte da resposta está no novo arquivo - Armazenamento

    #Quero fazer a interface gráfica disso aqui depois