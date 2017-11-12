# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Desenhando uma Árvore de Natal

altura = int(raw_input())
num_o = 1
for i in range(altura - 1, -1, -1):
	print i * " " + num_o * "o"
	num_o += 2
print (altura - 1) * " " + "o"