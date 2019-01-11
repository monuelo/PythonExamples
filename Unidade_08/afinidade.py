# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Afinidade Musical

def tem_afinidade(l1,l2):
	count = 0
	for i in range(len(l1)):
		for e in range(len(l2)):
			if l1[i] == l2[e]:
				count += 1
	if count >= 3:
		return True
	else:
		return False
