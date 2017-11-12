# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Ordem Alfabética

num_palavras = int(raw_input())
words = []
antes = []
depois = []

for i in range(0, num_palavras):
	palavra = raw_input()
	words.append(palavra)

print "---"
referencial = raw_input()

for word in words:
	if word != referencial:
		if word < referencial:
			antes.append(word)
		else:
			depois.append(word)

print "%i antes" % len(antes)
print "%i depois" % len(depois)