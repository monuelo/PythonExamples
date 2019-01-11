# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Agenda Telefônica
agenda = []
buscas = []
impressas = []
def inserir():
	num = int(raw_input())
	for i in range(num):
		nome = raw_input()
		numero = raw_input()
		agenda.append((nome, numero))
def buscar():
	nomes = raw_input()
	buscas.append(nomes)

def insertionsort(lista,numero):
	lista.append(numero)
	for i in range(len(lista)-1,0,-1):
		if lista[i] < lista[i-1]:
			lista[i],lista[i-1] = lista[i-1], lista[i]
	return lista

imprime = False
while True:
	operation = raw_input()
	if operation == "buscar":
		buscar()
	if operation == "inserir":
		inserir()
	if operation == "imprimir":
		imprime = True
	if operation == "finalizar":
		break

if len(buscas) >= 1:
	existent = False
	for i in range(len(buscas)):
		for e in range(len(agenda)):
			if buscas[i] == agenda[e][0]:
				print "Nome: %s" % agenda[e][0]
				print "Fone: %s" % agenda[e][1]
				print "----------"
				existent = True
		if existent == False:
			print "Nome inexistente"
			print "----------"
if imprime:
	for i in range(len(agenda)):
		insertionsort(impressas, agenda[i])
for i in range(len(impressas)):
	print "Nome: %s" % impressas[i][0]
	print "Fone: %s" % impressas[i][1]
	print "----------"