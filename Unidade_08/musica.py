# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Já sei tocar essa música

def sei_tocar_musica(musica, acordes):
	count = 0
	for i in range(len(musica)):
		if musica[i] in acordes: 
			count += 1
	return True (if count == len(musica)) else False