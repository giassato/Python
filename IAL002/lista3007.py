# Dado um número inteiro n (n>0), exibir os n primeiros pares, iniciando em trinta.

n = int(input("Digite n>1: "))

for i in range(30, 30 + n*2, 2):
    print(i)

