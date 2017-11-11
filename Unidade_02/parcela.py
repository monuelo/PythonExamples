# coding: utf-8
# Passagem Aérea
# (c) Héricles Emanuel, UFCG, Programação 1

milhas = float(raw_input())
aliquota = float(raw_input())
valor_passagem = (milhas * aliquota) + 51.00

print "Valor da passagem: R$ %.2f" % valor_passagem

	#Formas de Pagamento
		# À vista
pag_vista = valor_passagem * 0.75
		# Em 6 parcelas
pag_6 = valor_passagem * 0.95
		# Em 10 parcelas
pag_10 = valor_passagem
	
	# Valor das parcelas
		# 6 Parcelas
parcela_6 = pag_6 / 6
		# 10 Parcelas
parcela_10 = pag_10 / 10

print "\nPagamento:"
print "1. À vista. R$ %.2f" % pag_vista
print "2. Em 6 parcelas. Total: R$ %.2f" % pag_6
print "   6 x R$ %.2f" % parcela_6
print "3. Em 10 parcelas. Total: R$ %.2f" % pag_10
print "   10 x R$ %.2f" % parcela_10