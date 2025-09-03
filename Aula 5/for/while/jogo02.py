import random 
maquina = random.randint(0,10)

while True : 
    usuario = int(input("Digite um número: "))
    
    if maquina == usuario : 
        print("Você venceu!")
        break 
    
    elif usuario < maquina :
        print("Digite um número maior")
    else:
        print("Digite um número menor")
    
    