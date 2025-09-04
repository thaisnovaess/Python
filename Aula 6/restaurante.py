listaLanches = ["X-Bacon", "X-Tudo", "Hot-Dog", "X-Salada", "X-Frango", "Batata com cheddar e bacon", "X-Burguer"]
listaPreco = [20,30,20,23,20,]

i= 1

for preco, lanche in zip (listaPreco, listaLanches):
    print(f"{i} - {lanche} - R${preco}")
    i = i + 1
    
lancheEscolhido = int(input("Digite a posição do lanche esolhido: ")) - 1

print(f"Lanche escolhido {listaLanches}")

