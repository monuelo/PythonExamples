# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Encontra Elemento

elemento = raw_input()
sequencia = raw_input().split()

for i in sequencia:
	encontrou = False
	if i == elemento:
		encontrou = True
		break
if encontrou:
	print "sim"
else:
	print "não" 