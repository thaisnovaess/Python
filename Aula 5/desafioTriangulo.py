trianguloA = int(input("Digite aqui o lado A do triângulo: "))
trianguloB = int(input("Digite aqui o lado B do triângulo: "))
trianguloC = int(input("Digite aqui o lado C do triângulo: "))

if trianguloA == trianguloB == trianguloC: 
    print("Esse triângulo é equilátero!")
elif trianguloA == trianguloB or trianguloB == trianguloC or trianguloC == trianguloA: 
    print("Esse triângulo é Isósceles")
else : 
    print("Esse triângulo é Escaleno")