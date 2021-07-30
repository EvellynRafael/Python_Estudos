larg_terreno = float(input("Largura do terreno: "))
prof_terreno = float(input("Profundidade do terreno: "))
larg_casa = float(input("Largura da casa : "))
prof_casa = float(input("Profundidade da casa : "))

area_terreno = larg_terreno * prof_terreno
area_casa = larg_casa * prof_casa

percentual = area_terreno - area_casa

print((percentual * 100) / area_terreno, "%")