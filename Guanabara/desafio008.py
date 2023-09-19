# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
m = medida * 1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A media de {}m corresponde a {:.1f}km; '. format(medida, km))
print('A {:.1f}hm '. format(medida, hm))
print('A {:.1f}dam '. format(medida,km))
print('A {:.1f}m '. format(m))
print('A {:.1f}dm '. format(dm))
print('A {:.1f}cm '. format(cm))
print('A {:.1f}mm '. format(mm))