# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Limite de gastos

limite = float(raw_input())
entradas = []

while True:
  entrada_integra = raw_input()
  entradas = entrada_integra.split(" ")
  if entradas[0] == "fim":
    break
  soma = 0
  for i in entradas:
    soma += float(i)
  if soma / len(entradas) < limite / 2:
  	break
  if soma / len(entradas) > limite:
    print entrada_integra
