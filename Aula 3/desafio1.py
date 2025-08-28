# Desafio 01
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

# Desafio 02
# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem cobrando R$
# 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
# viagens mais longas.

velocidade = int(input("Digite aqui a velocidade (somente números):"))
velocidadeMaxima = 80


if velocidade <= velocidadeMaxima :
    print("Você está dentro do limite permitido!")
    
else :
    multa = velocidade - velocidadeMaxima 
    print("Você ultrapassou o limite permitido nessa via. O valor da multa é: " , multa * 7)






