#Solicite a nota
nota = float(input("Digite sua nota: "))

#Solicite a frequência do aluno 
freq = float(input("Digite sua frequência: "))

#Se a nota for maior ou igual a 6 e a frequência for maior ou igual a 75, exiba "Aprovado".
if nota >= 6 and freq >= 75:
    print("Aluno aprovado!")