#Solicite a nota
nota = float(input("Digite sua nota: "))

#Solicite a frequência do aluno 
freq = float(input("Digite sua frequência: "))

#Se a nota for menor que 6 e a frequência for maior ou igual a 75, exiba "Faça a recuperação";
#Se a nota for menor que 6 e a frequência for menor que 75, exiba "Reprovado".
#Se a nota for maior que 6 e a frequência maior que 75, exiba “Aprovado”.

if nota <= 6 and freq >= 75:
    print("Faça a recuperação")

elif nota <= 6 and freq < 75:
    print("Reprovado")

elif nota > 6 and freq > 75:
    print("Aprovado")