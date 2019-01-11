# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Subtração de Polinômios

def subtrai_polinomios(p1,p2):
    resultado = []
    x = 0
            
    while True:
        subtracao = p1[x] - p2[x]
        resultado.append(subtracao)
        x+=1
            
        if x == len(p1):
            for i in range(x,len(p2)):
                resultado.append(-p2[i])
            break
        elif x == len(p2):
            for i in range(x,len(p1)):
                resultado.append(p1[i])
            break
                
    if resultado[-1] == 0:
        resultado.pop(-1)
        
    return resultado
