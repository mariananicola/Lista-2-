#Solicite o ano de nascimento
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2025 - ano_nascimento



if idade >= 65:
    print("Aposentadoria concedida por idade")
    exit()

tempo_contrib = int(input("Informe o tempo de contribuição: "))

if idade >= 60 and tempo_contrib >=30:
    print("Aposentadoria concedida por tempo de contribuição")

else:
    print("Não pode se aposentar")
