# coding: utf-8
# Segundo Maior e Segundo Menor
# (c) Héricles Emanuel, UFCG, Programação 1

num1 = int(raw_input())

maior = num1
menor = num1
aux1 = None
aux = None

num2 = int(raw_input())
if num2 > maior:
  maior = num2
if num2 < menor:
  menor = num2
num3 = int(raw_input())
if num3 > maior:
  maior = num3
if num3 < menor:
  menor = num3
num4 = int(raw_input())
if num4 > maior:
  maior = num4
if num4 < menor:
  menor = num4
print "Considerando os números %i, %i, %i e %i" % (num1, num2, num3, num4)

if num1 != maior and num1 != menor:
  aux1 = num1

if num2!= maior and num2 != menor:
  aux1 = num2
  
if num3 != maior and num3 != menor:
  aux1 = num3
  
if num4 != maior and num4 != menor:
  aux1 = num4
  
if num2 != maior and num2 != menor and num2 != aux1:
  aux = num2
if num3 != maior and num3 != menor and num3 != aux1:
  aux = num3
if num4 != maior and num4 != menor and num4 != aux1:
  aux =  num4 
if aux == None:
  print "O Segundo menor número é %i\nO Segundo maior número é %i" % (aux1, aux1)
else:
  print "O Segundo menor número é %i\nO Segundo maior número é %i" % (aux, aux1) if aux1 > aux else "O Segundo menor número é %i\nO Segundo maior número é %i" % (aux1, aux)
  
  
  
  