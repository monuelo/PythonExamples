# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Busca Todos

def busca_matriz(m,e):
	busca = []
	for i in range(len(m)):
		for n in range(len(m[i])):
			if m[i][n] == e:
				busca.append((i, n))
	return busca

matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [1, 2, 3, 2, 1],
]
print busca_matriz(matriz,3)
