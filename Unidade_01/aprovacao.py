# coding: utf-8
# Porcentagem de aprovados
# (c) Héricles Emanuel, UFCG, Programação 1

print "Análise da Turma"
print "==="

aprovados = int(raw_input("Número de aprovados? "))
reprovados = int(raw_input("Número de reprovados? "))

print "---"

total_alunos = aprovados + reprovados
p_aprovados = (float(aprovados) / total_alunos) * 100
p_reprovados = (float(reprovados) / total_alunos) * 100.0

print "Total de alunos na turma: %i" % total_alunos
print "Aprovados: %i = %.1f%%" % (aprovados, p_aprovados)
print "Reprovados: %i = %.1f%%" % (reprovados, p_reprovados)