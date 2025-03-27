#Solicite a idade
idade = int(input("Digite sua idade: "))

#O usuário já participou de um sorteio (sim ou não)
sorteio = input("Você já participou de um sorteio (sim ou não)? ")

#Se a idade for maior ou igual a 18 e a resposta for "não", exiba "Pode participar do sorteio".
if idade >= 18 and sorteio == "não":
    print("Pode participar do sorteio")