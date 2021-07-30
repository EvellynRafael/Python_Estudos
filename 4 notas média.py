print("MÉDIA DAS 4 NOTAS!")

nota = []
nome =[]

nome = (input("Digite o nome do aluno: "))

for i in range (10):

    nota.append(int(input('Nota ' + str(i+1) + ': ')))

print("Suas notas foram: {}" .format(nota) + nome)
print("A sua média foi: ", sum(nota) / len(nota))
