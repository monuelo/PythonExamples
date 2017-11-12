# coding: utf-8
# Clássico dos Maiorais
# (c) Héricles Emanuel, UFCG, Programação 1

campinense = int(raw_input())
treze = int(raw_input())

if campinense > treze:
	print "Campinense"
elif treze > campinense:
	print "Treze"
elif treze == campinense:
	print "Empate"