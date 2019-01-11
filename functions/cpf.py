# coding: utf-8
# Aluno: Héricles Emanuel
# Matrícula: 117110647
# Atividade: Dígitos de Verificação do CPF
def calcula_digitos_verificacao(digitos):
	n = 2
	str_digito = ""
	sum_produtos = 0
	for i in range(len(digitos) - 1, -1, -1):
		sum_produtos += (int(digitos[i]) * n)
		n += 1
	sum_produtos = (10 * sum_produtos) % 11
	if sum_produtos == 10:
		str_digito += "0"
	else:
		str_digito += str(sum_produtos)
	digitos += str_digito
	n = 2
	sum_produtos = 0
	for i in range(len(digitos) - 1, -1, -1):
		sum_produtos += (int(digitos[i]) * n)
		n += 1
	sum_produtos = (10 * sum_produtos) % 11
	if sum_produtos == 10:
		str_digito += "0"
	else:
		str_digito += str(sum_produtos)
	return str_digito

assert calcula_digitos_verificacao('153245875') == '40'