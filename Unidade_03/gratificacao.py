# coding: utf-8
# Gratificação Natalina
# (c) Héricles Emanuel, UFCG, Programação 1

codigo = int(raw_input())
faltas = int(raw_input())
gratif = None

# Cargos não gratificados

if codigo == 1:
	print "Deverá receber em dezembro R$ 25000.00."
elif codigo == 2:
	print "Deverá receber em dezembro R$ 15000.00."

# Cargos Contemplados

elif codigo == 3 and faltas == 0:
	gratif = 500.00 and salario = 8000.00
	print "Valor da gratificação R$ %.2f\nDeverá receber em dezembro R$ %.2f" % (gratif, salario + gratif)
elif codigo == 3 and faltas > 0:
	gratif = (235 - faltas) * 2.0 and salario = 8000.00
	print "Valor da gratificação R$ %.2f\nDeverá receber em dezembro R$ %.2f" % (gratif, salario + gratif)
elif codigo == 4 and faltas == 0:
	gratif = 300.00 and salario = 5000.00
	print "Valor da gratificação R$ %.2f\nDeverá receber em dezembro R$ %.2f" % (gratif, salario + gratif)
elif codigo == 4 and faltas > 0:
	gratif = (235 - faltas) * 1.0 and salario = 5.000
	print "Valor da gratificação R$ %.2f\nDeverá receber em dezembro R$ %.2f" % (gratif, salario + gratif)
elif codigo == 5 and faltas == 0:
	gratif = 200.00 and salario = 2800.00
	print "Valor da gratificação R$ %.2f\nDeverá receber em dezembro R$ %.2f" % (gratif, salario + gratif)
