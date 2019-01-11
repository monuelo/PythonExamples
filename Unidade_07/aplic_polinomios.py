# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Aplicação Polinômios

def valor_polinomio(polinomio, valor):
	counter = 0
	resultante = 0
	for i in range(len(polinomio)):
		resultante += int(polinomio[i]) * (valor ** counter)
		counter += 1
		
	return resultante

while True:
	valores = []
	entradas = raw_input()
	if entradas == "fim":
		break
	if entradas[0] == "p":
		polinomio = entradas.split()
		polinomio.pop(0)
		print "novo polinomio"
	else:
		print valor_polinomio(polinomio, int(entradas))