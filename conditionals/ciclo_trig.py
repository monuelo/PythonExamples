# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Ciclo Trigonométrico
 
angulo = int(raw_input())
 
if angulo > 360:
    angulo = (angulo % 360)
else: 
    angulo = angulo
    
if angulo > 0 and angulo < 90:
    print "Quadrante 1"
elif angulo > 90 and angulo < 180:
    print "Quadrante 2"
elif angulo > 180 and angulo < 270:
    print "Quadrante 3"
elif angulo > 270 and angulo < 360:
    print "Quadrante 4"
elif angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
    print "Sobre eixos"