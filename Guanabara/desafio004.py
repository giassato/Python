# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(x))
print('Só tem espaços? ', x.isspace())
print('É um número? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Está em minúsculas? ', x.isupper())
print('Está em maiúsculas? ', x.islower())
print('Está capitalizada? ', x.istitle())
