# coding: utf-8
# Movimento Retilíneo Variado
# (c) Héricles Emanuel, UFCG, Programação 1

pos_inicial = float(raw_input("Posição inicial? "))
v_inicial = float(raw_input("Velocidade inicial? "))
tempo = float(raw_input("Tempo? "))
aceleracao = float(raw_input("Aceleração? "))

v_final = v_inicial + aceleracao * tempo
pos_final = pos_inicial + (v_inicial * tempo) + (aceleracao * (tempo ** 2)) / 2
v_media = v_inicial + ((aceleracao * tempo) / 2)

print "\nDados da questão"
print "================"
print "   Posição inicial: %.2f m" % pos_inicial
print "Velocidade inicial: %.2f m/s" % v_inicial
print "        Aceleração: %.2f m/s2" % aceleracao
print "             Tempo: %.2f s" % tempo
print "  Velocidade final: %.2f m/s" % v_final
print "  Velocidade média: %.2f m/s" % v_media
print "     Posição final: %.2f m" % pos_final
