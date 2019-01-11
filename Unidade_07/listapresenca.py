# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Lista Presença

def cria_lista_presenca(turmas, nomes, num):
	indice = []
	presentes = []
	for i in range(len(turmas)):
		if num == turmas[i]:
			indice.append(i)
	for n in range(len(indice)):
		presentes.append(nomes[indice[n]])
	return presentes

turmas = [1, 2, 2, 4, 5, 3, 5]
nomes = ["Maria", "Pedro", "Carlos", "Ana", "Carla", "Joao", "Jose"]
print cria_lista_presenca(turmas, nomes, 5)
