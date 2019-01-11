# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Maioridade Penal Função

def maioridade_penal(pessoas, idade):
	pessoas = pessoas.split()
	idade = idade.split()
	string = ""
	for i in range(len(idade)):
		if int(idade[i]) >= 18:
			string += pessoas[i]
			string += " "
	return string.strip()


assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"