# coding: utf-8
# Número de Fatias
# (c) Héricles Emanuel, UFCG, Programação 1

convidados = float(raw_input())
op1_inteira = 32 / convidados
op1_resto = 32 % convidados


print "Opção 1: %d fatias cada, %i de resto" % (op1_inteira, op1_resto)
print "Opção 2: %.2f fatias cada" % op1_inteira
