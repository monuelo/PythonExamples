# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Inverte 3a3

def inverte3a3(s):
	string = ""
	lista = []
	for i in range(len(s)):
		lista.append(s[i])
	for e in range(len(lista)-1, -1, -3):
		string += lista[e - 2]
		string += lista[e - 1]
		string += lista[e]
	return string

print inverte3a3("paisimtio")
