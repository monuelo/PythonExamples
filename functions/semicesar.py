# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Minha Implementação para o Método join

def cesar(frase, chave):
	alphabet = []
	for i in range(26):
		alphabet.append(chr(ord("a") + i))
	criptografada  = ""

	for i in range(len(frase)):
		achou = False
		for e in range(len(alphabet)):
			if frase[i] == alphabet[e]:
				if (e + chave) > 25:
					criptografada += alphabet[(e + chave) % 26]
				else:
					criptografada += alphabet[(e + chave)]
				achou = True
		if achou == False:
			criptografada += frase[i]

	return criptografada

assert cesar('exemplo', 4) == 'ibiqtps'
assert cesar('Exemplo 2!', 4) == 'Ebiqtps 2!'