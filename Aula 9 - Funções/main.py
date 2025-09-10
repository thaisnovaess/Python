try:

    #ValueError: 
    numero = int(input("Digite um número: "))
except ValueError:
    print("IMPOSSÍVEL CONVERTER TEXTO PARA NÚMERO")
try:
    #ZeroDivisionError - Não é possível dividir por 0
    n1 = 10
    n2= 0 
    divisão = n1/n2 
except ZeroDivisionError:
    print("IMPOSSÍVEL DIVIDIR POR 0")

    #SyntaxError - Erro de Síntaxe
    #4nome = "Pedro" 
# except: SyntaxError:
#     print("VERIFIQUE A SÍNTAXE DO SEU CÓDIGO")
    
