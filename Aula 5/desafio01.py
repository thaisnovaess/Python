# A confederação Nacional de Natação precisa de uma programa que leia a idade de uma atleta e mostre sua 
# categoria, de acordo com a idade.
# Até 9 anos: MIRIM
# Taxa inscrição - R$ 50
# Até 14 anos: INFANTIL
# Taxa inscrição - R$ 70
# Até 19 anos: JUNIOR
# Taxa inscrição - R$ 90
# Até 24 anos: SÊNIOR
# Taxa inscrição - R$ 110
# Acima: MASTER
# Taxa inscrição - R$ 130

idade = int(input("Digite sua idade: "))

if idade <= 9 :
    print("Categoria: Mirim. Taxa de Inscrição R$50,00")
    
elif idade <= 14 : 
    print("Categoria: Infantil. Taxa de Inscrição R$70,00")
    
elif idade <= 19 :
    print("Categoria: Junior. Taxa de Inscrição R$90,00")
    
elif idade <= 24 : 
    print("Categoria Sênior. Taxa de Inscrição R$110,00 ")
    
if idade > 24 : 
    print("Categoria Master. Taxa de inscrição: R$ 130,00")
