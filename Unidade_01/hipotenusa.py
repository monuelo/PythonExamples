# coding: utf-8
# Cálculo de Hipotenusa
# (c) Héricles Emanuel, UFCG, Programação 1
import math

cateto1 = float(raw_input("Medida do Cateto 1? "))
cateto2 = float(raw_input("Medida do Cateto 2? "))

hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))

print "Medida da Hipotenusa: %.2f" % hipotenusa