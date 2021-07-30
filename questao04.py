print("QUESTÃO 04 - AV 2")

import random

carta_pc = []
ponto = 0
ponto_pc = 0
tentativas = 3
qtdcarta = 5

random.seed(10)

game = int(input("Digite 1 para iniciar o jogo: "))
for tentativa in range (0,3):

        carta_pc.append(random.choice(range(13)))

        carta = int(input("Escolha uma carta: \n2.\n3.\n4."
                        "\n5.\n6.\n7."
                        "\n8.\n9.\n10."
                        "\n11 - Valete."
                        "\n12 - Rainha."
                        "\n13 - Rei.\n1 - Ás. "))

        if carta in carta_pc:
            print("Acertou. ")
            ponto += 3

        else:
            print("Errou!")

        #vez do computador

        random.randint(1,13)

        if random in carta_pc:
            print("Acertei!")
            ponto_pc += 3

        else:
            print("Errei!")

print("Cartas secretas: ", carta_pc)
print("Cartas digitadas: ", carta)
print("Quantidade de pontos: ", ponto)
print("Quantidade de pontos meus: ", ponto_pc)
print("Fim de jogo!")


