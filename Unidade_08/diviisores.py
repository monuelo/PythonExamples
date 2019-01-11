# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Remove os n últimos divisores de K

def remove_divisores_k(lista, k, n):
	count = 0
	for i in range(len(lista) - 1, -1, -1):
		if count == n:
			break
		if k % lista[i] == 0:
			lista.pop(i)
			count += 1
	print lista
l1 = [1, 8, 1, 2, 2, 13, 4, 17]
remove_divisores_k(l1, 4, 2)
