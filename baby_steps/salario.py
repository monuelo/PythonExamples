# coding: utf-8
# Salário
# (c) Héricles Emanuel, UFCG, Programação 1

salario_bruto = float(raw_input())
horas_de_trabalho = int(raw_input())
hora_bruta = salario_bruto / horas_de_trabalho
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto * 0.76
hora_liquida = salario_liquido / horas_de_trabalho

print "Salário Bruto =", salario_bruto
print "Hora Bruta =", hora_bruta
print "Desconto IR =", ir
print "Desconto INSS =", inss
print "Desconto Sindicato =", sindicato
print "Salário Líquido =", salario_liquido
print "Hora Líquida =", hora_liquida
