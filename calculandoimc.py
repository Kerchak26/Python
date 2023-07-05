peso = float(input("Digite seu peso:"))

altura = float(input("Digite sua altura:"))

imc = peso/(altura**2)

print("O seu imc é:%.2f"%imc)

if peso < 18.5:
    print("Você está abaixo do peso normal.")
elif peso >= 18.5 and peso <= 24.9:
    print("Seu peso está normal.")
elif peso >= 25.0 and peso <= 29.9:
    print("Você está com execesso de peso.")
elif peso >= 30.0 and peso <= 34.9:
    print("Você está com obesidade classe 1.")
elif peso >= 35.0 and peso <= 39.9:
    print("Você está com obesidade classe 2.")
elif peso >= 40.0:
    print("Você está com obesidade classe 3.")

