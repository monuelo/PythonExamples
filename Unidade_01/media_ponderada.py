# coding: utf-8
# Média Ponderada
# (c) Héricles Emanuel, UFCG, Programação 1

nota1 = float(raw_input()) 
nota2 = float(raw_input())
nota3 = float(raw_input())
peso1 = float(raw_input())
peso2 = float(raw_input())
peso3 = 100 - peso1 - peso2

media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
print "Média Final: %.1f" % media