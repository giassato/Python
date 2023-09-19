# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta, pinta uma área de 2m².

alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))

area = alt * lar

tinta = area / 2

print(f'A área da parede é de {area} m² e será necessário {tinta} litros de tinta para pintá-la')