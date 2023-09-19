# Faça um programa que leia o comprimento do
# cateto oposto e do cateto adjacente de um triângulo retângulo e o comprimento da hipotenusa.

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = hypot(co, ca)
# ou hipotenusa = (ca ** 2 + co ** 2) ** (1 / 2)

print('O resultado é ', hipotenusa)
