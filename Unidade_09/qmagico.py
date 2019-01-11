# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: É quadrado Mágico?

def eh_quadrado_magico(m):
	somas_all = []
	eh_magico = True
	soma = 0
	for e in range(len(m[0])):
		soma += m[0][e]

# Linhas
	for i in range(len(m)):
		somados = 0
		for e in range(len(m[i])):
			somados += (m[i][e])
		soma_all.append(somados)
# Colunas
	x = 0
	while x < len(m):
		somados = 0
		for n in range(len(m)):
			somados += m[n][x]
		x += 1
		soma_all.append(somados)

# Diagonal1
	x = len(m) - 1
	somados = 0
	for i in range(len(m)):
		somados += m[i][x]
		x -= 1
	soma_all.append(somados)
# Diagonal 2	
	x = len(m) -1
	somados = 0
	for i in range(len(m) -1, -1, -1):
		somados += m[i][x]
		x -= 1
	soma_all.append(somados)

for i in somados:
	if i != soma:
		return False		 	 
		 	 
	if eh_magico:
		return True
quadrado1 = [[2,7,6],[9,5,1],[4,3,8]]
print eh_quadrado_magico(quadrado1)

