temp = float(input("Digite a temperatura: "))

#Acima de 30°C: "Muito quente"
# Entre 15°C e 30°C: "Temperatura agradável"
# Abaixo de 15°C: "Frio"

if temp >=30:
    print("Muito quente")

elif temp >=15:
    print("Temperatura agradável")

else:
    print("Frio")