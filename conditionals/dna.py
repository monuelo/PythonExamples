# coding: utf-8
# DNA
# (c) Héricles Emanuel, UFCG, Programação 1

dna1 = raw_input()
dna2 = raw_input()
dna3 = raw_input()

if len(dna1) <= len(dna2) and len(dna1) <= len(dna3):
	print dna1, len(dna1)
elif len(dna2) < len(dna1) and len(dna2) <= len(dna3):
	print dna2, len(dna2)
elif len(dna3) < len(dna2) and len(dna3) < len(dna1):
	print dna3, len(dna3)
