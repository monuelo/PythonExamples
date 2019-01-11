# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Remove Números Opostos Adjacentes

def anula(lista):
	while True:
		existe = False
		for i in range(len(lista) - 1):
			for e in range(len(lista)):
				if lista[i] + lista[e] == 0:
					lista.pop(e)
					lista.pop(i)
					existe = True
					break
			if existe == True:
				break
		if existe == False:
			break
lista = [1,4,-4,2,4,3,5,-2,-1]
anula(lista)
