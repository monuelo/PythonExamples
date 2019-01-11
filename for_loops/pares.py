# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Pares de Múltiplos

numeros = raw_input().split(" ")
fator = float(raw_input())
pares = []

for i in range(0, len(numeros)):
	numeros[i] = int(numeros[i])

for i in range(0, len(numeros)- 1):
	if numeros[i] * fator == numeros[i + 1] or numeros[i] / fator == numeros[i + 1]:
		pares.append((numeros[i], numeros[i + 1]))

print "%i par(es)" % len(pares)

for i in range(0, len(pares)):
	print pares[i][0], pares[i][1]