# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva
# Matrícula: 117110647
# Atividade: Maiores e Menores

pivot = int(raw_input())
maiores = []
menores = []
while True:
	numeros = int(raw_input())
	if numeros < 0:
		break
	if numeros > pivot:
		maiores.append(numeros)
	else:
		menores.append(numeros)

print menores
print pivot
print maiores
