# coding: utf-8
# Ciclo Trigonométrico
# Héricles Emanuel, UFCG, Programação 1

angulo = int(raw_input())

if angulo > 360:
	angulo = (angulo % 360)
	if angulo > 0 and angulo < 90:
		print "Quadrante 1"
	elif angulo > 90 and angulo < 180:
		print "Quadrante 2"
	elif angulo > 180 and angulo < 270:
		print "Quadrante 3"
	elif angulo > 270 and angulo < 360:
		print "Quadrante 4"
	elif angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
		print "sobre eixos"
else:
	if angulo > 0 and angulo < 90:
		print "Quadrante 1"
	elif angulo > 90 and angulo < 180:
		print "Quadrante 2"
	elif angulo > 180 and angulo < 270:
		print "Quadrante 3"
	elif angulo > 270 and angulo < 360:
		print "Quadrante 4"
	elif angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
		print "sobre eixos"