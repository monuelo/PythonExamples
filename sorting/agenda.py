# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Agenda Telefônica

agenda = []
buscas = []
imprime = False
while True:
	operation = raw_input()
	if operation == "finalizar": 
		break
	if operation == "buscar":
		while True:
			nomes = raw_input()
			if nomes == "inserir" or nomes == "finalizar":
				operation = nomes
				break
			buscas.append(nomes)
	if operation == "inserir":
		num = int(raw_input())
		for i in range(num):
			nome = raw_input()
			numero = raw_input()
			agenda.append((nome, numero))
	if operation == "imprimir":
		imprime = True
	if operation == "finalizar":
		break


if len(buscas) >= 1:
	for e in range(len(agenda)):
		for i in range(len(buscas)):
			if buscas[i] == agenda[e][0]:
				print "Nome: %s" % agenda[e][0]
				print "Fone: %s" % agenda[e][1]
				print "----------"
	
if imprime:
	for i in range(len(agenda)):
		print "Nome: %s" % agenda[i][0]
		print "Fone: %s" % agenda[i][1]
		print "----------"