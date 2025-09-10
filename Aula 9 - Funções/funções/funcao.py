#Cria a Função:
def hello():
    print("Olá Mundo")
    
#Chamada da Função:
hello()

def soma (): 
    numero = int(input("Digite um número: "))
    numero2 = int(input("Digite um número: "))
    soma = numero + numero2 
    print(soma)
    
soma()
    
#Calcula Média
def somaMedia (): 
    nota1 = int(input("Digite um número: "))
    nota2 = int(input("Digite um número: "))
    soma = nota1 + nota2 
    return soma 
media = somaMedia()/2
print(media)