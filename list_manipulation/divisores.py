# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Seleciona Divisores em uma Lista

def filtra_divisores(lista):
	for i in range(len(lista) -1, -1, -1):
		soma_algarismos = 0
		string = str(lista[i])
		for e in range(len(string)):
			soma_algarismos += int(string[e])
			print soma_algarismos
		if lista[i] % soma_algarismos != 0:
			lista.pop(i)
	print lista

lista1 = [333,121,81]
filtra_divisores(lista1)
