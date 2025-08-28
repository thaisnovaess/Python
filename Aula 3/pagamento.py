#Simular sistema de pagamento
#crédito - total 
#débito - 5% de desconto

valor = int(input("Digite o valor da compra: "))
pagamento = (input("Digite o número correspondente à forma de pagamento desejada: "))
print("MÉTODOS DE PAGAMENTO: ")
print("1 - CRÉDITO")
print("2 - PIX")

if pagamento == 1: 
    print("O valor a ser pago será: ", pagamento)
    
else :
    print("O valor a ser pago com desconto de 5%: ", valor*0.95)