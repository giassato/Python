# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite o ângulo que você deseja: '))
sen = math.sin((math.radians(angulo)))
print('O ângulo {} tem o seno de {:.2f}' .format(angulo, sen))

cos = math.cos(math.radians(angulo))
print('O ângulo {} tem o cosseno de {:.2f}' .format(angulo, cos))

tan = math.tan(math.radians(angulo))
print('O ângulo {} tem a tangente {:.2f}' .format(angulo, tan))