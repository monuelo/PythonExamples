# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Make Set

def make_set(lista):
	for i in range(len(lista) -1, -1, -1):
		for e in range(i + 1, len(lista)):
			if lista[i] == lista[e]:
				lista.pop(e)
