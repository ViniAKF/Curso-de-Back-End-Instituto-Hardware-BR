"""
-------- Contagem de caracteres -----------           (em andamento)                          || -------- Character Count -----------           (in progress)                                        
Informe quantos caracteres a frase contém desconsiderando os espaços                          || Enter the number of characters in the phrase, excluding leading and trailing spaces.         
Informe quantas vezes aparece um certo caracter                                               || Enter how many times a certain character appears      
 
Autor: Vinicius Fagundes                                                                      || Author: Vinicius Fagundes
Data:28/03/2026                                                                               || Date: 03/28/2026
"""
import time

op = 4

print("Bem vindo!")

while(op!=0):
    
    if (op == 0):
        print("Saindo...")
        time.sleep(2)

    elif (op == 1):
        print(frase)
        time.sleep(2)

    elif (op == 2):
        #Aqui eu poderia utilizar o strip para algo como escolher se quer considerar os espaços no meio da frase ou não
        print(f"A frase contém: {len(frase.replace(' ',''))} caracteres") #Eu escolhi deixar todas as alterações dentro do print para que a pessoa possa sempre ver a mesma frase que digitou (opção 1)
        time.sleep(2)

    elif (op == 3):
        total = 0
        s = ''

#Quero tentar colocar aqui aquuilo que a gente fazia em c - a qualquer momento que clicar uma tecla sai - ou, primeiro volta para o menu principal e depois sai(como se fosse 2 return)

        letra = input("Qual letra você quer conferir?")
        
        for c in frase:
            if (c == letra): #preciso colocar aqui ainda para testar letra maiúscula e minúscula
                total+=1
        if (total!=1):
            s = 'es'
        print(f"A letra {letra} aparece {total} vez{s} na frase digitada")
        time.sleep(2)

    elif(op==4):
        print("Digite uma frase para manipulação:")
        frase = input()

    else:
        print("Digite uma das opções fornecidas")
        time.sleep(2)


    op = int(input("""Digite o que deseja fazer: 
               1 - Ver a frase digitada 
               2 - Contar os caracteres de uma frase
               3 - Contar quantas vezes o caractere aparece na frase
               4 - Digitar nova frase
               0 - Para sair
    """))   