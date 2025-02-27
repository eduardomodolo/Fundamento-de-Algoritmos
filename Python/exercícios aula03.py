#Recupera 
from math import ceil

PI = 3.1415

raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))
#calcular area da base
area_base = PI * raio**2#estrela dupla eleva a 2#
#calcular area lateral#
area_lateral = altura * 2 * PI * raio

area_cilindro = area_base + area_lateral
print(f"Area a ser pintada: {area_cilindro:.2f}")

#calcular volume tinta
volume_tinta = area_cilindro / 3
print(f"Qtde de litros necessários: {volume_tinta:.2f}")


latas_tinta = ceil(volume_tinta / 5 )
print(f"Qtde de latas de tinta: {latas_tinta:.2f}")

