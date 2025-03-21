pontuacao = float(input("Insira sua pontuação: "))

#Pontuação ≥ 85: "Excelente"
#Entre 70 e 84: "Bom"
#Entre 50 e 69: "Regular"
#Abaixo de 50: "Insuficiente"

if pontuacao >=85:
    print("Excelente")

elif pontuacao >=70:
    print("Bom")

elif pontuacao >=50:
    print("Regular")

else:
    print ("Insuficiente")