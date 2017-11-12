# coding: utf-8
# Custo INSS
# (c) Héricles Emanuel, UFCG, Programação 1

salario = float(raw_input())

inss_empregador = salario * 0.12

if salario <= 1317.07:
	inss_trab = salario * 0.08
elif salario >= 1317.08 and salario <= 2195.12:
	inss_trab = salario * 0.09
elif salario >= 2195.13:
	inss_trab = salario * 0.11

print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % inss_empregador
print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % inss_trab