# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Imprime Sequencias de Números Inteiros

n_alvo = int(raw_input())
select = []
seq_n = 0

while True:
	string = ""
	num_sequencia = 0
	seq = raw_input().split(" ")
	if seq[0] == "fim": break
	media = len(seq) / 2
	seq_n += 1
	for i in range(len(seq)):
		if int(seq[i]) > n_alvo: num_sequencia += 1
	for n in seq:
		string += (n)
		string += " "
	if num_sequencia > media:
		print "sequencia %i: %s" % (seq_n, string.strip())
