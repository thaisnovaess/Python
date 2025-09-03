import random
jogadorUsuario = 100
jogadorMaquina = 100

for rodada in range(1, 11):
    print(f"=======RODADA {rodada}=======")
    print("INFORME A AÇÃO DESEJADA")
    print("1 - ATAQUE")
    print("2 - RECUPERAR VIDA")
    escolhaUser = input("Opção escolhida: ")
    
    if escolhaUser == "1":
        ataque = random.randint(10,15)
        jogadorMaquina = jogadorMaquina - ataque
    else:
        recuperarVida = random.randint(10,15)
        jogadorUsuario = jogadorUsuario + recuperarVida
        
    if jogadorMaquina <= 0:
        print("VOCÊ VENCEU")
        break
    
    escolhaMaquina = random.randint(1,2)
    
    if escolhaMaquina == 1:
        ataque = random.randint(10,15)
        jogadorUsuario = jogadorUsuario - ataque
    else: 
        recuperarVida = random.randint(10,15)
        jogadorMaquina = jogadorMaquina + recuperarVida
    
    if jogadorUsuario <= 0:
        print("VOCÊ PERDEU")
        break

    print(f"A SUA VIDA É DE {jogadorUsuario}")
    print(f"A VIDA DA MÁQUINA É DE {jogadorMaquina}")
    
if jogadorUsuario > jogadorMaquina and jogadorUsuario > 0:
    print("Você perdeu!")
elif jogadorUsuario > jogadorMaquina and jogadorMaquina > 0: 
    print("Você venceu!")    
else: 
    print("Empate")
