# coding: utf-8
# Orçamento Construção
# (c) Héricles Emanuel, UFCG, Programação 1

preco_tijolo = float(raw_input("Digite o preço da unidade do tijolo (Em reais): "))
altura_tijolo = float(raw_input("Digite a altura do tijolo (Em metros): "))
comprimento_tijolo = float(raw_input("Digite o comprimento do tijolo (Em metros): "))
altura_parede = float(raw_input("Digite a altura das paredes (Em metros): "))
comprimento_parede = float(raw_input("Digite o comprimento das paredes (Em metros): "))

num_tijolos_altura = altura_parede / altura_tijolo
num_tijolos_comprimento = comprimento_parede / comprimento_tijolo
num_tijolos_total = num_tijolos_comprimento * num_tijolos_altura
preco_total = num_tijolos_total * preco_tijolo

print "O número total de tijolos é %.1f e o orçamento final é de R$ %.1f" % (num_tijolos_total, preco_total)
