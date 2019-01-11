# coding: utf-8
# Segundo Maior e Segundo Menor
# (c) Héricles Emanuel, UFCG, Programação 1

num_1 = int(raw_input())
menor = num_1
maior = num_1
num_2 = int(raw_input())
if num_2 < menor:
	menor = num_2
if num_2 > maior:
	maior = num_2
num_3 = int(raw_input())
if num_3 < menor:
	menor = num_3
if num_3 > maior:
	maior = num_3
num_4 = int(raw_input())
if num_3 < menor:
	menor = num_4
if num_3 > maior:
	maior = num_4
print "Considerando os números %i, %i, %i e %i" % (num_1, num_2, num_3, num_4)

resto1 = menor
resto2 = maior
if num_1 != menor and num_1 != maior:
	resto1 = num_1