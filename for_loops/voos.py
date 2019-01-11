# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Autorização Voos

tempo = int(raw_input())
voos = int(raw_input())
autorizados = 0
for i in range(voos):
	tempo_aviao = int(raw_input())
	if tempo_aviao <= tempo:
		autorizados += 1
		tempo -= tempo_aviao
print "%i voo(s) autorizados." % (autorizados)