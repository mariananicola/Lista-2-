ano = int(input("Digite o ano: "))

#Descobrir se é bissexto 
if ano % 4 == 0 and ( not ano % 100 == 0 or  not ano % 400 == 0):
    print ("Ano bissexto")
