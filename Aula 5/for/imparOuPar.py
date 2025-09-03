somaPar = 0
somaImpar = 0
for i in range(1,7,1): 
    valor = int(input("Digite um número: "))
    resto = valor % 2
    
    if resto == 0:
        print("O número digitado é par") 
        somaPar = valor + somaPar  
        print(somaPar)
    else:
        print("O número digitado é ímpar")
        somaImpar = valor + somaImpar
        print(somaImpar)
        
        