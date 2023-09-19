# Dado um número inteiro n (n>1), exibir os números de n até 1.

n = int(input("Digite n>1: "))

for i in range(n, 0, -1):
    print("Valor", i)

