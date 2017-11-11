# coding: utf-8
# Conversão Fahrenheit
# (c) Héricles Emanuel, UFCG, Programação 1

grausf = float(raw_input())
grausc =  (grausf - 32) / 1.8
grausk = grausc + 273.15

print "Fahrenheit: %.3f F" % grausf
print "Celsius: %.3f C" % grausc
print "Kelvin: %.3f K" % grausk