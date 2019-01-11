# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Valor Polinômio

def valor_polinomio(polinomio, valor):
	counter = 0
	resultante = 0
	for i in range(len(polinomio)):
		resultante += polinomio[i] * (valor ** counter)
		counter += 1
		
	return resultante