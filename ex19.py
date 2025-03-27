#Solicite a idade
idade = int(input("Insira sua idade: "))

#Pergunte se o cliente possui o cartão 
cartao = input("Você possui o cartão da loja (sim ou não)? ")

#Se a idade for 65 ou mais ou se o cliente tiver o cartão, exiba "Desconto aplicado".
if idade >= 65 and cartao == "sim" or cartao == "SIM"  or cartao == "s" or cartao == "Sim" or cartao == "S":
    print("Desconto aplicado")