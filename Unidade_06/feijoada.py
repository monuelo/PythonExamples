# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Quantos Comeram?

def quantos_comeram(N, fila):
	comidas = 0
	for i in range(len(fila)):
		if fila[i] <= N:
			comidas += fila[i]
			N -= fila[i]
		elif fila[i] > N:
			break
	return comidas

assert quantos_comeram(10, [10, 10]) == 10
assert quantos_comeram(12, [10, 10]) == 10
assert quantos_comeram(2, [10, 10]) == 0
assert quantos_comeram(5, [2, 3, 5]) == 5