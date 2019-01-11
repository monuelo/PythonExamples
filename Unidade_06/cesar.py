# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Minha Implementação para o Método join

def cesar(frase, chave):
	alphabet = []
	for i in range(26):
		alphabet.append(chr(ord("a") + i))
	for i in frase:
		letra = ord(i) + chave
	pos = 
	
	conta = 0
	while(conta < chave):
		conta += chave
		if(pos == 25):
			pos = 0
		else:
			pos = pos + 1
	return frase

print cesar("exemplo", 4)