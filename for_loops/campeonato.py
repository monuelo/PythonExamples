# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Ataque mais positivo de um campeonato

n_times = int(raw_input())
lista = []
maior_atual = 0
total_gols = 0
for i in range(n_times):
	time = raw_input()
	gol = int(raw_input())
	if gol > maior_atual:
		maior_atual = gol
	total_gols += gol
	lista.append(time)
	lista.append(gol)

print "Time(s) com melhor ataque (%i gol(s)):" % maior_atual
for e in range(len(lista)):
	if lista[e] == maior_atual:	
		print lista[e - 1]
print "\nMédia de gols marcados: %.1f" % (float(total_gols / float(n_times)))

