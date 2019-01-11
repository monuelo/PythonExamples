# coding: utf-8
# Área e Perímetro de um Círculo
# (c) Héricles Emanuel, UFCG, Programação 1
import math

diam = float(raw_input())
raio = diam / 2
area = math.pi * (raio ** 2)
perimetro = 2 * (math.pi * raio)

print "A: %.5f" % area
print "P: %.5f" % perimetro