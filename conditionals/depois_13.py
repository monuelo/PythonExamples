# coding: utf-8
# Depois do 13 Nada
# (c) Héricles Emanuel, UFCG, Programação 1

num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

if num1 == 13:
	print "0"
elif num2 == 13:
	soma = num1
	print soma
elif num3 == 13 and num1 + num2 != 13:
	soma = num1 + num2
	print soma
elif num3 == 13 and num1 + num2 == 13:
	print "0"
elif num1 != 13 and num2 != 13 and num3 != 13 and num1 + num2 + num3 != 13:
	soma = num1 + num2 + num3
	print soma
elif num1 != 13 and num2 != 13 and num3 != 13 and num1 + num2 + num3 == 13:
	print "0"