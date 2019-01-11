# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Inserção ordenada do último elemento de uma lista

def insere_ordenado_ultimo(lista):
	for i in range(len(lista)-1,0,-1):
		if lista[i] < lista[i-1]:
			lista[i],lista[i-1] = lista[i-1], lista[i]
	return lista

l1 = [2,6,9,11,13,5]
print insere_ordenado_ultimo(l1)