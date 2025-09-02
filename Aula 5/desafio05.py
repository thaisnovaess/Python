import random
lista = ["Pedra", "Papel", "Tesoura"]
maquina = random.choice(lista)

usuario = input("Hora de jogar! Digite Pedra, Papel ou Tesoura: ")

print(maquina)

if maquina == "Pedra" and usuario == "Papel":
    print("Parabéns! Você venceu o jogo")
    
elif maquina == "Pedra" and usuario == "Tesoura":
    print("Você perdeu! tente novamente")
    
elif maquina == "Papel" and usuario == "Tesoura": 
    print("Parabéns! Você venceu o jogo") 
    
elif maquina == "Papel" and usuario == "Pedra":
    print("Você perdeu! tente novamente")
    
elif maquina == "Tesoura" and usuario == "Papel":
    print("Você perdeu! tente novamente")
    
elif maquina == "Tesoura" and usuario == "Pedra":
    print("Parabéns! Você venceu o jogo")
    
else: 
    print("Você empatou o jogo com a máquina!")