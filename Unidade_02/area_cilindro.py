# coding: utf-8
# Área do Cilindro
# (c) Héricles Emanuel, UFCG, Programação 1
import math

print "Cálculo da Superfície de um Cilindro"
print "---"

diam = float(raw_input("Medida do diâmetro? "))
altura = float(raw_input("Medida da altura? "))

print "---"

raio = diam / 2
perimetro = 2 * (math.pi * raio)
ab = math.pi * (raio ** 2)		# Área da Base
al = perimetro * altura 		# Área Lateral

area_total = (2 * ab) + al 				# Duplicando as áreas da base
										# Considerando que um cilindro possui duas bases
print "Área calculada: %.2f" %	area_total