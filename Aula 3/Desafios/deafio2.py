# Desafio 02
# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem cobrando R$
# 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
# viagens mais longas.

distancia = int(input("Digite a distância da viagem a ser realizada: "))

if distancia <= 200 :
    calculo1 = distancia * 0.50
    print("O valor da passagem é: R$ " , calculo1)
else :
    calculo2 = distancia * 0.45 
    print("O valor da passagem é: R$ " , calculo2)
    

    