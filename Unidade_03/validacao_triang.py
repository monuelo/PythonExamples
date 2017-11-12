# coding: utf-8
# Validação de Triângulos
# (c) Héricles Emanuel, UFCG, Programação 1

lado_1 = int(raw_input())
lado_2 = int(raw_input())
lado_3 = int(raw_input())
soma_lados = lado_1 + lado_2 + lado_3

if lado_1 < lado_2 + lado_3 and lado_1 > abs(lado_2 - lado_3):
	print "triangulo valido. %i" % soma_lados
elif lado_2 < lado_1 + lado_3 and lado_2 > abs(lado_1 - lado_3):
	print "triangulo valido. %i" % soma_lados
elif lado_3 < lado_2 + lado_1 and lado_3 > abs(lado_2 - lado_1):
	print "triangulo valido. %i" % soma_lados
elif lado_1 < lado_2 + lado_3 and lado_1 < abs(lado_2 - lado_3):
	print "triangulo invalido."
elif lado_2 < lado_1 + lado_3 and lado_2 < abs(lado_1 - lado_3):
	print "triangulo invalido."
elif lado_3 < lado_2 + lado_1 and lado_3 < abs(lado_2 - lado_1):
	print "triangulo invalido."