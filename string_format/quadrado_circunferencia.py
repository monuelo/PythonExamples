# coding: utf-8
# Quadrado na circunferência
# (c) Héricles Emanuel, UFCG, Programação 1
import math

raio = float(raw_input())
area_circulo = math.pi * (raio ** 2)
diagonal = raio * 2

		# Diagonal Quadrado
		# diagonal = lado * (2 ** 1/2)
		# lado = diagonal / (2 ** 1/2)
		# 	Logo...


lado = diagonal / (2 ** (1.0/2))
area_quadrado = lado ** 2
area_incomum = area_circulo - area_quadrado

print "Área não comum: %.5f" % area_incomum