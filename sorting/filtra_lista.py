# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva
# Matrícula: 117110647
# Atividade: Filtrando Elementos em uma Lista

def filtra_lista(num, lista):
	n_lista = []
	for i in range(len(lista)):
		if i % num == 0:
			n_lista.append(lista[i])
	return n_lista
