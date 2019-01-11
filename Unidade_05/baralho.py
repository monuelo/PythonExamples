# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Guerra Baralho

jogador1 = 0
jogador2 = 0
empates = 0
cartas = raw_input().split(" ")

while cartas != ['0', '0']:
	if int(cartas[0]) > int(cartas[1]):
		jogador1 += 1
	elif int(cartas[0]) < int(cartas[1]):
		jogador2 += 1
	elif (cartas[0]) == (cartas[1]):
		empates += 1
	cartas = raw_input().split(" ")

print "Jogador 1: %i, Jogador 2: %i, Empates: %i" % (jogador1, jogador2, empates)