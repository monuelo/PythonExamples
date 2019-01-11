# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Make Set

def make_set(lista):
	for i in range(len(lista)):
		x = i + 1
		while x < len(lista):
			if lista[i] == lista[x]:
				lista.pop(x)
			else:
				x+= 1
