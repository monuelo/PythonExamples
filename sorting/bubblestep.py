# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva
# Matrícula: 117110647
# Atividade: Um Passo do Algoritmo BubbleSort (Bubble Step)

while True:
	string = ""
	seq = raw_input().split()

	if seq[0] == "fim":
		break
	for i in range(len(seq) - 1):
		if int(seq[i]) > int(seq[i + 1]):
			seq[i], seq[i + 1] = seq[i + 1], seq[i]
	for i in seq:
		string += i
		string += " "
	print string.strip()
