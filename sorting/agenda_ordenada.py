# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Agenda Ordenada

def insere(lista,nome):
	lista.append(nome)
	for i in range(len(lista)-1,0,-1):
		if lista[i] < lista[i-1]:
			lista[i],lista[i-1] = lista[i-1], lista[i]
	for e in range(len(lista)):
		if lista[e] == nome:
			print "* %s" % nome
		else:
			print lista[e]
	print "----"
lista = []
while True:
	nome = raw_input()
	if nome == "####": 
		break
	insere(lista, nome)
