# Dado um número inteiro n (n>1), exibir os números de n-1 até 1. Quantos serão impressos?

n = int(input("Digite n>1: "))

for i in range(n-1, 1, -1):
    print(i)


