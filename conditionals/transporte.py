# coding: utf-8
# Transporte Modificado
# (c) Héricles Emanuel, UFCG, Programação 1
import math
passageiros = float(raw_input())
valor_disponivel = float(raw_input())
custo1 = passageiros * 100
custo2 = math.ceil(passageiros / 4) * 200
custo3 = passageiros * 22

if valor_disponivel >= custo1:
	print "TAV. R$ %.2f" % custo1
elif valor_disponivel >= custo2:
	print "Táxi. R$ %.2f" % custo2
elif valor_disponivel >= custo3:
	print "Ônibus. R$ %.2f" % custo3
elif valor_disponivel < custo1 and valor_disponivel < custo2 and valor_disponivel < custo3:
	print "Não é possível realizar a viagem."	