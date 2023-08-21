print("Programa Cálculo IMC")
print("Digite seu peso e sua altura conforme exemplo. Ex.: Seu peso é: 56.7 kg e sua altura á 1.76 cm")

peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura: "))
imc = peso /altura ** 2
msg = "IMC: {0:.2f} \nIMC {1} classifica-se como {2}. O seu IMC de acordo com a OMS está {3} do recomendado para sua altura"

if imc <= 18.5:
   print(msg.format(imc, "menor ou igual a 18.5", "Magreza", "abaixo"))

elif imc <= 24.9:
   print(msg.format(imc, "entre 18.5 e 24.9", "Normal", "normal"))

elif imc <= 29.9:
   print(msg.format(imc, "entre 24.9 e 29.9", "Sobrepeso", "acima"))

elif imc <= 34.9:
   print(msg.format(imc, "entre 29.9 e 34.9", "Obesidade Grau I", "acima"))

elif imc >= 39.9:
   print(msg.format(imc, "entre 34.9 a 39.9", "Obesidade Grau II", "acima"))

elif imc > 40:
    print(msg.format(imc, "maior que 40", "Obesidade Grau III", "acima"))
