# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Utilizando o Teorema de Herão para Calcular a Área de Triângulos
import math
num_triang = int(raw_input())
maiores = 0
total_area = 0
areas = []
for i in range(0, num_triang):
	soma = 0
	medidas = raw_input().split()
	a, b, c = medidas
	soma = float(a) + float(b) + float(c)
	s = soma / 2
	area = math.sqrt(s * (s - float(a)) * (s - float(b)) * (s - float(c)))
	areas.append(area)
	if area > 100:
		maiores += 1
		total_area += area
	print "Área %i: %.2f" % (i + 1, area)
if maiores > 0:
	area_media = total_area / maiores
	print "Número maiores: %i, área média: %.2f" % (maiores, area_media)