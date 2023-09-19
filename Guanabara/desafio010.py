# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

car = float(input('Digite quanto você tem na carteira R$ '))

dol = car / 4.98
res = round(dol, 2)

print(f'Você pode comprar R$ {res} dólares com R$ {car} reais')