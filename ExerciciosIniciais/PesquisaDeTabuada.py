"""
-----------Multiplication Table Search------------------                                                               ||   -----------Pesquisa de Tabuada------------------
Write a program that prompts the user to enter an integer (1-10) and prints the multiplication table for that number.  ||   Faça um programa que peça um número inteiro (1-10) e imprima a tabuada desse número.  

Author: Vinícius Fagundes                                                                                              ||   Autor: Vinícius Fagundes
Date: 03/25/2026                                                                                                       ||   Data: 25/03/2026
"""

num = 1

while num != 0:
    num = int(input("Enter an integer to see its multiplication table: (1-10) - 0 for Exit \n"))
    if(1<= num <= 10):
        #try:      #Usaria o try caso não tivesse essa condição de 1-10, para tratar os erros com o except
            print(f"Multiplication Table for {num}:")
            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")
        #except ValueError:                                       - #Estava tentando fazer aqui a condição de 1 até 10, mas o except é só para tratamento de erro. "Se falhar..."
            #print("Invalid input. Please enter a valid integer")    - O ValueError trata o conteúdo inválido (valor errado no tipo certo)(buscar algo inexistente em uma lista por ex), enquanto o TypeError trata a natureza incompatível (tipo errado para a operação)(tentar somar int com array).

    elif num==0:
        print("Leaving...")
    else:
        print("Please enter a value between 1 and 10")
        #Preciso arrumar essa parte de 0 e até 10 para que funcione corretamente e consiga sair quando quiser (não deu tempo na aula)