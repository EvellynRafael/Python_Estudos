def cria_matriz(numero_linhas, numero_colunas, valor):

    # define uma matriz vazia
    matriz = []

    for i in range(0, numero_linhas):
        # cria a linha
        linha = []
        for j in range(0, numero_colunas):
            # cria a coluna
            linha.append(valor)
        matriz.append(linha)

    return matriz

def cria_matriz_usuario (numero_linhas, numero_colunas)
    matriz = []

    for i in range (numero_linhas):
        # Cria a linha
        linha = []
        for j in range (numero_colunas):
            valor = int(input("Digite o valor da posição [" + str(i) + "," + str(j) + "]"))
            linha.append(linha)
        matriz.append(linha)

def imprime_matriz(numero_linhas, numero_colunas, matriz):

    for i in range(numero_linhas):
        print('')
        for j in range(numero_colunas):
            print(matriz[i][j], end=' ')

numero_linhas = int(input('Digite o número de linhas: '))
numero_colunas = int(input('Digite o número de colunas: '))
valor = int(input('Digite um valor: '))

matriz = cria_matriz(numero_linhas, numero_colunas, valor)

imprime_matriz(numero_linhas, numero_colunas, matriz)
