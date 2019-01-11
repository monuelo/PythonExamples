# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Palavras com Letras Dobradas

num_palavras = int(raw_input())
list_dobrada = []
list_nao_dobrada = []

for i in range(0, num_palavras):
    dobradas = 0
    palavra = raw_input()
    for letra in range(0, len(palavra) - 1):
        if palavra[letra] == palavra [letra + 1]:
            dobradas += 1
            break
    if dobradas > 0:
        list_dobrada.append(palavra)
    else:
        list_nao_dobrada.append(palavra)

print "%i palavra(s) com letras dobradas:" % len(list_dobrada)
for i in range(0, len(list_dobrada)):
    print list_dobrada[i]
print "---"
print "%i palavra(s) sem letras dobradas:" % len(list_nao_dobrada)
for i in range(0, len(list_nao_dobrada)):
    print list_nao_dobrada[i]
