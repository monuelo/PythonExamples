# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Minha Implementação para o Método join

def cesar(frase, chave):
	alphabet = []
	for i in range(26):
		alphabet.append(chr(ord("a") + i))
	i_frase = 0
	i_letra = 0
	criptografada  = ""
	for e in range(len(alphabet)):
		if i_frase == len(frase) - 1:
			return criptografada
		if frase[i_frase] == alphabet[e]:
			i_letra = e + chave
		if i_letra > 25:
			i_letra = i_letra % 26
		criptografada += alphabet[i_letra]
		i_frase += 1
print cesar('exemplo', 4)

