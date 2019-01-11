# coding: utf-8
# Concurso
# (c) Héricles Emanuel, UFCG, Programação 1

c1nota1 = float(raw_input())
c1nota2 = float(raw_input())
c1nota3 = float(raw_input())
c1_idade = int(raw_input())
c2nota1 = float(raw_input())
c2nota2 = float(raw_input())
c2nota3 = float(raw_input())
c2_idade = int(raw_input())

media_1 = (c1nota1 * 0.3) + (c1nota2 * 0.4) + (c1nota3 * 0.3)
media_2 = (c2nota1 * 0.3) + (c2nota2 * 0.4) + (c2nota3 * 0.3)

if media_1 > media_2:
	print "O primeiro candidato foi aprovado com média %.1f." % media_1
elif media_2 > media_1:
	print "O segundo candidato foi aprovado com média %.1f." % media_2
elif media_1 == media_2 and c1_idade > c2_idade:
	print "O primeiro candidato foi aprovado com média %.1f." % media_1
elif media_1 == media_2 and c2_idade > c1_idade:
	print "O segundo candidato foi aprovado com média %.1f." % media_2
elif media_1 == media_2 and c1_idade == c2_idade:
	print "Empate."