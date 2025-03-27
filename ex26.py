#Solicite o login 
login = input("Insira seu login: ")

#Solicite a senha:
senha = input("Digite sua senha (de numeros): ")

#Se o login for "admin" e a senha for "1234", exiba "Acesso liberado"; 
if login == "admin" and senha == "1234":
    print("Acesso liberado!")

#Senão, exiba "Acesso negado".
else:
    print("Acesso negado!")