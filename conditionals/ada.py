# coding: utf-8
# Avaliação de Desempenho Acadêmico
# (c) Héricles Emanuel, UFCG, Programação 1

semestres = float(raw_input())
if semestres > 0:
	ensino = float(raw_input())
	intelectual = float(raw_input())
	orientacao = float(raw_input())
	admin = float(raw_input())

	media = ((ensino + intelectual + orientacao + admin) / semestres)
	if semestres < 4:
		print "Promoção indeferida. Número de semestres insuficiente."
	elif ensino < 320 or intelectual < 100 or orientacao < 20:
		print "Promoção indeferida. Pontuação mínima não alcançada."
	elif media < 140:
		print "Promoção indeferida. Média insuficiente."
	elif media >= 140 and semestres >= 4 and ensino >= 320 and intelectual >= 100 and orientacao >= 20:
		print "Promoção deferida. Parabéns!"