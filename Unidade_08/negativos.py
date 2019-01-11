# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Negativos no fim

def negativos_no_fim(lista):
	ind = len(lista) - 1
	for i in range(len(lista) -1, -1, -1):
		if lista[i] < 0:
			lista[i], lista[ind] = lista[ind], lista[i]
			ind -= 1
