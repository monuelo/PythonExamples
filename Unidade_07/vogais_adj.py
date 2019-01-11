# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva
# Matrícula: 117110647
# Atividade: Tem Vogais Adjacentes

def tem_vogais_adjacentes(palavra):
	vogais = "aAeEiIoOuU"
	isVogal = False
	for l in range(len(palavra) - 1):
		for v in range(len(vogais)):
			if palavra[l] == vogais[v]:
				for i in range(len(vogais)):
					if palavra[l + 1] == vogais[i]:
						isVogal = True
	if isVogal:
		print "sim"
	else:
		print "nao"

palavra = raw_input()
tem_vogais_adjacentes(palavra)
