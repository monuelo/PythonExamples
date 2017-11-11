
# coding: utf-8
# Vazão da Água
# (c) Héricles Emanuel, UFCG, Programação 1

import math

velocidade_de_vazao = float(raw_input())			   # Em m/s (metros por segundo)
diametro_do_cano = float(raw_input())				   # Em metros
tempo = int(raw_input())                               # Em segundos

seccao = (math.pi * diametro_do_cano**2) / 4
vazao = velocidade_de_vazao * seccao * 1000            #convertendo para litros
quantidade_de_agua = tempo * vazao
print "Quantidade de água =", quantidade_de_agua, "litros."
