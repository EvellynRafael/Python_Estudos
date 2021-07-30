print("QUESTÃO 03 - AV 2")

pedido = 0
valor = 0
total = (0)
qtditens = 0

print("Cardápio: \n100 - Cachorro-Quente - R$3.00 "
      "\n101 - Bauru Simples - R$2.50 "
      "\n102 - Bauru com Ovo - R$4.50 "
      "\n103 - Hambúrguer - R$7.00 "
      "\n104 - X-Tudo - R$11.00 "
      "\n105 - Refrigerante - R$5.00\n")


while pedido != -1:

    pedido = int(input("Faça o seu pedido: "))
    qtditens = int(input("Digite a quantidade:" ))

    if pedido == 100:
        valor = 3 * qtditens

    elif pedido == 101:
        valor = 2.50 * qtditens

    elif pedido == 102:
        valor = 4.50 * qtditens

    elif pedido == 103:
        valor = 7 * qtditens

    elif pedido == 104:
        valor = 11 * qtditens

    elif pedido == 105:
        valor = 5 * qtditens


#Valor total só é contabilizado corretamente o informar 0 na quantidade do produto depois de finalizar a compra digitando -1

total = valor + qtditens
print('O valor total do pedido é R$: {}'.format(total))