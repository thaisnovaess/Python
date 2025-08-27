#Peça ao usuário o preço original de um produto e o percentual de desconto. Calcule o valor com desconto e mostre o resultado.

precoOriginal = int(input("Digite o preço original do produto: "))
desconto = int(input("Digite o desconto (sem caracteres especiais):"))
valorDesconto = precoOriginal * (desconto /100)
precoComDesconto = precoOriginal - valorDesconto

print("O novo valor do produto com desconto aplicado é: ", "/n R$", precoComDesconto) #/n pula linha (dentro das aspas)

#Notação centífica 
#12000 - 1.2 * 10 **4
#12000 - 1.2E4

