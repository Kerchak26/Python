idade = int(input("Digite sua idade:"))

if idade < 10:
    print("Você é uma criança!")
elif idade >= 10 and idade <= 14:
    print("Você é um pré-adolescente!")
elif idade >= 15 and idade <18:
    print("Você é adolescente!")
else:
    print("Você é adulto!")
