# coding: utf-8
# Despesas de Cinema
# (c) Héricles Emanuel, UFCG, Programação 1

dia = raw_input("Dia da semana? ")
orcamento = raw_input("Orcamento? R$ ")
adultos = raw_input("Numero de adultos? ")
criancas = raw_input("Numero de criancas? ")
pizza = raw_input("Preco da pizza? R$ ")
refrigerante = raw_input("Preco do refrigerante? R$ ")
estacionamento = raw_input("Preco do estacionamento? R$ ")
cinema = raw_input("Preco do ingresso do cinema? R$ ")

gastos_alimentacao = float(pizza) + float(refrigerante)
gastos_cinema = int(adultos) * (float(cinema) + 2) + int(criancas) * ((float(cinema) / 2) + 2)
gastos_total = gastos_cinema + gastos_alimentacao + float(estacionamento)
gastos_media = gastos_total / (int(adultos) + int(criancas))
saldo = float(orcamento) - gastos_total

gastos_alimentacao = str(gastos_alimentacao)
gastos_cinema = str(gastos_cinema)
gastos_total = str(gastos_total)
gastos_media = str(gastos_media)
saldo = str(saldo)

print "========== Despesas de %s ==========" % dia
print "Despesas com alimentacao: R$ %s" % gastos_alimentacao
print "Despesas com cimena: R$ %s" % gastos_cinema
print "Despesas por pessoa: R$ %s" % gastos_media
print "Saldo disponivel: %s" % saldo