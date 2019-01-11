# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Classifica Letra como Vogal ou Consoante

palavra = raw_input()

vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
for i in range(0, len(palavra)):
	encontrou = False
	for vogal in vogais:
		if palavra[i] == vogal:
			encontrou = True
			break
	if encontrou:
		print  "<%s> sim" % palavra[i]
	else:
		print "<%s> nao" % palavra[i]