#Solicite a idade
idade = int(input("Digite sua idade: "))

#Pergunte se o usuário possui documento ("sim" ou "não").
documento = input("Você possui documento (sim ou não)? ")

#Se a idade for maior ou igual a 18 e a resposta for "sim", exiba "Acesso permitido".
if idade >= 18 and documento == "sim" or documento == "SIM" or documento == "Sim":
    print("Acesso permitido")
