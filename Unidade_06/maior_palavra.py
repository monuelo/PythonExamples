# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Naior Palavra de Uma Frase

def maior_palavra(frase):
	palavra = ""
	maior_palavra = ""
	for i in frase:
		if i != " ":
			palavra += i
		else:
			if len(palavra) >= len(maior_palavra):
				maior_palavra = palavra
			palavra = ""
	if len(palavra) >= len(maior_palavra):
		maior_palavra = palavra

	return maior_palavra

assert maior_palavra("eu acredito que seja um bom exemplo") == "acredito"