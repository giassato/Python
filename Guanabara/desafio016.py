# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
n = float(input('Digite um número: '))

print('O número digitado é {} e sua porção inteira é {}' .format(n, math.trunc(n)))