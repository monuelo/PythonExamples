# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Mais consoantes
vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
counter = 0
while True:
	palavra = raw_input()
	n_vogais = 0
	for i in range(len(palavra)):
		for v in vogais:
			if palavra[i] == v:
				n_vogais += 1
	counter += 1
	if n_vogais < (len(palavra) / 2.0): break
print counter