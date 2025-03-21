tempo = input("Informe o tempo do dia (ensolarado, nublado ou chuvoso): ")

#: se "ensolarado", exiba "Dia perfeito para sair"; 
#se "chuvoso", leve um guarda-chuva";
# senão, "Aproveite o dia!"

if tempo == 'ensolarado':
    print("Dia perfeito para sair!")

elif tempo == 'chuvoso':
    print("Leve um guarda chuva")

else:
    print("Aproveite o dia!")