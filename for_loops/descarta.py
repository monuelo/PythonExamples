# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Descarta coincidente

descartados = []
aceitos = []
qtd_numeros = int(raw_input())
for i in range(qtd_numeros):
	num = raw_input()
	for n in range(len(num)):
		if int(num[n]) != n:
			aceitos.append(num)
			break
		elif int(num[n]) == n:
			descartados.append(num)
			break

print "---"
print "%i aceito(s)" % len(aceitos)
for a in range(len(aceitos)):
	print aceitos[a]
print "%i descartado(s)" % len(descartados)
for d in range(len(descartados)):
	print descartados[d]
