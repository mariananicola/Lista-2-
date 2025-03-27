#Solicite a média do aluno
media = int(input("Insira sua média: "))

#Renda familiar 
renda_familiar = int(input("Insira sua renda familiar: "))



# Condições para ser elegível para bolsa:
#média for maior ou igual a 8 e renda for menor que 3000
#média for maior ou igual a 7 e participação for "sim"
#Se o aluno atende a qualquer um desses dois critérios, exiba "Elegível para a bolsa". Caso contrário exiba "Não elegível para bolsa"

if media >= 8 and renda_familiar < 3000:
    print("Elegível para bolsa")
    exit()

#Participa de atividades extracurriculares ("sim" ou "não").
atividades_extra = input("Participa de atividades extracurriculares (sim ou não)? ")

if media >=7 and atividades_extra == "sim":
    print("Elegível para a bolsa")


else:
    ("Não elegível para bolsa")