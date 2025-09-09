while True :
    try: 
        numero= int(input("Digite um número: "))
        numero2= int(input("Digite um número: "))
        divisao= numero / numero2
        print(divisao)
        break
    except ValueError: 
        print("INFORME UM NÚMERO")
        
    except ZeroDivisionError: 
        print("NÃO É POSSÍVEL DIVIDIR UM NÚMERO POR 0")