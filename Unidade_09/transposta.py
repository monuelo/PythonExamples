# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Transposta

def transposta(M):
	x = 0
	trans = []
	while x < len(M[0]):
		T = []
		for i in range(len(M)):
			T.append(M[i][x])
		trans.append(T)
		x += 1
	return trans

M = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3]]

print transposta(M)
