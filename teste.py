num1 = float (input("Digite um número: "))
num2 = float (input("Digite um número: "))

#Se a variável num2 for igual a 0, não faz a divisão
if num2 == 0:
    print("Não é possível fazer a divisão por zero.")
    print("Para o segundo número, informe um número diferente de zero.")
    print("Tente novamente")


divisao = num1 / num2

print(divisao)