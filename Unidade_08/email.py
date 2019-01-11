# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Email

def encontra_email_perdido(l1, l2):
	for i in range(len(l1)):
		confere = False
		for e in range(len(l2)):
			if l1[i] == l2[e]:
				confere = True
		if confere == False:
			return l1[i]
	return l1
