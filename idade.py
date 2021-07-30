idade = int(input("Qual a sua idade?: "))

if(idade <= 3):
    print("Bebê!")
elif (idade > 3 and idade <= 13):
        print("Criança")

elif (idade > 13 and idade < 20):
    print("Adolescente")

elif (idade <= 20 and idade < 65):
    print("Adulto")

elif (idade >= 65):
    print("Idoso")