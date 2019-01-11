# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Aprovados e Reprovados
 
n_alunos = int(raw_input())
reprovados = []
aprovados = []
soma_reprovados = 0
soma_aprovados = 0

for i in range(0, n_alunos):
    nota = float(raw_input())
    if nota < 7.0:
        reprovados.append(nota)
        soma_reprovados += nota
    else:
        aprovados.append(nota)
        soma_aprovados += nota
print "Reprovados: %i" % len(reprovados)
if len(reprovados) > 0:  
    media_reprovados = soma_reprovados / len(reprovados)
    print "Média: %.1f" % media_reprovados
 
print "\nAprovados: %i" % len(aprovados)
if len(aprovados) > 0:
    media_aprovados = soma_aprovados / len(aprovados)
    print "Média: %.1f" % media_aprovados