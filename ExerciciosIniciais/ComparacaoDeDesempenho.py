"""
 -------------------------- Performance Comparison ------------------------                                 || -------------------------- Comparação de desempenho ------------------------                                     
Ask the user to enter two lists of integers (1–100) as scores for two players                               || Peça para o usuário digitar 2 listas de números inteiros (1-100), como pontuações de 2 jogadores                 
Provide the option to remove duplicate numbers.                                                             || De a opção de retirar os números repetidos.                                                                     
Calculate the average of all remaining numbers.                                                             || Calcule a média de todos os números restantes.                                                                   
Display the two lists with the values interleaved, highlighting those that were greater than the average.   || Mostre as duas listas com os valores intercalados, apontando os que estavam maior que a média.                   
Continue if anyone still has scores.                                                                        || Continue caso alguém ainda tenha pontuações.                                                                     
Each value above the average counts as one point, which ultimately determines the winner                    || Cada valor acima da média conta um ponto que, ao final, indica um vencedor                                       

Author: Vinícius Fagundes                                                                                   || Autor: Vinícius Fagundes
Date: 04/01/2026                                                                                            || Data: 01/04/2026
"""
#This project is gonna be in english

def main(){
    int i=0, op1 = 1, op2=1;

    while op1!=0:
        op1= input()
        while op2!=0:
            op2 = int(input(f"Enter the {i+1}° number of the list"))
}