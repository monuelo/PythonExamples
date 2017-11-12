 # coding: utf-8
# Segundo Maior e Segundo Menor
# (c) Héricles Emanuel, UFCG, Programação 1

# Entrada de Números

num_1 = int(raw_input())
num_2 = int(raw_input())
num_3 = int(raw_input())
num_4 = int(raw_input())

print "Considerando os números %i, %i, %i e %i" %(num_1, num_2, num_3, num_4)

# Ordenamento dos Números

if num_1 > num_2:
  num_2, num_1 = num_1, num_2
if num_3 > num_4:
  num_3, num_4 = num_4, num_3
if num_1 > num_3:
  num_1, num_3 = num_3, num_1 
if num_2 > num_4:
  num_2, num_4 = num_4, num_2 
if num_2 > num_3:
  num_2, num_3 = num_3, num_2

print "O segundo menor número é %i" % num_2
print "O segundo maior número é %i" % num_3