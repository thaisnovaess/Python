import random
numero = int(input("Digite um número: "))
maquina = random.randint(0,10) #gera numero aleatorio

if numero == maquina: 
    print("Parabéns, você acertou o número secreto")
else :
    print("Você errou o número secreto")

print(maquina)