# Faça um algoritmo que leia o salário de um funcionário e ostre seu novo salário com 15% de aumento.

salario = float(input('Digite seu salário R$: '))

aumento = salario * 1.15
res = round(aumento, 2)

print(f'Parabéns!!! Você acaba de receber um aumento, seu novo salário é de R$ {res}')