#== igual 
#= atribuição 
#=! diferente

nota1 = int(input("Digite a primeira nota aqui:"))
nota2 = int(input("Digite a segunda nota aqui:"))

media = (nota1 + nota2) / 2

if media >= 70:
    print("Aprovado") #identação(espaço), não precisa das chaves
else:
    print("Reprovado")