# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Organiza Array com Duas Cores

def separa_duas_cores(lista, cor1, cor2):
	indice_cor1 = 0
	for i in range(len(lista)):
		if lista[i] == cor1:
			lista[indice_cor1], lista[i] = lista[i], lista[indice_cor1]
			indice_cor1 += 1

l1 = ['a', 'a', 'b', 'a', 'b']
assert separa_duas_cores(l1, 'b', 'a') == None
assert l1 == [ 'b', 'b', 'a', 'a', 'a']
