ladoum = input('Informe o lado A do triangulo: ')
ladodois = input('Informe o lado B do triangulo: ')
ladotres = input('Informe o lado C do triangulo: ')

if (ladoum == ladodois) and (ladoum == ladotres):
    print("Triângulo Equilatero!")
elif (ladoum != ladodois) and (ladoum != ladotres) and (ladodois != ladotres):
    print("Triângulo Escaleno!")
else:
    print("Triângulo Isósceles!")







