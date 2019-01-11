# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Bubblesort

def bubblesort(lista):

	for i in range(len(lista) - 1):
		if lista[i] > lista[i + 1]:
			lista[i], lista[i + 1] = lista[i + 1], lista[i]
		for i in range(len(lista) - 1):
			if lista[i] > lista[i + 1]:
				lista[i], lista[i + 1] = lista[i + 1], lista[i]
	return lista

l1 = [5,2,9,11,6,13]
print bubblesort(l1)