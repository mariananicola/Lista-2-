#Solicite a idade
idade = int(input("Insira sua idade: "))

#Pergunte se o usuário possui impedimento para votar (sim ou não)
impedimento = input("Você possui impedimento para votar (sim ou não)?  ")

#Se a idade for maior ou igual a 16 e a resposta for "não", exiba "Pode votar".
if idade >= 16 and impedimento == "não" or impedimento == "n" or impedimento == "N" or  impedimento == "Não" or impedimento == "NÃO":
    print("Pode votar!")