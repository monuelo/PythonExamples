# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Organiza Lista pela Média

def organiza_por_media(lista):
	soma = 0
	pivot = len(lista)
	if pivot == 0:
		return lista
	for i in lista:
		soma += i
	media = float(soma) / len(lista)
	for i in range(len(lista)-1,-1,-1):
		if lista[i] > media:
			for e in range(i,pivot-1):
				lista[e],lista[e+1] = lista[e+1], lista[e]
			pivot -= 1  
	return lista
