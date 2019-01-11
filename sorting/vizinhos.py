# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Resolve vizinhos

def resolve_vizinhos(seq):
	for i in range(len(seq) - 1):
		if seq[i] == seq[i + 1]:
			seq[i] += 1
		if seq[i] == seq[i - 1]:
			seq[i] += 1
			
	return seq


seq = [1,2,5,5,8,4]
resolve_vizinhos(seq)
assert seq == [1,2,6,5,8,4]

seq = [1,6,5,5,8,4]
resolve_vizinhos(seq)
assert seq == [1,6,7,5,8,4]

seq = [1,6,5,5,5,8,4]
resolve_vizinhos(seq)
assert seq == [1,6,7,6,5,8,4]