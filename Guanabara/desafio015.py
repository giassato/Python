# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

km = float(input('Quantos Km foram percorridos? '))
qtd = int(input('Quantos dias você alugou o carro?  '))

preco = (km * 0.15) + (qtd * 60)

print('O preço a pagar é de R$ {:.2f} reais ' .format(preco))