# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva
# Matrícula: 117110647
# Atividade: MinMax Sort = Selection Sort Duplicado

def minmax_sort(lista):
	indice_menor = 0
	indice_maior = 0
	indice_alpha = 0
	indice_omega = len(lista) - 1
	
	while indice_alpha != len(lista) / 2 or indice_omega != len(lista) / 2
		for i in range(len(lista)):
			if lista[i] < menor:
				indice_menor = i
			if lista[i] > maior:
				indice_maior = i
		lista[indice_alpha] = lista[indice_menor]
		lista[indice_omega] = lista[indice_maior]
		indice_alpha += 1
		indice_omega += 1
	
