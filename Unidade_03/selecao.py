# coding: utf-8
# Seleção Projeto
# (c) Héricles Emanuel, UFCG, Programação 1

cre = float(raw_input())
exp = int(raw_input())
nota = int(raw_input())

if cre < 7.0 and exp < 6:
	print "Candidato eliminado. CRE e experiência abaixo do limite."
elif cre < 7.0:
	print "Candidato eliminado. CRE abaixo do limite."
elif exp < 6:
	print "Candidato eliminado. Experiência abaixo do limite."
elif cre >= 7.0 and exp >= 6 and nota <= 3:
	print "Candidato classificado."
elif cre >= 7.0 and exp >=6 and nota > 3:
	print "Candidato aprovado." 