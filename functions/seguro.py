# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Cálculo de seguro

def calcula_seguro(preco, lista):
	total_pontos = 0
	resultado = []
	risco = None

	if int(lista[0]) <= 21: 
		total_pontos += 20
	elif  int(lista[0]) > 21 and int(lista[0]) <= 30: 
		total_pontos += 15
	elif int(lista[0]) > 31 and int(lista[0]) <= 40:
		total_pontos += 12
	elif int(lista[0]) > 41 and int(lista[0]) <= 60:
		total_pontos += 10
	elif int(lista[0]) > 60:
		total_pontos += 20

	if lista[1] == True:
		total_pontos += 10
	else:
		total_pontos += 20
	if lista[5] == True:
		total_pontos += 10
	else:
		total_pontos += 20
	if lista[6] == "Trabalho":
		total_pontos += 10
	else:
		total_pontos += 20

	for n in range(2, 5):
		if lista[n] == True:
			total_pontos += 20
		else:
			total_pontos += 10
	
	if total_pontos <= 80:
		risco = "Risco Baixo"
		valor_pago = preco * 0.1
	elif total_pontos > 80 and total_pontos <= 100:
		risco = "Risco Medio"
		valor_pago = preco * 0.2
	elif total_pontos > 100:
		risco = "Risco Alto"
		valor_pago = preco * 0.3

	resultado.append(total_pontos)
	resultado.append(risco)
	resultado.append(valor_pago)

	return resultado