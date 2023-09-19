# Dado um número inteiro n(n>1), exibir os números de 0 até n-1.

n = int(input("Digite n>1: "))

for i in range(0, n, 1):
    print("Valor", i)