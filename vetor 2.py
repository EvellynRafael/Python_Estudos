print("Atividade 2, notas dos alunos")

num_aluno = []
reprovado - []

for i in range(0,10):

    nome = input("\nNome do aluno: ")
    nota_um = int(input("Digite sua primeira nota: "))
    nota_dois = int(input("Digite sua segunda nota: "))
    nota_tres = int(input("Digite sua terceira nota: "))
    nota_quatro = int(input("Digite sua quarta nota: "))

    media = (nota_um + nota_dois + nota_tres + nota_quatro) / 4

    if(media >= 7):
        num_aluno.append(nome)


    else:
        reprovado.append(nome)

print("Os alunos que obtiveram média maior ou igual a 7 foram:", num_aluno)
print("Os alunos que não alcançaram a média foram:", reprovado)