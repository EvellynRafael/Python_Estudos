print("Loja, atividade 3")

total = 0
dinheiro = 0
count = 0
valor = 0

while valor >= 0:
    total = valor 
    valor = float(input("Produto" + str(count) + "R$: "))

    if (valor == 0):
           print('Total: R$ ' + str(total))
           dinheiro = float(input('Dinheiro: R$ '))
           print('Troco: R$: ' + str(dinheiro-total))
           count = 0
           total = 0
           dinheiro = 0

    else:
        total = total + valor
        print("Fim da compra!")
