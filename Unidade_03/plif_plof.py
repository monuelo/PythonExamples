# coding: utf-8
# Plif Plof
# (c) Héricles Emanuel, UFCG, Programação 1

valor_1 = int(raw_input())
valor_2 = int(raw_input())
valor_3 = int(raw_input())
somatorio = valor_1 + valor_2 + valor_3

if somatorio % 3 == 0 and somatorio % 5 == 0:
	print "plifplof"
elif (somatorio % 3) == 0:
	print "plif"
elif (somatorio % 5) == 0:
	print "plof"