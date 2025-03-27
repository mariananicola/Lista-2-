#Solicite uma senha
senha = input("Digite a sua senha: ")

#Se ela contiver pelo menos um dos caracteres "!","@" ou "#" e além disso tiver mais de 10 caracteres exiba "Senha forte".
if  "!" in senha or  "@" in senha or  "#" in senha  and len(senha) >=10:
    print ("Senha forte!")