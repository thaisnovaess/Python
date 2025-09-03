# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se encontram entre 6 valores digitados 

# programa - soma - impares mutiplicados *3 - digitado 6 valores 
soma = 0

for i in range (1,7,1) :
    valor = int(input("Digite um valor: "))
    resto = valor % 2 
    resto2 = valor % 3
    
    if resto == 1 and resto2 == 0 :
        soma = soma + valor 
        print("Esse número é ímpar e multiplo de 3")
    else:
        print("Esse número não é ímpar ou multiplo de 3")