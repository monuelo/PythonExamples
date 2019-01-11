# coding: utf-8
# Construção de Condomínio
# (c) Héricles Emanuel, UFCG, Programação 1

comprimento = float(raw_input())
largura = float(raw_input())
area_casa = float(raw_input())

area_terreno = comprimento * largura
qtd_casa = area_terreno / area_casa

print "%i casa(s) pode(m) ser construída(s) no terreno." % qtd_casa