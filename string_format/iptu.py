# coding: utf-8
# IPTU
# (c) Héricles Emanuel, UFCG, Programação 1

area = float(raw_input("Área construída? "))
aliquota = float(raw_input("Alíquota? "))
valor_iptu = area * aliquota + 35.00

	#Formas de Pagamento
		# À vista
pag_vista = valor_iptu * 0.75
		# Em 6 parcelas
pag_6 = valor_iptu * 0.95
		# Em 10 parcelas
pag_10 = valor_iptu

print "IPTU: R$ %.2f" % valor_iptu

	# Valor das parcelas
		# 6 Parcelas
parcela_6 = pag_6 / 6
		# 10 Parcelas
parcela_10 = pag_10 / 10

print "\nPagamento:"
print "1. Quota única. R$ %.2f" % pag_vista
print "2. Em 6 parcelas. Total: R$ %.2f" % pag_6
print "   6 x R$ %.2f" % parcela_6
print "3. Em 10 parcelas. Total: R$ %.2f" % pag_10
print "   10 x R$ %.2f" % parcela_10