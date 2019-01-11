# coding: utf-8
# Status de uma Disciplina
# (c) Héricles Emanuel, UFCG, Programação 1

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
faltas = int(raw_input())

media = (nota1 + nota2 + nota3) / 3
limite_faltas = 30 * 0.25

if faltas <= limite_faltas and media >= 7.0:
	print "aprovado por media"
elif faltas > limite_faltas:
	print "reprovado por faltas"
elif faltas < limite_faltas and media < 4.0:
	print "reprovado por nota"
elif faltas < limite_faltas and media > 4.0 and media < 7.0:
	print "prova final"