# coding: utf-8
# Custo Empregado
# (c) Héricles Emanuel, UFCG, Programação 1

salario = float(raw_input())
dias = float(raw_input())
transporte = float(raw_input())

fgts = salario * 0.08
inss_patrao = salario * 0.12

if salario <= 1317.07:
	inss_trab = salario * 0.08
elif salario >= 1317.08 and salario <= 2195.12:
	inss_trab = salario * 0.09
elif salario >= 2195.13:
	inss_trab = salario * 0.11

if dias * transporte > salario * 0.06:
	custo_mensal = salario + fgts + inss_patrao + ((transporte * dias) - (salario * 0.06))
	salario_liq = salario - inss_trab - (salario * 0.06)
else:
	custo_mensal = salario + fgts + inss_patrao 
	salario_liq = salario - inss_trab

print "O salário base é R$ %.2f" % salario
print "O custo mensal para o empregador é de R$ %.2f" % custo_mensal
print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % salario_liq