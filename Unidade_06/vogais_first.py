# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva
# Matrícula: 117110647
# Atividade: Vogais primeiro

def vogais_primeiro(frase):
	vogal = ""
	consoantes = ""
	vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
	for i in range(len(frase)):
		evogal = False
		for v in vogais:
			if frase[i] == v:
				evogal = True
		if evogal:
			vogal += (frase[i])
		else:
			consoantes += (frase[i])

	return vogal + consoantes

assert vogais_primeiro("exemplo") == "eeoxmpl"
assert vogais_primeiro("Programacao 1") == "oaaaoPrgrmc 1"