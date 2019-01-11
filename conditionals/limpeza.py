# coding: utf-8
# Limpeza
# (c) Héricles Emanuel, UFCG, Programação 1

servico = int(raw_input())

if servico == 1:
	tamanho = int(raw_input())
	custo = tamanho * 80.00
elif servico == 2:
	tamanho = int(raw_input())
	custo = tamanho * 50.00
elif servico == 3:
	custo = 50.00

print "R$ %i,00" % custo 
if custo >= 200:
	print "Brinde!"