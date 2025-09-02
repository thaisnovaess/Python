#Simular sistema de pagamento
#crédito - total 
# a vista = valor total
# 2x - juros

#débito - 5% de desconto

valor = int(input("Digite o valor da compra: "))
print("MÉTODOS DE PAGAMENTO: ")
print("1 - CRÉDITO")
print("2 - PIX")
print("3 - Débito")
pagamento = int(input("Digite o número correspondente à forma de pagamento desejada: "))


if pagamento == 1: 
    print("O valor a ser pago será: R$", valor)
    print("Método Parcelamento: ")
    print("1 - à vista")
    print("2 - em 2x com juros de 5%")
    print("3- em 3x com juros de 10%")
    metodoParcelamento = int(input("Digite o método de parcelamento desejado: "))
    if metodoParcelamento == 1: 
        print("Pagamento à vista valor total: ", valor)
    elif metodoParcelamento == 2: 
        print("Pagamento parcelado em 2x - valor total: ", valor * 1.05)
    else : 
        print("Pagamento parcelado em 3x - valor total:  ", valor *1.10)
elif pagamento == 2  :
    print("O valor a ser pago com desconto de 5%: R$", valor*0.95)

else: 
    print("O valor a ser pago com desconto de 2%: R$", valor*0.98)