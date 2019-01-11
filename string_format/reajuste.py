# coding: utf-8
# Percentual de Reajuste
# (c) Héricles Emanuel, UFCG, Programação 1

valor_atual = float(raw_input("Valor atual? "))
novo_valor = float(raw_input("Novo valor? "))

reajuste = (novo_valor - valor_atual)
porc_reajuste = (reajuste / valor_atual) * 100.0

print "Reajuste de %.1f%%" % porc_reajuste