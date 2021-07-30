print("Atividade POO - Gasolina")

class bombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantCombustivel = quantCombustivel

    def alterarValor(self, valorLitro):
        self.valorLitro = valorLitro

    def alterarCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def alterarQuantCombustivel(self, quantCombustivel):
        self.quantCombustivel = quantCombustivel

    def abastecerPorValor(self, valor):
        temp = valor/self.valorLitro
        self.alterarQuantCombustivel(self.quantCombustivel - temp)
        return temp

    def abastecerPorLitro(self, qtd):
        temp2 = qtd * self.valorLitro
        self.alterarQuantCombustivel(self.quantCombustivel - qtd)
        return temp2

a1 = bombaCombustivel("Gasolina", 5, 500)
print("Valor a ser abastecido:", a1.abastecerPorValor(150))
print("Combustível total:", a1.quantCombustivel)
print("Litros:", a1.abastecerPorLitro(30))
print("Quantidade:", a1.quantCombustivel)


