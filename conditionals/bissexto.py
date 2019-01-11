# coding: utf-8
# Ano Bissexto
# (c) Héricles Emanuel, UFCG, Programação 1

ano = int(raw_input())
divisao1 = (ano % 400)
divisao2 = (ano % 4)
divisao3 = (ano % 100)
if divisao1 == 0 or divisao2 == 0 and divisao3 != 0:
	print "%i é bissexto" % ano
else:
	print "%i não é bissexto" % ano