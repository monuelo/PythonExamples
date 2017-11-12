# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Primeira Vogal

palavra = raw_input()

vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
for i in range(0, len(palavra)):
	n_vogal = 0
	if palavra[i] in vogais:
		n_vogal += 1
		print  palavra[i]
		break
if n_vogal == 0:
	print "-"