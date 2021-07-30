print("1O VETORES REAIS")

vetor = []

for i in range (10):
    vetor.append(float(input('Número ' +str(i+1) + ': ')))

vetor.reverse()

print(vetor)