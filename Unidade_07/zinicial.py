# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Z Inicial

def z_inicial(lista):
	n_palavras = 0
	for i in range(len(lista)):
		if lista[i][0] == "z" or lista[i][0] == "Z":
			n_palavras += 1
	print n_palavras


lista = raw_input().split(" ")
z_inicial(lista)