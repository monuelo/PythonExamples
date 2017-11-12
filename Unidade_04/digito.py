# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Calcula DV

numero = raw_input()

resto = ((int(numero[0]) + int(numero[2])) * (int(numero[1]) + int(numero[3]))) % 11
if resto ==10:
	resto = "X"

print "%s-%s" % (numero, str(resto))