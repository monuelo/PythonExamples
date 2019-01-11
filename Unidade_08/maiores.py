# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Remove Maiores

def remove_maiores(lista):
	maior = 0
	for i in lista:
		if i >= maior:
			maior = i
	for e in range(len(lista) - 1, -1, -1):
		if lista[e] == maior:
			lista.pop(e)
