# coding: utf-8
# Gratificação Natalina
# Héricles Emanuel, UFCG, Programação 1
 
codigo = int(raw_input())
gratif = None
salario = None

if codigo == 1:
    print "Deverá receber em dezembro R$ 25000.00."
elif codigo == 2:
    print "Deverá receber em dezembro R$ 15000.00."
elif codigo != 1 and codigo != 2:
    faltas = int(raw_input())
    if codigo == 3 and faltas == 0:
        gratif = 500.00
        salario = 8000.00
    elif codigo == 3 and faltas > 0:
        gratif = (235 - faltas) * 2.0
        salario = 8000.00
    elif codigo == 4 and faltas == 0:
       gratif = 300.00
       salario = 5000.00
    elif codigo == 4 and faltas > 0:
       gratif = (235 - faltas) * 1.0
       salario = 5000.00
    elif codigo == 5 and faltas == 0:
       gratif = 200.00
       salario = 2800.00
    elif codigo == 5 and faltas > 0:
        gratif = (235 - faltas) * 0.70
        salario = 2800.00


if codigo != 1 and codigo != 2:
    total = gratif + salario
    print "Valor da gratificação R$ %.2f.\nDeverá receber em dezembro R$ %.2f." % (gratif, total)
