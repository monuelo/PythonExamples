# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Classifica Números pelo Menor dos Extremos

numeros = []
n_abaixo = []
n_acima = []

qtd_num = int(raw_input())
if qtd_num > 1:
	for i in range(qtd_num):
		num = raw_input()
		numeros.append(int(num))

	if numeros[0] < numeros[len(numeros) - 1]:
		menor_extremo = numeros[0]
	else:
		menor_extremo = numeros[len(numeros) - 1]

	for n in numeros:
		if n < menor_extremo:
			n_abaixo.append(n)
		elif n > menor_extremo:
			n_acima.append(n)

	print "Menor dos extremos: %i" % menor_extremo
	print "%i número(s) abaixo do menor" % len(n_abaixo)
	print "%i número(s) acima do menor" % len(n_acima)
