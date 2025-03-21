idade = float(input("Informe sua idade: "))

#Menor que 12: "Criança"
#Entre 12 e 17: "Adolescente"
#Entre 18 e 64: "Adulto"
#65 ou mais: "Idoso"

if idade < 12:
    print("Criança")
elif 12 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 64:
    print("Adulto")
else:
    print("Idoso")