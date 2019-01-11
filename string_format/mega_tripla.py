# coding: utf-8
# Mega Tripla
# (c) Héricles Emanuel, UFCG, Programação 1

num_01 = abs(int(raw_input()))
num_02 = abs(int(raw_input()))
num_03 = abs(int(raw_input()))

resto_01 = (num_01 % 11)
resto_02 = (num_02 % 11)
resto_03 = (num_03 % 11)

print "%02i-%02i-%0t2i" % (resto_01, resto_02, resto_03)