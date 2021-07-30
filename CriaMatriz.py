def cria_matriz (numero_linhas, numero_colunas, valor):
    #Define uma matriz vazia
    matriz = []
    for i in range (numero_linhas):
        #Cria a linha
        linha = []
        for j in range (numero_colunas):
            #Cria a coluna
            linha.append(valor)
        matriz.append(linha)
    return matriz
def cria_matriz_usuario (numero_linhas, numero_colunas):
    matriz = []
    for i in range (numero_linhas):
        # Cria a linha
        linha = []
        for j in range (numero_colunas):
            valor = int(input("Digite o valor da posição [" + str(i+1) + "," + str(j+1) + "]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz
def exibir_matriz (matriz):
    for linha in matriz:
        for numero in linha:
            print (numero,end=" ")
        print()

        














































































































































































































































