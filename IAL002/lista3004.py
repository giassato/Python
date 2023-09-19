# Dado um número inteiro n (n>1), exibir os números múltiplos de 3, até no máximo n.

n = int(input("Digite n>1: "))

for i in range(0, n+3, 3):
    print("Valor", i)