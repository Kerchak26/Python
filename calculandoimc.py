peso = float(input("Digite seu peso:"))

altura = float(input("Digite sua altura:"))

imc = peso/(altura**2)

print("O seu imc é:%.2f"%imc)

if imc < 18.5:
    print("Você está abaixo do peso normal.")
elif imc >= 18.5 and imc <= 24.9:
    print("Seu peso está normal.")
elif imc >= 25.0 and imc <= 29.9:
    print("Você está com execesso de peso.")
elif imc >= 30.0 and imc <= 34.9:
    print("Você está com obesidade classe 1.")
elif imc >= 35.0 and imc <= 39.9:
    print("Você está com obesidade classe 2.")
else:
    print("Você está com obesidade classe 3.")

