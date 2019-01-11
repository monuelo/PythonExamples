# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Soma de Matriz Interna

def soma_matriz_interna(M, p1, p2):
	soma = 0
	
	for x in range(p1[0], p2[0] + 1):
		for e in range(p1[1], p2[1] +1):
			soma += M[x][e]
	return soma


M2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
print soma_matriz_interna(M2, (1,1),(2,2))
