# coding: utf-8
# Pedágio
# (c) Héricles Emanuel, UFCG, Programação 1

veiculo = raw_input()
if veiculo == "Ônibus":
	eixo = int(raw_input())
	tarifa = 11.40 * eixo
elif veiculo == "Caminhão":
	eixo = int(raw_input())
	tarifa = 9.60 * eixo
elif veiculo == "Automóvel utilitário":
	tarifa = 11.40
elif veiculo == "Motocicleta":
	tarifa = 5.70

if veiculo == "Ônibus" or veiculo == "Caminhão" or veiculo == "Automóvel utilitário" or veiculo == "Motocicleta":
	print "Valor a pagar: R$ %.2f." % tarifa
else:
	print "Veículo não cadastrado."