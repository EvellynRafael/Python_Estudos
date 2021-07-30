print("QUESTÃO 01 - AV2")

num_um = int(input('Digite o primeiro número: '))
num_dois = int(input('Digite o segundo número: '))
num_tres = int(input('Digite o terceiro número: '))
num_qua = int(input('Digite o quarto número: '))
num_cinc = int(input('Digite o quinto número: '))

numeros = [num_um, num_dois, num_tres, num_qua, num_cinc]

media = int((num_um + num_dois + num_tres + num_qua + num_cinc) / 5)
menor = min(numeros)
maior = max(numeros)

print('O menor número digitado é: {}'.format(menor))
print('O maior número digitado é: {}'.format(maior))
print('A média dos números digitados é: {}'.format(media))