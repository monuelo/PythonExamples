# coding: utf-8
# Caixas de Cerâmica
# (c) Héricles Emanuel, UFCG, Programação 1

cap_revestimento = float(raw_input("Capacidade de revestimento? "))

print "\n== Dados do vão a revestir =="
comprimento = float(raw_input("Comprimento? "))
largura = float(raw_input("Largura? "))
altura = float(raw_input("Altura? "))

area_total = (comprimento * largura) + ((comprimento * altura) * 4) 
caixas = area_total / 1.5

print "\n== Resultados =="
print "Área total a revestir: %.1f m2" % area_total
print "Número de caixas: %i" % caixas