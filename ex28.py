#Solicite o preço do produto
preco = float(input("Insira o preço do produto: "))

#Confirme se está em estoque (sim ou não)
estoque = input("O produto está em estoque?(sim ou não): ")

#Se o preço for menor que 50 e o produto estiver em estoque, exiba "Produto em promoção".
if preco < 50 and estoque == "sim":
    print("Produto em promoção!")