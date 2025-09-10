import math

def calculaCirculo(raio):
    area = math.pi * raio ** 2   #valor do pi, ** potência
    perimetro = 2 * math.pi * raio
    
    print(f"A área é de {area}")
    print(f"O perímetro pe de {perimetro}")
    
calculaCirculo(2)