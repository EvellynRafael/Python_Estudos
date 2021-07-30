
impar = 0

quant_num = int(input("Informe a quantidade de números que deseja digitar:"))

for i in range (quant_num):

    numero = int(input("Digite o número:"))

    if(numero%2 != 0):
        impar += 1

print('{} são numeros impares:'.format(impar))

