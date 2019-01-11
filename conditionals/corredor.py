# coding: utf-8
# Classifica Corredor
# (c) Héricles Emanuel, UFCG, Programação 1

velocidade = float(raw_input())
tempo = float(raw_input())

v_media = velocidade * tempo

if v_media < 10.0:
	print "Velocidade: %.1fkm/h. Corredor amador." % v_media
elif v_media > 10.0 and v_media < 15.0:
	print "Velocidade: %.1fkm/h. Corredor aspirante." % v_media
elif v_media > 15.0:
	print "Velocidade: %.1fkm/h. Corredor profissional." % v_media