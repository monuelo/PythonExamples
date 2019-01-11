# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Classificação de Elementos Utilizando a Média dos Extremos
 
num_numeros = int(raw_input())
numeros = []
menores = 0
maiores = 0
 
if num_numeros > 1:
    for i in range(0, num_numeros):
        num = int(raw_input())
        numeros.append(num)
 
    maior = numeros[0]
    menor = numeros[0]
 
    for i in numeros:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
     
    media_extremos = (float(maior) + float(menor)) / 2
 
    for e in numeros:
        if e > media_extremos:
            maiores += 1
        elif e < media_extremos:
            menores += 1
         
    print "Menor número: %s" % menor
    print "Maior número: %s" % maior
    print "Média dos extremos: %.2f" % media_extremos 
    print "%i número(s) abaixo da média" % menores
    print "%i número(s) acima da média" % maiores