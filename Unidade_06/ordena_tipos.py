# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Ordena Tipos

def ordena_tipos(lista):
	retorna = []
	for i in lista:
		if i.isdigit(): retorna.append(i)
	for i in lista:
		if i.isalpha(): retorna.append(i)
	for i in lista:
		if not i.isalpha() and not i.isdigit(): retorna.append(i)
	return retorna

print ordena_tipos(['1a', '2', 'e', '4', '4.4', 'e6', '8'])