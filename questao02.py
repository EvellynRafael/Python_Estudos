print("QUESTÃO 02 - AV 2")

florzinha = 1
Dubai = 2
branco = 3
voto_um = 0
voto_dois = 0
voto_b = 0
voto_n = 0
encerrar = -1

print("Opções de voto: \nFlorzinha = 1. \nDubai = 2. \nBranco = 3. \nNulo = Acima de 4.")

urna = int(input("Digite 0 para iniciar a votação ou -1 para encerrar a contagem de votos:"))

while urna == 0:
    votacao = int(input("Digite a sua opção de voto: "))

    if votacao == 1:
        voto_um += 1

    elif votacao == 2:
        voto_dois += 1

    elif votacao == 3:
        voto_b += 1

    elif votacao >= 4:
        voto_n += 1

    elif votacao == -1:
        break

total_votos = (voto_um + voto_dois) + (voto_b + voto_n)
percent_um = int(voto_um / (voto_um + voto_dois) * 100)
percent_dois = int(voto_dois / (voto_dois + voto_um) * 100)

print('Total de votos {}'.format(total_votos))
print('Total de votos Brancos: {}'.format(voto_b))
print('Total de votos Nulos: {}'.format(voto_n))
print('Total de votos do Candidato 1: {}'.format(voto_um))
print('Percentagem de votos do Candidato 1: {}%'.format(percent_um))
print('Total de votos do Candidato 2: {}'.format(voto_dois))
print('Percentagem de votos do Candidato 2: {}%'.format(percent_dois))