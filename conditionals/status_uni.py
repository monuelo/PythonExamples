# coding: utf-8
# Status Unidade
# Héricles Emanuel, UFCG, Programação 1

mtps = int(raw_input())

nota1 = float(raw_input())
total = nota1 

if mtps >= 2:
	nota2 = float(raw_input())
	total += nota2
	if mtps >= 3:
		nota3 = float(raw_input())
		total += nota3 - 0.5 * mtps
		if mtps >= 4:
			nota4 = float(raw_input())
			total += nota4
			
media = total / mtps

if media < 6.0:
	print "%.1f\nAluno ainda não aprovado na unidade" % media 
elif media >= 6.0:
	print "%.1f\nAluno aprovado na unidade" % media