# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Fundo de Investimento
soma = 0
somados = 0
while True:
    valor = float(raw_input())
    soma += valor
    somados += 1
    media = soma / somados
    if valor < media:
        soma = soma - valor
        media = soma / (somados - 1)
        break

print "Saldo total do FIS: R$%.2f." % soma
print "Média das contribuições: R$%.2f." % media