# coding: utf-8
# Corrigindo Equações
# (c) Héricles Emanuel, UFCG, Programação 1

import math
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

delta = (b ** 2) - (4 * a * c)

if delta < 0:
	print 'sem raizes reais'
else:
	x1 = (-b + math.sqrt(delta)) / (2 * a)
	x2 = (-b - math.sqrt(delta)) / (2 * a)
	if x1 == x2:
		print "x = %.2f" % x1
	elif x1 != x2:
		print "x1 = %.2f\nx2 = %.2f" % (x1, x2)