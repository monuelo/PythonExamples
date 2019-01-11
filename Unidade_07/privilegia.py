# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva
# Matrícula: 117110647
# Atividade: Privilegia Letra

def letra_magica(fila, letra):
	indice = 0
	for i in range(len(fila)):
		if fila[i][0] == letra.upper() or fila[i][0] == letra.lower():
			for p in range(i, indice, -1):
				fila[p], fila[p - 1] = fila[p - 1], fila[p]
			indice += 1
