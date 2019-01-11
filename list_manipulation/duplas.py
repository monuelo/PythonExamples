# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Organizando as Duplas do Projeto

def insere_nome(aluno1, duplas, aluno2):
	indice = len(duplas)
	for i in range(len(duplas)):
		if duplas[i] == aluno2:
			indice = i
	duplas.append(aluno1)
	for e in range(len(duplas) - 1, indice, -1):
		duplas[e], duplas[e - 1] = duplas[e - 1], duplas[e]
