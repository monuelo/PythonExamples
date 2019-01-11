# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Letras Coincidentes

palavra_1 = raw_input()
palavra_2 = raw_input()
coincidencias = 0
letras_coincidentes = []
menor_palavra = ""

if len(palavra_1) < len(palavra_2):
	menor_palavra = palavra_1
else:
	menor_palavra = palavra_2

for i in range(len(menor_palavra)):
	if palavra_1[i] == palavra_2[i]:
		coincidencias += 1
		letras_coincidentes.append((palavra_1[i], i + 1))

porcentagem = (coincidencias * 100) / (len(palavra_1) + len(palavra_2))

print "Letras coincidentes"
for e in letras_coincidentes:
	print "'%s' na posição %s" % (e[0], e[1])
print "Total de letras coincidentes: %i (%i%%)" % (coincidencias, porcentagem)