# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva
# Matrícula: 117110647
# Atividade: Elimina Menores

def elimina_menores(num, lista):
	removed = 0
	for i in range(len(lista) - 1, -1, -1):
		if lista[i] < num:
			lista.pop(i)
			removed += 1
	return removed
	
lista1 = [100,200,300,400]
assert elimina_menores(100, lista1) == 0
assert lista1 == [100,200,300,400]
