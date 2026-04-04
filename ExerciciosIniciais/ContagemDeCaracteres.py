"""
-------- Contagem de caracteres -----------           (em andamento)                          || -------- Character Count -----------           (in progress)                                        
Informe quantos caracteres a frase contém desconsiderando os espaços                          || Enter the number of characters in the phrase, excluding leading and trailing spaces.         
Informe quantas vezes aparece um certo caracter                                               || Enter how many times a certain character appears      
 
Autor: Vinicius Fagundes                                                                      || Author: Vinicius Fagundes
Data:28/03/2026                                                                               || Date: 03/28/2026
"""
import time
import keyboard

#if keyboard.is_pressed('0'):
#        print("Voltando!")

def return0(): #Função que vai voltar para o menu não sei como fazer isso ainda) sempre que for chamada a qualquer momento

    print("Voltando...AAA")
    


op = 4

print("Bem vindo!")

keyboard.add_hotkey("/", return0, suppress=True) #Chamando o hotkey -- esse comando cria um callback, então interrompe tudo o que estiver fazendo para rodar a função selecionada  --- o suppress não deixa que a tecla apareça no terminal (eu estava digitando e dai ficava printando por exemplo: "/ VoltandoAAA", com a barra junto)
                  #Quando eu cliquei o 'q' sem querer, chamou a função também, tenho q ver sobre isso


while(op!=0):
    try:            #vou tentar colocar isso para por exemplo, não quebrar caso coloque uma letra na pergunta inicial
        if (op == 0):
            print("Saindo...")
            time.sleep(2)

        elif (op == 1):
            print(frase)
            time.sleep(2)

        elif (op == 2): # Aqui da p deixar uma opção tbm sobre contar espaços ou não - tava vendo com o gemini e ele deu uma ideia bem interessante de usar dicionários de comandospara diminuir a complexidade desses if dentro de print... - como é mais avançado, vou deixar assim
            #Aqui eu poderia utilizar o strip para algo como escolher se quer considerar os espaços no meio da frase ou não
            conta = input("Você deseja contar os espaços? (S/N)").lower()
            if(conta !="s" and conta !="n"):
                print("Digite S ou N")
            else:
                print(f"A frase contém: {len(frase.replace(' ','')) if conta == 'n' else len(frase)} caracteres") #Eu escolhi deixar todas as alterações dentro do print para que a pessoa possa sempre ver a mesma frase que digitou (opção 1) --- Para fazer isso com um if, é necessário utilizar um if ternário
            time.sleep(2)                                                       #Aqui em cima tem que se ligar nessas aspas simples, se botar dupla, acha que ta fechando o print

        elif (op == 3):
            total = 0
            s = ''

#Quero tentar colocar aqui aquuilo que a gente fazia em c - a qualquer momento que clicar uma tecla sai - ou, primeiro volta para o menu principal e depois sai(como se fosse 2 return)

            letra = input("Qual letra você quer conferir?").lower() #Da p deixar ele escolher se quer considerar as maiusculas ou não
        
            for c in frase.lower():
                if (c == letra): #para testar letra maiúscula e minúscula -- coloquei ponto lower no for e na letra
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
                    (Digite '/' para voltar a qualquer momento)
        """))   
    except ValueError:
        print("Digite somente opções apresentadas")
        op=1