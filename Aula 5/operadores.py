#operadores 


idade = int(input(" Digite a sua idade: "))
habilitacao = input("Você possui habiliação? [S/N]")

if idade >= 18 and habilitacao == "S":
    print("Pode dirigir")
    
else: 
    print("Não esta permitido a dirigir")