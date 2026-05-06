"""
    -------------------------- Tratamento de Exceções --------------------------------
    Qualquer erro que de no programa
    
    Sem tratamento o programa quebra

    06/05
"""

#Exemplo sem tratamento
numero = int(input("Digite um número: "))
resultado = 10/numero
print(resultado)
#Se o numero digitado for 0, quebra
#Com a conversão para inteiro, no momento que eu coloco uma letra, também quebra

#tratamento com Try - Except
try:
    numero1 = int(input("Digite um número"))
    resultado1 = 10/numero1
    print(resultado1)
except:                                     #Essa geral, pega todos os erros possíveis. As mais específicas serve caso você queira tratar diferente cada exceção
    print("Ocorreu um erro")

#Tratamento de erro completo
try:
    x = int(input("Número: "))
    print(10/x)
except:        #tratamento de erro                             
    print("Ocorreu um erro")
else:          #se não der erro
    print("Executado com sucesso")
finally:        #Executa sempre
    print("Fim do programa")

#Tipos de exceção

#Value error (Valor inválido) - quando uma função recebe um argumento com o tipo correto mas com o valor inadequado.(Raiz para número negativo, transferir char pra int)

#ZeroDivisionError - quando um numero é dividido por zero

#TypeError (tipo incompatível) - Utilizando tipos incompatíveis (somar char com int)

#IndexError - quando tentamos acessar um indice que não existe dentro de uma sequência

#KeyError - Acessar uma chave inexistente em um dicionário

#FileNotFoundError - ocorre quando o programa tenta acessar um arquivo ou diretório que não existe no caminho especificado - sendo uma subclasse de OSError


#Tratamento de múltiplas exceções
#1° forma - Multiplas exceções
try:
    x = int(input("Número: "))
    print(10/x)
except ZeroDivisionError:                                  
    print("Divisão por zero")
except ValueError:                                   
    print("Valor inválido")

#2° forma - "tuplas"
try:
    x1 = int(input("Número: "))
    print(10/x1)
except (ZeroDivisionError, ValueError) as e:
    print(f"Erro: {e}")    #imprime o erro que ocorrer


#tratamento de erro genérico
try:
    
    resultado = 10/0
except Exception as e:    #Captura todas as excesões derivadas de exception  ----------- Qual seria a diferença de usar isso ou usar só o excption (acho que é pq assim tu pode imprimir) --- Da pra ter outros erros, como de memória.
    print(f"Ocorreu um erro genérico {e}") 