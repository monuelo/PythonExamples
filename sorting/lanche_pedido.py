# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Lanche mais Pedido

def lanchemaispedido(pedidos):
	comida = None
	for i in range(len(pedidos)):
		counter = 0
		for e in range(len(pedidos)):
			if pedidos[i] == pedidos[e]:
				counter += 1
	if counter > len(pedidos) / 2:
		comida = pedidos[i]

	return comida

ines = ['tapioca','tapioca','salada','bolo','misto','tapioca', 'tapioca']
marcos = ['suco','coxinha','suco','misto','folhado']

assert lanchemaispedido(ines) == 'tapioca'
assert lanchemaispedido(marcos) == None