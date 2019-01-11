# coding: utf-8
# Perímetro de Retângulo
# (c) Héricles Emanuel, UFCG, Programação 1

# Entrada em milímetros
base = int(raw_input()) 
altura = int(raw_input())

perimetro = 2*(base + altura)

# Convertendo de milímetro para centímetros, como exige na saída
perimetro = perimetro * 0.1 

print "O perímetro resultante (em cm) é %.2f." % perimetro