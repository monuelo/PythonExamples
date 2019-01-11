# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Zera Acima ou Abaixo

def zera_acima_ou_abaixo(m):
	
	def zera_acima():
		w = 0
		for n in range(len(m)):
			for e in range(len(m[n]) - 1, w, -1):
				m[n][e] = 0
			w += 1
	def zera_abaixo():
		x = 0
		for i in range(1,len(m)):
			for e in range(x + 1):
				m[i][e] = 0
			x += 1
	
	uppersum = 0
	undersum = 0
	w = 0
	
	for n in range(len(m)):
		for e in range(len(m[n]) - 1, w, -1):
			uppersum += m[n][e]
		w += 1
	x = 0
	for i in range(1,len(m)):
		for e in range(x + 1):
			undersum += m[i][e]
		x += 1
		
	if uppersum > undersum:
		zera_acima()
	elif undersum > uppersum:
		zera_abaixo()
	else:
		zera_acima()
		zera_abaixo()
