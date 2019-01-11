# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva
# Matrícula: 117110647
# Atividade: QUantas PAs?
pas = 0
razao = int(raw_input())
while True:
    is_pa = True
    string = ""
    lista = raw_input().split()
    if lista[0] == "fim":
        break
    for i in range(len(lista) - 1):
        if int(lista[i]) != int(lista[i + 1]) - razao:
            is_pa = False
    if is_pa == True:
        pas += 1
print pas
