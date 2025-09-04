listaNotas = []

while True:
    nota = int(input("Digite a sua nota ou 999 para sair: "))
    
    
    if nota == 999:
        break
    elif nota > 10 or nota < 0:
        print("Adicione uma nota entre 0 e 10")
    
    listaNotas.append(nota)
    print(listaNotas)
    