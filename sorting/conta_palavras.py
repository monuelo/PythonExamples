# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Conta Palavras

def conta_palavras(k, palavras):
	letras = 0
	lista_palavras = palavras.split(":")
	for i in range(len(lista_palavras)):
		if len(lista_palavras[i]) >= k:
			letras += 1
	return letras

print conta_palavras(5, "zero:um:dois:tres:quatro:cinco")