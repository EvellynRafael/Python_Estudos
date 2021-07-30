
import operator


print("Atividade 3 sobre vetores")


vetor_um = []
vetor_dois = []
vetor_tres = []

print("Primeiro vetor")

for i in range (0,10):
    numero = int(input("Digite o número: "))
    vetor_um.append(numero)

print(vetor_um)

print("Segundo vetor ")

for i in range (0,10):
    number = int(input("Digite o numero: "))
    vetor_dois.append(number)

print(vetor_dois)


for i in range (0,20):

    vetor_tres = vetor_um + vetor_dois

print(vetor_tres)






