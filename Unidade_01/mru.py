# coding: utf-8
# Movimento Retilíneo Uniforme (MRU)
# (c) Héricles Emanuel, UFCG, Programação 1

pos_inicial = float(raw_input())			# Em metros
velocidade_movel = float(raw_input())		# Em m/s (metros por segundo)
instante = float(raw_input())				# 
pos_final = velocidade_movel * instante + pos_inicial

print "Posição final do móvel"
print "S(%.1f) = %.1f m" % (instante, pos_final)