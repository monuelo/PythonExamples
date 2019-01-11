# coding: utf-8
# Segundo Maior e Segundo Menor
# (c) Héricles Emanuel, UFCG, Programação 1

num_1 = int(raw_input())
num_2 = int(raw_input())
num_3 = int(raw_input())
num_4 = int(raw_input())

print "Considerando os números %i, %i, %i e %i" % (num_1, num_2, num_3, num_4)
# Considerando o Primeiro número
maiores = 0
if num_1 < num_2:
	maiores += 1
if num_1 < num_3:
	maiores += 1
if num_1 < num_4:
	maiores += 1
if maiores == 2:
	print "O segundo menor número é %i" % num_1
elif maiores == 1:
	print "O segundo maior número é %i" % num_1

# Considerando o Segundo número
maiores = 0
if num_2 < num_1:
	maiores += 1
if num_2 < num_3:
	maiores += 1
if num_2 < num_4:
	maiores += 1
if maiores == 2:
	print "O segundo menor número é %i" % num_2
elif maiores == 1:
	print "O segundo maior número é %i" % num_2 

# Considerando o Terceiro número
maiores = 0
if num_3 < num_1:
	maiores += 1
if num_3 < num_2:
	maiores += 1
if num_3 < num_4:
	maiores += 1
if maiores == 2:
	print "O segundo menor número é %i" % num_3
elif maiores == 1:
	print "O segundo maior número é %i" % num_3

# Considerando o Quarto número
maiores = 0
if num_4 < num_1:
	maiores += 1
if num_4 < num_2:
	maiores += 1
if num_4 < num_3:
	maiores += 1
if maiores == 2:
	print "O segundo menor número é %i" % num_4
elif maiores == 1:
	print "O segundo maior número é %i" % num_4