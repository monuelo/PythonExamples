# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Imprime Sequencias de Números Inteiros

n_alvo = int(raw_input())
select = []
seq_n = 0

while True:
	string = ""
	num_seq = 0
	seq = raw_input().split(" ")
	if seq[0] == "fim":
		break
	media = len(seq) / 2
	seq_n += 1
	for i in range(len(seq) - 1):
		if int(seq[i]) > n_alvo:
			num_seq += 1
	for n in seq:
		string += (n)
		string += " "
	if num_seq >= n_alvo:
		print "sequencia %i: %s" % (seq_n, string.strip())
		print ""