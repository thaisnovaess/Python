# Lista = []
# Tupla = ()
# Dicionario = {}


produto = {
    "Tipo" : "Notebook",
    "Preco" : 5000,
    "Marca" : "Positivo",
    "Processador" : "I5-10210U"
}
#Adicionar itens no dicionario
produto["Memoria Ram"] = "8gb ram"


#Alterar o valor do item em um dicionario
produto["Preco"] = 6000


#Remover um item
del produto["Memoria Ram"]


for key, value in produto.items():
    print(f"{key} - {value}")
    
