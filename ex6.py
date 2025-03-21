num = float(input("Digite um número: "))

#Se o número for divisível por 2, ele é par
#Se não, ele é ímpar 
resto_da_divisao = num % 2

if resto_da_divisao == 0:
    print("O número informado é par")

else: 
    print("O número informado é ímpar")