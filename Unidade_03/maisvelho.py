# coding: utf-8
# Mais velho entre duas pessoas
# Héricles Emanuel, UFCG, Programação 1

nome1 = raw_input()
dia1 = int(raw_input())
mes1 = int(raw_input())
ano1 = int(raw_input())
nome2 = raw_input()
dia2 = int(raw_input())
mes2 = int(raw_input())
ano2 = int(raw_input())

if ano2 > ano1:
	print nome1
elif ano1 > ano2:
	print nome2
elif ano1 == ano2:
	if mes1 < mes2:
		print nome1
	elif mes2 < mes1:
		print nome2
	elif mes1 == mes2:
		if dia1 < dia2:
			print nome1
		elif dia2 < dia1:
			print nome2
		elif ano1 == ano2 and mes1 == mes2 and dia1 == dia2:
			print "nenhuma"