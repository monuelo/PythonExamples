# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Soma Linha e Coluna
def soma_linha_e_coluna(matriz,l,c):
	soma = 0
	for e in range(len(matriz[l])):
		soma += matriz[l][e]
	for n in range(len(matriz)):
		soma += matriz[n][c]
	soma -= 2*(matriz[l][c])
	return soma

matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [3, 2, 3, 2, 1],
]

print soma_linha_e_coluna(matriz,0,0)
