# coding: utf-8
# Nota na Final
# Héricles Emanuel, UFCG, Programação 1

print "== Estágio 1 =="
pd1 = float(raw_input("Peso? ")) # Peso da disciplina 1
nd1 = float(raw_input("Nota? ")) # Nota da disciplina 1
print "== Estágio 2 =="
pd2 = float(raw_input("Peso? ")) # Peso da disciplina 2
nd2 = float(raw_input("Nota? ")) # Nota da disciplina 2
print "== Estágio 3 =="
pd3 = float(raw_input("Peso? ")) # Peso da disciplina 3
nd3 = float(raw_input("Nota? ")) # Nota da disciplina 3

media_parcial = (pd1 * nd1 + pd2 * nd2 + pd3 * nd3) / (pd1 + pd2 + pd3)
nota_necessaria = (5.0 - ((media_parcial) * 0.6)) / 0.4
nota_necessaria2 = (7.0 - ((media_parcial) * 0.6)) / 0.4


print "== Resultados =="
print "Média parcial: %.1f" % media_parcial
print "Nota na final, pra média 5.0 = %.1f" % nota_necessaria
print "Nota na final, pra média 7.0 = %.1f" % nota_necessaria2
