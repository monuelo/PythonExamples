# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Quantos Comeram?

def soma_diminui_vizinhos(lista):
	result = 0
	if lista == []:
		return result
	else:
		result += lista[0]
		for i in range(1, len(lista)):
		 	if(i % 2 == 0):
		 		result -= lista[i]
		 	else:
		 		result += lista[i]
	return result

lista = [1,2,3]
assert soma_diminui_vizinhos(lista) == 0