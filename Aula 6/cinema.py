
#Você foi contratado para criar um programa em Python que ajude na venda de ingressos em um cinema.

	#Crie uma lista com os filmes em cartaz.

	#Crie outra lista com os preços dos ingressos para cada filme.

	#Exiba os filmes numerados junto com seus preços.

	#Peça para o usuário escolher o número do filme desejado.

	#Mostre na tela o filme escolhido e o valor a ser pago.

#1 - Vingadores: Ultimato - R$ 25
#2 - Toy Story 4 - R$ 20
#3 - O Rei Leão - R$ 22
#4 - Matrix - R$ 18

#Digite a posição do filme escolhido: 2
#Filme escolhido: Toy Story 4 - R$ 20
i = 1
listaFilmes = ["Vingadores: Ultimato", "Toy Story 4", "Rei Leão", "Matrix"]
listaPreco = [25,20,22,18]

for filme, preco in zip(listaFilmes, listaPreco): 
    print(f"{i}- {filme} = R$ {preco} ")
    i= i + 1
    
posicao = int(input("Digite a posição do filme que deseja assistir: ")) - 1
print(f"Filme escolhido:  {listaFilmes[posicao]} - R$ {listaPreco[posicao]}")