# coding: utf-8
# Perímetro de um Triângulo
# (c) Héricles Emanuel, UFCG, Programação 1
import math

x1 = int(raw_input())
y1 = int(raw_input())

x2 = int(raw_input())
y2 = int(raw_input())

x3 = int(raw_input())
y3 = int(raw_input())

d1_2 = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
d1_3 = math.sqrt(((x1 - x3) ** 2) + ((y1 - y3) ** 2))
d2_3 = math.sqrt(((x2 - x3) ** 2) + ((y2 - y3) ** 2))

perimetro = d1_2 + d1_3 + d2_3
print "O perímetro é de %.2f" % perimetro