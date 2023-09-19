# Faça um algoritmo que leia o preço de um produto e mostra seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto R$: '))

desc = preco * 0.95
res = round(desc, 2)

print(f'O novo preço com desconto de 5% é igual a R$ {res}')