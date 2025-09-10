#calcular área e perímetro de um retângulo: 

def retangulo(altura, base):
    perimetro = 2*(altura + base)
    print("O PERÍMETRO DO RETÂNGULO É " , perimetro)
    
    
retangulo(10, 10)

#Código que calcula o perímetro de um triÂngulo:
def triangulo(ladoA, ladoB=0, ladoC=0):
    if ladoB == 0 and ladoC == 0:
        perimetro = ladoA * 3
    elif ladoC == 0:
        perimetro = ladoA + 2* ladoB
    else:
        perimetro = ladoA + ladoB + ladoC
        
    print(f"O prímetro é de {perimetro}")
    
triangulo(3, 2)