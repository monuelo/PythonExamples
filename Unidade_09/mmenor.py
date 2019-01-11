# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Matriz Menor

def matriz_menor(m1, m2):
	menor = []
	for i in range(len(m2)):
		main = []
		for e in range(len(m2[i])):
			if m1[i][e] < m2[i][e]:
				main.append(m1[i][e])
			else:
				main.append(m2[i][e])
		menor.append(main)
	return menor
