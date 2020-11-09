print("Atividade sobre vetores 1.")

principal = []
par = []
impar = []

for i in range (0,10):
    numero = int(input("Digite o número: "))
    principal.append(numero)

    if(numero%2 == 0):
        par.append(numero)
    else:
        impar.append(numero)

print(principal)
print(par)
print(impar)