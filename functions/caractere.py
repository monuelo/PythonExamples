# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Mais Ocorrências de um Caractere

palavras = []
selecionadas = []

while True:
	word = raw_input()
	if word == "fim": break
	palavras.append(word)
letra = raw_input()
numero = int(raw_input())

for i in range(len(palavras)): 
	counter = 0
	for e in range(len(palavras[i])):
		if palavras[i][e] == letra: counter += 1
	if counter > numero:
		selecionadas.append(palavras[i])
if len(selecionadas) > 0:
	for p in selecionadas:
		print p
else: print "Nenhuma palavra encontrada."