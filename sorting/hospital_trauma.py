# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Hospital de Trauma

red = 0
orange = 0
yellow = 0
green = 0
blue = 0
pacientes = []
while True:
	paciente = ()
	nome = raw_input().split()
	if nome[0] == "fim":
		break
	if (nome[1] == "vermelho"):
		paciente = (nome[0], 0)
		red += 1
	elif (nome[1] == "laranja"):
		paciente = (nome[0], 1)
		orange += 1
	elif (nome[1] == "amarelo"):
		paciente = (nome[0], 2)
		yellow += 1 
	elif (nome[1] == "verde"):
		paciente = (nome[0], 3)
		green += 1
	elif (nome[1] == "green"):
		paciente = (nome[0], 4)
		blue += 1
	pacientes.append(paciente)

for i in range(len(pacientes) - 1, 0, -1):
	if pacientes[i][1] < pacientes[i - 1][1]:
		pacientes[i], pacientes[i - 1] = pacientes[i - 1], pacientes[i]

for p in range(len(pacientes)):
	print pacientes[p][0]
print "---"
print "vermelho: %i" % red
print "laranja: %i" % orange
print "amarelo: %i" % yellow
print "verde: %i" % green
print "azul: %i" % blue