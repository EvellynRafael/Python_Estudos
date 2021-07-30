print("Alunos maiores de 18")

idade_aluno = 0


for i in range (0,10):

    idade = int(input("Informe a sua idade:"))

    if (idade >= 18):
        idade_aluno += 1

print('{} São maiores de 18 anos.', format(idade_aluno))