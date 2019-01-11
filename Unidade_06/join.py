# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Minha Implementação para o Método join

def meu_join(delimitador, sequencia):
	sstring = []
	string = ""
	for i in range(len(sequencia)):
		string += sequencia[i]
		if i != len(sequencia) - 1:
			string += delimitador

	return string

assert meu_join("*", "abc") == "a*b*c"
assert meu_join("*", ["a", "b", "c"]) == "a*b*c"