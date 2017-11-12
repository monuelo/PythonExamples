# coding: utf-8
# Status de uma Disciplina
# (c) Héricles Emanuel, UFCG, Programação 1

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
faltas = float(raw_input())
media = (nota1 + nota2 + nota3) / 3
limite_faltas = 90 * 0.25

if faltas > limite_faltas:
	print "reprovado por faltas"
elif media < 4 and faltas <= limite_faltas:
	print "reprovado por nota"
elif media >= 4 and media <= 7 and faltas <= limite_faltas:
	print "prova final"
elif media >= 7 and faltas <= limite_faltas:
	print "aprovado por media"